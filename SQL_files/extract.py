# can use this file to extract csv from a url
""" This file can take csv data from a url and extract it to be transformed and queried """

import requests
import os

def extract_data(
    url1="""https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_1_remote_work_mental_health_data.csv""",
    url2="""https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_2_remote_work_mental_health_data.csv""",
    path1="data/table_1_remote_work_mental_health_data.csv",
    path2="data/table_2_remote_work_mental_health_data.csv",
    directory="data",
):
    """Extract data from a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url1) as r:
        with open(path1, "wb") as f:
            f.write(r.content)
    with requests.get(url2) as r:
        with open(path2, "wb") as f:
            f.write(r.content)
    return path1, path2
