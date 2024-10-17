# calls all the extract, transform, query functions to main
"""
ETL-Query script
"""
import sys
import os
import argparse
from SQL_files.extract import extract_data
from SQL_files.transform import transform_1, transform_2
from SQL_files.complex_query import complex_query



url1 = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_1_remote_work_mental_health_data.csv"
url2 = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_2_remote_work_mental_health_data.csv"
path1 = "data/table_1_remote_work_mental_health_data.csv"
path2 = "data/table_2_remote_work_mental_health_data.csv"
folder = "data"



def arguments(args):
    """parses cli arguments"""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "action",
        help="--action to perform--",
        choices=["extract", "transform", "complex_query"],
    )

    args = parser.parse_args(args[:1])
    print(args.action)

    if args.action == "complex_query":
        parser.add_argument("query", help="--query to run--")
        print(parser.parse_args(sys.argv[1:]))
    return parser.parse_args(sys.argv[1:])


def main():
    """handles all the cli commands"""
    args = arguments(sys.argv[1:])

    if args.action == "extract":
        print("Extracting data...")
        extract_data(url1, url2, path1, path2, folder)
    elif args.action == "transform":
        print("Transforming data...")
        if os.path.exists(path1) and os.path.exists(path2):
            transform_1(path1)
            transform_2(path2)
        else:
            print("One of the files does not exist, please try again")
    elif args.action == "complex_query":
        print("Querying data...")
        complex_query(args.query)

    else:
        print("Invalid action, please try again")


if __name__ == "__main__":
    main()
