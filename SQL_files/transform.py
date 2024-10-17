# This file should take the cvs data and convert it into a database, or .db file
# performs the CREATE from CRUD operations
import csv
import os
from databricks import sql
from dotenv import load_dotenv


def transform_1(data1):
    """Transforms and loads first data into the database"""

    payload1 = csv.reader(open(data1, newline=""), delimiter=",")
    next(payload1)

    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'remote_health1'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                    CREATE TABLE remote_health1 (
                        Employee_ID STRING,
                        Age INTEGER,
                        Gender STRING,
                        Job_Role STRING,
                        Industry STRING,
                        Years_of_Experience INTEGER,
                        Work_Location STRING,
                        Hours_Worked_Per_Week INTEGER,
                        Number_of_Virtual_Meetings INTEGER,
                        Work_Life_Balance_Rating INTEGER
                    )
                """
            )
        for idx, row in enumerate(payload1):
            print(f"Inserting row {idx + 1}: {row}")
            c.execute(
                """
                    INSERT INTO remote_health1 (
                            Employee_ID, Age, Gender, Job_Role, Industry, Years_of_Experience, 
                            Work_Location, Hours_Worked_Per_Week, Number_of_Virtual_Meetings, 
                            Work_Life_Balance_Rating
                            ) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                row,
            )
            
        connection.commit()
        c.execute("SHOW TABLES FROM default LIKE 'remote_health1'")
        result = c.fetchall()
        c.close()
        print("Successfully transformed and loaded first data!")
    return "Success"


def transform_2(data2):
    """Transforms and loads second data into the database"""

    payload2 = csv.reader(open(data2, newline=""), delimiter=",")
    next(payload2)

    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'remote_health2'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                    CREATE TABLE remote_health2 (
                            Employee_ID STRING,
                            Stress_Level STRING,
                            Mental_Health_Condition STRING,
                            Access_to_Mental_Health_Resources BOOLEAN,
                            Productivity_Change STRING,
                            Social_Isolation_Rating INTEGER,
                            Satisfaction_with_Remote_Work STRING,
                            Company_Support_for_Remote_Work INTEGER,
                            Physical_Activity STRING,
                            Sleep_Quality STRING,
                            Region STRING 
                    )
                """
            )

        for idx, row in enumerate(payload2):
            print(f"Inserting row {idx + 1}: {row}")
            c.execute(
                """
                    INSERT INTO remote_health2 (
                            Employee_ID, Stress_Level, Mental_Health_Condition, 
                            Access_to_Mental_Health_Resources, Productivity_Change, 
                            Social_Isolation_Rating, Satisfaction_with_Remote_Work, 
                            Company_Support_for_Remote_Work, Physical_Activity, Sleep_Quality, Region
                            ) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                row,
            )
        connection.commit()
        c.execute("SHOW TABLES FROM default LIKE 'remote_health2'")
        c.close()
        print("Successfully transformed and loaded second data!")
    return "Success"
