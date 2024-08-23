import os
import yaml
import zipfile
import gdown


def read_yaml(path_to_yaml: str):
    with open(os.path.join(os.getcwd(), path_to_yaml), "r") as file:
        sav_link_collection = yaml.safe_load(file)
    return sav_link_collection


def unzip_file(zip_path: str, dest: 'str', extract_to: str = '.'):
    new_var = os.path.join(dest, extract_to)
    print(f"Extracting {zip_path}")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(new_var)
        print(f"Extracted {zip_path}")
        
        
def delete_zip_file(zip_path: str):
    # Check if file exists
    if os.path.exists(zip_path):
        os.remove(zip_path)
        print(f"File {zip_path} has been deleted.")
    else:
        print(f"Error: {zip_path} does not exist.")
    

def create_folder(path):
    destination = os.path.join(path)
    if os.path.exists(destination) and os.path.isdir(destination):
        print(f"Folder in '{destination}' already exists.")
    else:
        os.makedirs(destination, exist_ok=False)


    
    