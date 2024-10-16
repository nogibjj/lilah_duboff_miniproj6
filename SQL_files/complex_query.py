"""Performs a query to join, aggregate, and sort the data"""

from dotenv import load_dotenv
from databricks import sql
import os


LOG_FILE = "query_log.md"


def log_query(query, result="none"):
    """Adds informationto a query log file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")


def complex_query(query):
    """Connects to the database and executes the query"""
    print(query, '--------!!!!')
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
    cursor.close()
    connection.close()
    log_query(f"{query}", result)
    return "Successfully completed query!"






