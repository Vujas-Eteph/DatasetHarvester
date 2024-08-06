# Automatically download the SA-V dataset
# by Stéphane Vujasinovic


# - IMPORTS ---
import os
import yaml


# - FUNCTIONS ---
def read_yaml(path_to_yaml: str):
    with open(path_to_yaml, "r") as file:
        sav_link_collection = yaml.safe_load(file)
    return sav_link_collection


def download_datachunk(filename: str, url: str):
    os.system(f' wget -O {filename} "{url}"')


def extract_datachunk(filename: str, file_destination: str):
    os.system(f' tar -xf {filename} -C {file_destination}')


def download_and_extract_data_split(
    sav_link_collection: dict, file_destination: str, split: str
):
    sav_urls_split = sav_link_collection[split]
    for chunck_name, chunk_url in sav_urls_split.items():
        print(f"\n-- Downloading and Extracting {chunck_name} --")
        download_datachunk(chunck_name, chunk_url)
        extract_datachunk(chunck_name, file_destination)

        os.system(f'rm {chunck_name}')  # clean up

    print(f"\n-- Downloaded and Extracted SA-V {split} --")


# - CONSTANTS ---
PATH_TO_YAML = "download_SA_V.yaml"
DESTINATION_FILE = "adapt/path/to/SA_V"  # TODO: To adapt


# - MAIN ---
def main():
    sav_link_collection = read_yaml(PATH_TO_YAML)

    # Extract the SA-V dataset
    splits = ["train", "val", "test", "check_sum"]
    for split in splits:
        download_and_extract_data_split(
            sav_link_collection, DESTINATION_FILE, split)

# - RUN ---
if __name__ == "__main__":
    main()
