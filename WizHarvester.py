# Wizard to download VOS Datasets
import os
import yaml
import questionary
import gdown
import requests
import tarfile
import zipfile
import concurrent.futures


# ----
# MAIN
def main():
    YAML_CONFIG = "supported_datasets.yaml"
    gdrive_global_addr, datasets_info = prep_dict_config(YAML_CONFIG)

    parent_folder, selected_datasets, selected_splits, proceed = run_wizard(
        datasets_info
    )
    if not proceed:
        return

    os.makedirs(parent_folder, exist_ok=True)

    workers = min(len(selected_datasets), os.cpu_count())
    print(f"Using {workers} workers")

    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        futures = []
        for name in selected_datasets:
            # Run multiple workers asynchronously
            future = executor.submit(
                process_single_dataset,
                parent_folder,
                name,
                selected_splits,
                gdrive_global_addr,
                datasets_info[name],
            )
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:
                # raise exceptions caught during the worker process
                result = future.result()
                print(result)
            except Exception as e:
                print(f"Failed with error: {e}")

    print("\nData Harvestation completed")


# ---------
# FUNCTIONS
def process_single_dataset(
    parent_folder, name, selected_splits, gdrive_global_addr, datasets_info
):
    print(f"\n $$ Starting worker for dataset {name}")
    downloaded_files = download_dataset(
        parent_folder, name, selected_splits, gdrive_global_addr, datasets_info
    )

    if downloaded_files:
        extract_compressed_content(downloaded_files, selected_splits)
        return f"Successfully Downloaded and Extracted {name}"
    else:
        return f"Error with {name}"


def prep_dict_config(yaml_config):
    with open(yaml_config, "r") as file:
        yaml_config_dict = yaml.safe_load(file)

    gdrive_global_addr = yaml_config_dict.pop("GDrive_addr", "")
    datasets_info = yaml_config_dict

    return gdrive_global_addr, datasets_info


def run_wizard(available_datasets):
    parent_folder = questionary.path(
        "Parent folder to download the datasets (Use 'Tab'):", only_directories=True
    ).ask()

    if not parent_folder:
        print("Operation cancelled")
        return None, None, None, False

    selected_datasets = questionary.checkbox(
        "Select datasets to download ('Space' to select & 'Enter' to confirm):",
        choices=list(available_datasets.keys()),
    ).ask()

    if not selected_datasets:
        print("Exit, no datasets selected")
        return None, None, None, False

    print(f"\n Datasets selected: {selected_datasets}")
    selected_splits = questionary.checkbox(
        "UNselect splits to download ('Space' to UNselect & 'Enter' to confirm):",
        choices=[
            questionary.Choice("train", checked=True),
            questionary.Choice("valid", checked=True),
            questionary.Choice("test", checked=True),
        ],
    ).ask()

    if not selected_splits:
        print("Exit, no split selected")
        return None, None, None, False

    return parent_folder, selected_datasets, selected_splits, True


def filter_info_based_on_splits_selected(info, splits):
    if len(splits) == 3:
        return info

    if len(info) <= 1:
        return info

    # negative filtering (download all expect the unselected part)
    updated_info = {}
    unslected_splits = list(set(["train", "valid", "test"]) - set(splits))
    for label, url_link in info.items():
        if not any(s in label for s in unslected_splits):
            updated_info[label] = url_link
    info = updated_info

    return info


def download_dataset(parent_folder, name, splits, gdrive_global_addr, info):
    target_dir = os.path.join(parent_folder, name)
    os.makedirs(target_dir, exist_ok=True)
    downloaded_files = []

    info = filter_info_based_on_splits_selected(info, splits)

    # download content
    for label, url_link in info.items():
        if is_gdrive_link(url_link):
            url_link = gdrive_global_addr + url_link

        print(f"Starting download of {label} for {name}")
        output_path = os.path.join(target_dir, label)
        gdown.download(url_link, output_path, quiet=False)

        downloaded_files.append((label, output_path))

    return downloaded_files


def is_gdrive_link(url):
    if url.startswith("https://"):
        return False

    return True


def extract_compressed_content(downloaded_files, selected_splits):
    for label, file_path in downloaded_files:
        target_dir = os.path.dirname(file_path)

        if tarfile.is_tarfile(file_path):
            with tarfile.open(file_path) as tar:
                print(f"Starting extraction of {label}")
                tar.extractall(path=target_dir)
            os.remove(file_path)
        elif zipfile.is_zipfile(file_path):
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                print(f"Starting extraction of {label}")
                zip_ref.extractall(path=target_dir)
            os.remove(file_path)


# ---------
# EXECUTION
if __name__ == "__main__":
    main()
