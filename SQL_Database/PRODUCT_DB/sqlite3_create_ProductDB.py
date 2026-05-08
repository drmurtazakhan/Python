# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:53:04 2024

@author: Dr. Murtaza Ali Khan
"""

import sqlite3

connection = sqlite3.connect("PRODUCT");

cursor = connection.cursor()

cursor.execute("CREATE TABLE ITEM (ItemCode TEXT, PurchaseDate DATE, ItemName TEXT, ItemPrice REAL, Category TEXT)")

cursor.execute("INSERT INTO ITEM VALUES('123', '2024-10-01', 'Bread', 0.20, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('124', '2024-10-01', 'Milk', 0.50, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('231', '2024-10-02', 'Apple', 0.60, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('233', '2024-10-02', 'Banana', 0.30, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('245', '2024-10-02', 'Mango', 0.90, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('321', '2024-10-03', 'Pen', 0.10, 'Stationary')")
cursor.execute("INSERT INTO ITEM VALUES('333', '2024-10-03', 'Notebook', 0.30, 'Stationary')")
cursor.execute("INSERT INTO ITEM VALUES('421', '2024-10-04', 'Eraser', 0.50, 'Stationary')")
cursor.execute("INSERT INTO ITEM VALUES('521', '2024-10-05', 'Chair', 3.00, 'Furniture')")
cursor.execute("INSERT INTO ITEM VALUES('551', '2024-10-05', 'Table', 5.00, 'Furniture')")
cursor.execute("INSERT INTO ITEM VALUES('611', '2024-10-06', 'Keyboard', 3.00, 'Electronics')")
cursor.execute("INSERT INTO ITEM VALUES('623', '2024-10-06', 'Mouse', 2.00, 'Electronics')")
cursor.execute("INSERT INTO ITEM VALUES('721', '2024-10-07', 'Calculator', 3.00, 'Electronics')")
cursor.execute("INSERT INTO ITEM VALUES('734', '2024-10-07', 'USB', 2.00, 'Electronics')")

connection.commit()

row = cursor.execute("SELECT * FROM ITEM").fetchall()
print(row)

for row in cursor.execute("SELECT * FROM ITEM"):
    print(row)

connection.close()