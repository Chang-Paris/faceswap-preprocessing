"""
Download videos from excel sheet
"""
import pandas as pd
import os
import urllib.request

# get file
file_path = ""
sheet = pd.read_excel(
    file_path
).to_dict(orient="record")

# Initialize output folder
output_folder = './output_video/'
os.makedirs(output_folder, exist_ok=True)


def download_vid(url, name):
    name = name + ".mp4"
    try:
        print("Downloading starts...\n")
        urllib.request.urlretrieve(url, name)
        print("Download completed..!!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    for record in sheet:
        file_name = os.path.join(output_folder, record["课件名称"] + "_" + record["课件编码"])
        print(file_name)
        download_vid(
            url=record["下载链接"],
            name=file_name
        )
