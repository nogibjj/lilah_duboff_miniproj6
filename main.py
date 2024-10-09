# calls all the extract, transform, query functions to main
"""
ETL-Query script
"""

from SQL_files.extract import extract_data
from SQL_files.transform import transform
from SQL_files.query import create, read, update, delete, query_1, query_2

database1 = "remotehealthDB.db"
database2 = "remotehealthDB2.db"
table1 = "remote_health_1"
table2 = "remote_health_2"
url1 = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_1_remote_work_mental_health_data.csv"
url2 = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/table_2_remote_work_mental_health_data.csv"
path1 = "data/table_1_remote_work_mental_health_data.csv"
path2 = "data/table_2_remote_work_mental_health_data.csv"
folder = "data"
payload1 = (
    "EMP5001",
    6,
    "Female",
    "Pirate",
    "Theft",
    12,
    "Hybrid",
    46,
    7,
    2,
    "High",
    "Scurvy",
    "No",
    "Decrease",
    1,
    "Unsatisfied",
    1,
    "Weekly",
    "Good",
    "Caribbean",
)
payload2 = (
    "EMP6050",
    40,
    "Male",
    "Wizard",
    "Corporate",
    12,
    "Hybrid",
    46,
    7,
    2,
    "Low",
    "Schizophrenia",
    "No",
    "Decrease",
    1,
    "Satisfied",
    1,
    "Weekly",
    "Good",
    "Narnia",
)

# Extract
print("Extracting data...")
extract_data(url1, url2, path1, path2, folder)

# Transform and load/create
print("Transforming data...")
transform(path1, path2)


# CREATE
create(payload1, payload2, database1, database2,table1, table2)

# READ
read(database1, database2, table1, table2)

# UPDATE
update(database1, database2, table1, table2, "Age", 35, "EMP0040")

# DELETE
delete(database1, database2, table1, table2, "EMP0040")


# Query
print("First query...")
print(query_1())
print("Second query...")
print(query_2())
