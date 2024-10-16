"""Asserting that the Data is being extracted from the url"""

from SQL_files.extract import extract_data
import os


def test_extract_data():
    url1 = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_1_remote_work_mental_health_data.csv"
    url2 = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_2_remote_work_mental_health_data.csv"
    test_path1 = "data/test_table_1_remote_work_mental_health_data.csv"
    test_path2 = "data/test_table_2_remote_work_mental_health_data.csv"
    folder = "data"
    result_1 = extract_data(url1, test_path1, folder)
    result_2 = extract_data(url2, test_path2, folder)
    assert os.path.exists(result_1)
    assert os.path.exists(result_2)

    os.remove(result_1)
    os.remove(result_2)


if __name__ == "__main__":
    test_extract_data()
