# Run: & "C:\0MAK\install\python\312\python.exe" check_db.py
# python check_db.py
import ssl
import pymysql

# Update these 3 fields with your Aiven credentials
HOST = "mysql-test1-drkhan-proj1.e.aivencloud.com"  # Your Aiven host
PORT = 11820    # Your port number as an integer
#PASSWORD = ""  # Your Aiven password

ssl_context = ssl.create_default_context(cafile="ca.pem")

conn = pymysql.connect(
    host=HOST,
    port=PORT,
    user="avnadmin",
    password=PASSWORD,
    ssl=ssl_context
)

cursor = conn.cursor()

# 1. Show all databases on your Aiven server
print("--- Databases on Aiven Cloud ---")
cursor.execute("SHOW DATABASES;")
for db in cursor.fetchall():
    print(db[0])

# 2. Select company database and read EMPLOYEE table
print("\n--- Rows in 'company.EMPLOYEE' ---")
cursor.execute("USE company;")
cursor.execute("SELECT * FROM EMPLOYEE;")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
