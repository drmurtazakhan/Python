# insert_company_data.py
# Run: python insert_company_data.py

import sqlite3

# 1. Connect to the existing COMPANY_DB database
connection = sqlite3.connect("COMPANY_DB")
cursor = connection.cursor()

# 2. Enforce Foreign Key constraints
cursor.execute("PRAGMA foreign_keys = ON;")

print("Starting data insertion...")

# =====================================================================
# STEP 1: Insert Data into DEPARTMENT
# =====================================================================
departments = [
    ('D1', 'Sales', 'New York'),
    ('D2', 'Marketing', 'Chicago'),
    ('D3', 'IT', 'San Francisco'),
    ('D5', 'R&D', 'Boston')
]

cursor.executemany("INSERT OR IGNORE INTO DEPARTMENT VALUES (?, ?, ?)", departments)
print("- Department records processed successfully.")


# =====================================================================
# STEP 2: Fetch Valid Department IDs from the Database
# =====================================================================
cursor.execute("SELECT DeptID FROM DEPARTMENT")
# Fetchall returns a list of tuples like [('D1',), ('D2',)...], so we flatten it into a clean set
valid_dept_ids = {row[0] for row in cursor.fetchall()}


# =====================================================================
# STEP 3: Validate and Insert Employees
# =====================================================================
employees = [
    (101, 'Alice Smith', 60000, 'D1'),
    (102, 'Bob Johnson', 75000, 'D2'),
    (103, 'Charlie Brown', 50000, 'D1'),
    (104, 'David Lee', 90000, 'D3'),
    (105, 'Eva Green', 65000, 'D4')  # Python will catch and skip this before hitting SQL
]

print("Validating employee records against active departments...")
for emp in employees:
    emp_id, emp_name, salary, dept_id = emp
    
    # Check if the employee's department exists in our valid set
    if dept_id in valid_dept_ids:
        cursor.execute("INSERT OR IGNORE INTO EMPLOYEE VALUES (?, ?, ?, ?)", emp)
        print(f"  [Inserted] {emp_name} assigned to {dept_id}.")
    else:
        # Skip the record entirely
        print(f"  [Skipped Invalid Record] {emp_name} has an invalid DeptID '{dept_id}'.")

print("- Employee data processing complete.")

# 3. Save changes and close connection
connection.commit()
print("All valid records saved to COMPANY_DB successfully!")

connection.close()