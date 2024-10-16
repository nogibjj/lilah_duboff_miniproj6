# calls all the extract, transform, query functions to main
"""
ETL-Query script
"""
import sys
import argparse
from SQL_files.extract import extract_data
from SQL_files.transform import transform_1, transform_2
from SQL_files.complex_query import complex_query

test_query = """
SELECT 
    r1.Industry,
    COUNT(r1.Employee_ID) AS count_of_employees,
    AVG(r1.Hours_Worked_Per_Week) AS avg_hours_worked,
    AVG(CASE 
        WHEN r2.Stress_Level = 'High' THEN 1 
        WHEN r2.Stress_Level = 'Medium' THEN 2 
        WHEN r2.Stress_Level = 'Low' THEN 3 
        ELSE NULL 
    END) AS avg_stress_level
FROM 
    remote_health1 AS r1
JOIN 
    remote_health2 AS r2 
ON 
    r1.Employee_ID = r2.Employee_ID
GROUP BY 
    r1.Industry
ORDER BY 
    count_of_employees DESC;
"""
test_query2 = """
SELECT * FROM remote_health1 LIMIT 5
"""

table1 = "remote_health1"
table2 = "remote_health2"
url1 = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_1_remote_work_mental_health_data.csv"
url2 = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_2_remote_work_mental_health_data.csv"
path1 = "data/table_1_remote_work_mental_health_data.csv"
path2 = "data/table_2_remote_work_mental_health_data.csv"
folder = "data"


# Extract
# print("Extracting data...")
# extract_data(url1, url2, path1, path2, folder)

# Transform and load/create
# print("Transforming data...")
# transform_1(path1)
# transform_2(path2)


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
        transform_1(path1)
        transform_2(path2)
    elif args.action == "complex_query":
        print("Querying data...")
        # how to pass the query from the makefile to the complex_query function
        complex_query(args.query)

    else:
        print("Invalid action, please try again")


if __name__ == "__main__":
    main()
