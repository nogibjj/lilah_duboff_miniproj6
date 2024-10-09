# This file should take the cvs data and convert it into a database, or .db file
# performs the CREATE from CRUD operations
import sqlite3
import csv
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


def transform(data1, data2):
    """Transforms and loads data into the database"""

    payload1 = csv.reader(open(data1, newline=""), delimiter=",")
    next(payload1)

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
        c.execute("SHOW TABLES FROM remotehealthdb LIKE 'remote_health*'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                        CREATE TABLE remote_health1 (
                                Employee_ID,
                                Gender, 
                                Age,
                                Job_Role,
                                Industry,
                                Years_of_Experience,
                                Work_Location,
                                Hours_Worked_Per_Week,
                                Number_of_Virtual_Meetings,
                                Work_Life_Balance_Rating,
                                Stress_Level,
                                Mental_Health_Condition,
                                Access_to_Mental_Health_Resources,
                                Productivity_Change,
                                Social_Isolation_Rating,
                                Satisfaction_with_Remote_Work,
                                Company_Support_for_Remote_Work,
                                Physical_Activity,
                                Sleep_Quality,
                                Region 
                            )
                        """
            )
        for _, row in payload1.iterrows():
            convert = (_,) + tuple(row)
            c.execute(f"INSERT INTO remotehealthdb VALUES {convert}")
    print(payload1)

    if not result:
        c.execute(
            """
                        CREATE TABLE remote_health2 (
                                Employee_ID,
                                Gender, 
                                Age,
                                Job_Role,
                                Industry,
                                Years_of_Experience,
                                Work_Location,
                                Hours_Worked_Per_Week,
                                Number_of_Virtual_Meetings,
                                Work_Life_Balance_Rating,
                                Stress_Level,
                                Mental_Health_Condition,
                                Access_to_Mental_Health_Resources,
                                Productivity_Change,
                                Social_Isolation_Rating,
                                Satisfaction_with_Remote_Work,
                                Company_Support_for_Remote_Work,
                                Physical_Activity,
                                Sleep_Quality,
                                Region 
                            )
                        """
        )
        for _, row in payload2.iterrows():
            convert = (_,) + tuple(row)
            c.execute(f"INSERT INTO remotehealthdb VALUES {convert}")
        c.execute("SHOW TABLES FROM remotehealthdb LIKE 'remote_health*'"),
    c.commit()
    c.close()
    print(payload2)
    return payload1, payload2
