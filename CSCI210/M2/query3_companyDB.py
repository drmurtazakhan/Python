# query3_companyDB.py
# Run: python query3_companyDB.py

import sqlite3

# 1. Connect to the existing COMPANY_DB database
connection = sqlite3.connect("COMPANY_DB")
cursor = connection.cursor()

# =====================================================================
# QUERY 3: JOIN Operation for Department 'D1'
# Showing Employee Name, Department Code, and Location
# =====================================================================
print("--- Employees in D1 with Department Details (Using JOIN) ---")
query_join = """
SELECT EMPLOYEE.Name, DEPARTMENT.DeptID, DEPARTMENT.Location
FROM EMPLOYEE
INNER JOIN DEPARTMENT ON EMPLOYEE.DeptID = DEPARTMENT.DeptID
WHERE EMPLOYEE.DeptID = 'D1'
"""

cursor.execute(query_join)
rows_join = cursor.fetchall()

for row in rows_join:
    print(f"Employee Name: {row[0]} | Dept Code: {row[1]} | Location: {row[2]}")
print()


# 2. Close the database connection
connection.close()