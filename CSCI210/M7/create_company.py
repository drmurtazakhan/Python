# Run: & "C:\0MAK\install\python\312\python.exe" create_company.py
# python create_company.py
import ssl
import pymysql

# Update these 3 fields with your Aiven credentials
HOST = "mysql-test1-drkhan-proj1.e.aivencloud.com"  # Your Aiven host
PORT = 11820    # Your port number as an integer
#PASSWORD = ""  # Your Aiven password

ssl_context = ssl.create_default_context(cafile="ca.pem")

# 1. Connect to Aiven defaultdb
conn = pymysql.connect(
    host=HOST,
    port=PORT,
    user="avnadmin",
    password=PASSWORD,
    database="defaultdb",
    ssl=ssl_context
)

cursor = conn.cursor()

# 2. Create and switch to 'company' database
cursor.execute("CREATE DATABASE IF NOT EXISTS company;")
cursor.execute("USE company;")

# 3. Create EMPLOYEE table (MySQL compatible types)
create_table_sql = """
CREATE TABLE IF NOT EXISTS EMPLOYEE (
    EmployeeID INT NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Salary DECIMAL(10, 2),
    DeptID VARCHAR(5),
    CONSTRAINT PK_EMPLOYEE PRIMARY KEY (EmployeeID)
);
"""
cursor.execute(create_table_sql)

# 4. Insert records
employees = [
    (101, 'Alice Smith', 60000, 'D1'),
    (102, 'Bob Johnson', 75000, 'D2'),
    (103, 'Charlie Brown', 50000, 'D1'),
    (104, 'David Lee', 90000, 'D3'),
    (105, 'Eva Green', 65000, 'D4')
]

insert_sql = "INSERT INTO EMPLOYEE (EmployeeID, Name, Salary, DeptID) VALUES (%s, %s, %s, %s);"

# executemany inserts all records efficiently in one batch
cursor.executemany(insert_sql, employees)

# Commit changes to cloud database
conn.commit()

print("Database 'company', table 'EMPLOYEE', and 5 records created successfully!")

cursor.close()
conn.close()