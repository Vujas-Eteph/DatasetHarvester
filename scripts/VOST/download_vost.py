# Automatically download the VOST dataset
# Reference: https://www.vostdataset.org/data.html

import gdown

# URL of the file to download
url = "https://tri-ml-public.s3.amazonaws.com/datasets/VOST.zip"

# Specify the path where you want to save the file
output = "VOST.zip"

# Use gdown to download the file
gdown.download(url, output, quiet=False)

print("Download completed successfully.")