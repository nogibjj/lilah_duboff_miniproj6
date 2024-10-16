"""This file takes the csv data and converts it into a database/.db file"""

from SQL_files.transform import transform_1, transform_2


def test_transform():
    result_1 = transform_1("data/table_1_remote_work_mental_health_data.csv")
    result_2 = transform_2("data/table_2_remote_work_mental_health_data.csv")
    assert result_1 is not None
    assert result_2 is not None


if __name__ == "__main__":
    test_transform()
