# Automatically download the LVOS 1 and LVOS 2 dataset
# Reference: https://github.com/LingyiHongfd/LVOS
# by Stéphane Vujasinovic


# - IMPORTS ---
import os
from utils.utils import *

# - FUNCTIONS ---

# - MAIN ---
def main():
    yaml_config = read_yaml("config.yaml")

    destination_folder = yaml_config["destination"]
    dataset_infos = yaml_config["dataset"]
    attributes_infos = yaml_config["attributes"]
    
    create_folder(destination_folder)
  
    for dataset, splits in dataset_infos.items():
        print(f"Downloading the {dataset} dataset")
        
        dataset_folder = os.path.join(destination_folder, dataset)
        create_folder(dataset_folder)
        
        for split, url in attributes_infos.items():
            print(split, url)
            split_folder = os.path.join(dataset_folder, split)
            dest_json_file = f"{split_folder}.json" 
            print(f"Downloading the json attributes for the {split} split")
            gdown.download(url, dest_json_file, quiet=False)
        
        for split, url in splits.items():
            split_folder = os.path.join(dataset_folder, split)
            dest_zip_file = f"{split_folder}.zip"  # Replace with the desired path and filename
            
            print(f"Downloading the {split} split")
            gdown.download(url, dest_zip_file, quiet=False)
            
            unzip_file(dest_zip_file, dataset_folder)
            delete_zip_file(dest_zip_file)


if __name__ == '__main__':
    main()