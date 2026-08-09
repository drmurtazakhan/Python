# query1_companyDB.py
# Run: python query1_companyDB.py

import sqlite3

# 1. Connect to the existing COMPANY_DB database
connection = sqlite3.connect("COMPANY_DB")
cursor = connection.cursor()

# =====================================================================
# QUERY 1: Employees with a salary greater than 60,000
# =====================================================================
print("--- Employees with Salary > 60,000 ---")
query_salary = "SELECT * FROM EMPLOYEE WHERE Salary > 60000"

cursor.execute(query_salary)
rows_salary = cursor.fetchall()

for row in rows_salary:
    print(f"ID: {row[0]} | Name: {row[1]} | Salary: ${row[2]:,} | DeptID: {row[3]}")
print()  # Empty line for spacing

# 2. Close the database connection
connection.close()
