# query2_companyDB.py
# Run: python query2_companyDB.py

import sqlite3

# 1. Connect to the existing COMPANY_DB database
connection = sqlite3.connect("COMPANY_DB")
cursor = connection.cursor()

# =====================================================================
# QUERY 2: Employees belonging to Department 'D1' (Employee Table Only)
# =====================================================================
print("--- Employees in Department D1 (From EMPLOYEE Table) ---")
query_dept_d1 = "SELECT * FROM EMPLOYEE WHERE DeptID = 'D1'"

cursor.execute(query_dept_d1)
rows_dept = cursor.fetchall()

for row in rows_dept:
    print(f"ID: {row[0]} | Name: {row[1]} | Salary: ${row[2]:,} | DeptID: {row[3]}")
print()  # Empty line for spacing

# 2. Close the database connection
connection.close()