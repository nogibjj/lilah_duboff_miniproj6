"""Asserting that the Data is being extracted from the url"""

from SQL_files.extract import extract_data
import os

def test_extract_data():
    url = "https://github.com/lilah-duboff/data-for-URLS/blob/main/Impact_of_Remote_Work_on_Mental_Health.csv"
    test_path = "data/test_remote_work_mental_health_data.csv"
    folder = "data"
    result = extract_data(url, test_path, folder)
    assert os.path.exists(result)
    
    os.remove(result)


if __name__ == "__main__":
    test_extract_data()