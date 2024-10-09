import sqlite3
import os
from databricks import sql
from dotenv import load_dotenv

def create(payload1, data1, table1):
    """Create and insert into table"""
    conn = sqlite3.connect(data1)
    c = conn.cursor()
    c.execute(
        f"""
              CREATE TABLE IF NOT EXISTS {table1} (
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

    query = f"INSERT INTO {table1} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    c.execute(query, payload1)

    conn.commit()
    conn.close()

    print("Record inserted successfully")
    return "Record inserted successfully"



def read(data1, table1):
    """Read data from the table"""
    conn = sqlite3.connect(data1)
    c = conn.cursor()
    
    query = f"SELECT * FROM {table1} LIMIT 10"
    c.execute(query)

    read_result = c.fetchall()
    conn.close()
    
    return read_result


def update(data, table1, column, new_value, ID_number):
    """Update a specific column in a row based on Employee_ID"""
    conn = sqlite3.connect(data)
    c = conn.cursor()
    query = f"UPDATE {table1} SET {column} = ? WHERE Employee_ID = ?"
    c.execute(query, (new_value, ID_number))
    affected_rows = c.rowcount
    conn.commit()
    c.close()
    conn.close()

    if affected_rows == 0:
        print("No record found")
        return "No record found"
    print("Record updated successfully!")
    return "Record updated successfully!"


def delete(database1, table1, ID_number):
    """Delete a specific column in a row based on Employee_ID"""
    conn = sqlite3.connect(database1)
    c = conn.cursor()
    query = f"DELETE FROM {table1} WHERE Employee_ID = ?"
    c.execute(query, (ID_number,))
    changed_rows = c.rowcount
    conn.commit()
    c.close()
    conn.close()

    if changed_rows == 0:
        print("No record found")
        return "No record found"
    print("Record deleted successfully!")
    return "Record deleted successfully!"


def query_1():
    """queries the db for top five rows"""
    conn = sqlite3.connect("remotehealthDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM remote_health LIMIT 5")
    print("Top 5 rows of the remote_health table:")
    query_1_result = c.fetchall()
    print("Query is complete")
    conn.close()
    return query_1_result


def query_2():
    """queries the db for max hours worked per week,
    and collects the subsequent information"""
    conn = sqlite3.connect("remotehealthDB.db")
    c = conn.cursor()
    c.execute(
        "SELECT Job_Role, Industry, Hours_Worked_Per_Week, Stress_Level, Mental_Health_Condition FROM remote_health WHERE Hours_Worked_Per_Week=(SELECT MAX(Hours_worked_per_week) FROM remote_health) LIMIT 5"
    )
    print("Max hours worked per week from remote_health table:")
    query_2_result = c.fetchall()
    print("Query is complete!")
    conn.close()
    return query_2_result