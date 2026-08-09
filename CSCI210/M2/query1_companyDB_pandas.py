# query1_companyDB_pandas.py
# Run: python query1_companyDB_pandas.py

import sqlite3
import pandas as pd

connection = sqlite3.connect("COMPANY_DB")

print("--- Employees with Salary > 60,000 ---")
query_salary = "SELECT * FROM EMPLOYEE WHERE Salary > 60000"

# Read the SQL query directly into a DataFrame table
df = pd.read_sql_query(query_salary, connection)

# Display the table instantly
print(df)

connection.close()