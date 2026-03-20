# Run this in the MOSEv1 folder to download the MOSEv1 dataset.
#
# ATTENTION ! RUN IN BASH
# '''
# mkdir MOSEv1
# mv download_MOSEv1.py MOSEv1/download_MOSEv1.py
# cd MOSEv1
# python download_MOSEv1.py
# ''' 
#
# by Stéphane Vujasinovic


import os
import gdown
import tarfile
import requests


# ---------
# CONSTANTS
BASE_GDRIVE_URL = "https://drive.google.com/uc?id="
MOSE_GDRIVE_ID = {
    "train.tar.gz"      : "16Ns7a_frLaCo2ug18UIUkzVYFQqyd4N0",
    "valid.tar.gz"      : "1yFoacQ0i3J5q6LmnTVVNTTgGocuPB_hR",
    "meta_train.json"   : "1BwGlVBdGTvcRJ5Jezxn5Ucfyu32G2jkL",
    "meta_valid.json"   : "1MmhRXKXFnEwzaoeE0b_e_RQjvVLHOc7I",
    "SHA256SUMS"        : "1qSul3OYaCRhSLmx7rhJxM3nVcCmyK9Q3",
    "sample_submission_valid_all.zip" : "1qdkU6yZ0ZxZ0FzOXuRf9wRi5xNxLQoX4",
}


# ---------
# FUNCTIONS
def check_access_to_link(url):
    try:
        response = requests.get(url, stream=True, timeout=10)
        if response.status_code != 200:
            print(f"Access Denied: {response.status_code}")
            return
    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")


# ----
# MAIN
for label, url in MOSE_GDRIVE_ID.items():
    gdrive_link = BASE_GDRIVE_URL + url
    check_access_to_link(gdrive_link)

    print (f"Starting download of {label}.")
    gdown.download(gdrive_link, label, quiet=False, fuzzy=True)

    if "tar" in label:
        print (f"Extracting {label}.")
        with tarfile.open(label) as tar:
            tar.extractall()

        os.remove(label)

print("MOSEv1 downloaded and setup complete.")
