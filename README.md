[![Python Application Test with Github Actions](https://github.com/nogibjj/lilah_duboff_miniproj5/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/lilah_duboff_miniproj5/actions/workflows/main.yml)

![alt text](<passing_test_functions.png>)

# Python Script interacting with SQL Database
#### This project imports a csv dataset, converts it to a database, and performs CRUD operations to analyze data

#### Requirements:

- [X] Connect to a SQL database
- [X] Perform CRUD operations
- [X] Write at least two different SQL queries
- [X] Database connection
- [X] CI/CD pipeline
- [X] Test each operation works by loading the .db file into your pipeline 
- [X] README.md
- [X] Screenshot or log of successful database operations
- [X] Arch Diagram
- [X] CLI - BONUS 

---
### Folder Navigation
##### Here is a quick overview of how the folders are structured for this project:
---
- Project Folder
    - .devcontainer
        - devcontainer.json
        - Dockerfile
    - .github
        - workflows
            - main.yml
    - data
        - data csv file (optional to import into the folder, could use URL)
    - SQL_files
        - extract.py
        - query.py
        - transform.py
    - tests
        - test_extract.py
        - test_query.py
        - test_transform.py
    - ETL with SQLite.png (ETL diagram)
    - main.py
    - Makefile
    - passing_test_functions.png (screenshot of make test results)
    - queries.png (screenshot of query results)
    - README.md
    - remotehealthDB.db (database created from csv)
    - requirements.txt
---
### Workflow Summary and Explanation
##### This project contains the following dependencies:
- pylint == 2.15.3
- black == 22.3.0
- pytest == 7.1.3
- ruff == 0.0.284
- fire == 0.7.0
- requests == 2.32.3
---
### Arch Diagram and Explanation
##### The following diagram displays the map of how ETL processes work in SQLite. [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query For the ETL-Query lab
![alt text](ETL_diagram.png)

---
### Query Results
##### This screenshot displays the terminal results from the two query functions. The first query returns the first five rows of the table, and the second query returns a few rows that contain the highest number or hours worked per week. In this case, many rows contained 60hrs, which was the highest from the table, so I limited the query to return five results. In addition, we are only looking at the job title, industry, number of hours worked, stress level, and mental health condition.

![alt text](<queries.png>)