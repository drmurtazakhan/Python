# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:53:04 2024

@author: Dr. Murtaza Ali Khan
"""

import sqlite3

connection = sqlite3.connect("PRODUCT");

cursor = connection.cursor()


## SQL query to get all the items in a variable
rowsAll = cursor.execute("SELECT * FROM ITEM").fetchall()
print(rowsAll)
print ("--------------------------------------------")


stationaryRows = cursor.execute("SELECT * FROM ITEM WHERE Category ='Stationary' ").fetchall()
print(stationaryRows)
print ("--------------------------------------------")



## SQL query to get all the items one by one
for row in cursor.execute("SELECT * FROM ITEM"):
    print(row)
print ("--------------------------------------------")

print ("Items of Stationary Category")
## SQL query to get all the items one by one where Category is Stationary 
for row in cursor.execute("SELECT * FROM ITEM WHERE Category ='Stationary'"):
    print(row)
print ("--------------------------------------------")

print ("Count of items in each Category")
rowsCategoryCount = cursor.execute("SELECT Category, COUNT(Category) AS CategoryCount FROM ITEM GROUP BY Category").fetchall()
print(rowsCategoryCount)
print ("--------------------------------------------")

print ("Sum of item price in each Category")
rowsCategoryPrice = cursor.execute("SELECT Category, SUM(ItemPrice) AS CategoryPrice FROM ITEM GROUP BY Category").fetchall()
print(rowsCategoryPrice)
print ("--------------------------------------------")



#connection.close()