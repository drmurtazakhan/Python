# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:53:04 2024

@author: Dr. Murtaza Ali Khan
"""

import sqlite3

connection = sqlite3.connect("TRADE_DB");

cursor = connection.cursor()

cursor.execute("CREATE TABLE ITEM (ItemCode TEXT, PurchaseDate DATE, ItemName TEXT, ItemPrice REAL, Category TEXT)")

cursor.execute("INSERT INTO ITEM VALUES('1', '2024-09-27', 'Pizza', 2.0, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('2', '2024-09-27', 'Bread', 0.50, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('3', '2024-09-28', 'Apple', 1.0, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('4', '2024-09-28', 'Banana', 0.5, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('5', '2024-09-28', 'Mango', 1.0, 'Food')")
cursor.execute("INSERT INTO ITEM VALUES('6', '2024-09-29', 'Pen', 1.0, 'Stationary')")
cursor.execute("INSERT INTO ITEM VALUES('7', '2024-09-29', 'Notebook', 2.0, 'Stationary')")
cursor.execute("INSERT INTO ITEM VALUES('8', '2024-09-30', 'Markers', 1.0, 'Stationary')")
cursor.execute("INSERT INTO ITEM VALUES('9', '2024-10-01', 'Chair', 2.0, 'Furniture')")
cursor.execute("INSERT INTO ITEM VALUES('10', '2024-10-01', 'Table', 3.0, 'Furniture')")
cursor.execute("INSERT INTO ITEM VALUES('11', '2024-10-02', 'Keyboard', 2.0, 'Electronics')")
cursor.execute("INSERT INTO ITEM VALUES('12', '2024-10-02', 'Mouse', 2.0, 'Electronics')")
cursor.execute("INSERT INTO ITEM VALUES('13', '2024-10-03', 'Calculator', 1.0, 'Electronics')")
cursor.execute("INSERT INTO ITEM VALUES('14', '2024-10-03', 'USB Memory', 1.0, 'Electronics')")

connection.commit()

row = cursor.execute("SELECT * FROM ITEM").fetchall()
print(row)

for row in cursor.execute("SELECT * FROM ITEM"):
    print(row)

connection.close()

