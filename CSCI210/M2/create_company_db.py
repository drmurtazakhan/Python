# create_company_db.py
# Run: python create_company_db.py
import sqlite3

# 1. Establish a connection to the company database file
# If the file 'COMPANY_DB' doesn't exist, SQLite will create it automatically
connection = sqlite3.connect("COMPANY_DB")

# 2. Create a cursor object to execute SQL commands
cursor = connection.cursor()

# 3. Enable foreign key support (good practice for relational data)
cursor.execute("PRAGMA foreign_keys = ON;")

print("Creating database schema...")

# 4. Create the DEPARTMENT table
# We create this first or alongside EMPLOYEE so relational structures are ready
cursor.execute("""
CREATE TABLE IF NOT EXISTS DEPARTMENT (
    DeptID TEXT NOT NULL,
    DeptName TEXT NOT NULL,
    Location TEXT,
    CONSTRAINT PK_DEPARTMENT PRIMARY KEY (DeptID)
)
""")
print("- DEPARTMENT table created successfully.")

# 5. Create the EMPLOYEE table
cursor.execute("""
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    EmployeeID INTEGER NOT NULL,
    Name TEXT NOT NULL,
    Salary REAL,
    DeptID TEXT,
    CONSTRAINT PK_EMPLOYEE PRIMARY KEY (EmployeeID),
    CONSTRAINT FK_EMP_DEPT FOREIGN KEY (DeptID) REFERENCES DEPARTMENT(DeptID)
)
""")
print("- EMPLOYEE table created successfully.")

# 6. Commit (save) the changes to the database file
connection.commit()
print("Database schema saved successfully!")

# 7. Close the connection to free up system resources
connection.close()