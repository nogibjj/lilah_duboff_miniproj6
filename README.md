

![alt text](make_test_results.png)

# Python Script interacting with SQL Database
#### The purpose of this project is to perform ETL functions on a csv file, connect to an external database (databricks), and perform a complex query that includes joins, aggregation, and sorting

#### Requirements:

- [X] Connect to a SQL database in databricks
- [X] Design a complex SQL query involving joins, aggregation, and sorting
- [X] Provide an explanation for what the query is doing and the expected results
- [X] CI/CD pipeline
- [X] Written or video explanation of the query
- [X] README.md
- [X] Potentially use CLI


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
        - Table 1 csv file
        - Table 2 csv file
    - SQL_files
        - complex_query.py
        - extract.py
        - transform.py
    - main.py
    - Makefile
    - query_log.md (markdown that logs all queries made)
    - README.md
    - requirements.txt
    - test_main.py
---
### Workflow Summary and Explanation
##### This project contains the following dependencies:
- pylint == 2.15.3
- black == 22.3.0
- pytest == 7.1.3
- ruff == 0.0.284
- fire == 0.7.0
- requests == 2.32.3
- pandas == 2.2.2
- python-dotenv == 1.0.1
- databricks-sql-connector == 3.4.0
---
### What is the Purpose of this Project?
##### The purpise of this project is to perform and ETL and a complex query by connecting to an external database. To set up data for the join, I downloaded a public dataset from Kaggle, that collected information about remote work and its impacts on mental health conditions and stress levels. I split this data into two separate files, one with demographics and job information, and one with the health statistics collected. The data was then passed as a url through an extract function to return two file paths. 

##### Next, a connection with the databricks warehouse was established, and the data was transformed/cleaned and loaded as two tables (remote_health1 and remote_health2) into the database. 

##### Finally, after the tables are successfully loaded into the database, any type of query can be performed to explore the data. 

___
### What is the Goal of the Query?
##### In this project, the complex query I ran can be seen in the query_log.md file, or in the screenshot below. I first took the count of how many employees were in the dataset, then found the average number of hours worked per week overall. From there, I found the average number of hours worked per week, grouped by stress level(Low, Medium, or High). Then, I joined the two tables together using an automatic inner merge, where the Employee ID number of Table 1 matched that of Table 2. Finally, I grouped it by industry, and then ordered the data by the Employee ID number in descending order.

##### Query (Reformatted from the makefile):
![alt text](query_image.png)

##### Result:
![alt text](query_result.png)

### Integrating CLI Tools 
##### To make this project accessible from the terminal, I created a Command Line Tool (CLI) to be able to run the project with simple commands. In the main.py file, I utilized the argparse package to create the CLI, which lets the user choose between three actions: "extract," "transform," and "complex_query." The arguments function parses the CLI arguments, with the "complex_query" action requiring an additional query argument. This is where you would input any query of your choice into the makefile. The main function executes the appropriate action based on the user's input: extracting data, transforming data, or running a complex query. Depending on the action, it calls specific functions (extract_data, transform_1, transform_2, complex_query). Finally, the script runs the main function if executed as the main module.
___
### Arch Diagram 
##### The following diagram displays the map of how ETL processes work. [E] Extract a dataset from URL, [T] Transform, [L] Load into SQLite Database and [Q] Query For the ETL-Query lab
![alt text](<ETL_diagram copy.png>)


