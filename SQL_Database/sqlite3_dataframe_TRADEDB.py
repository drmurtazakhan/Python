# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:53:04 2024

@author: Dr. Murtaza Ali Khan
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3


## The TRADE_DB is an existing databse in the current working directory
## The TRADE_DB has a table callsed TRADE 
## The TRADE table has following five fields (columns):
## ItemCode PurchaseDate ItemName ItemPrice Category

## create a connection to TRADE_DB 
connection = sqlite3.connect("TRADE_DB");

## In order to execute SQL statements and fetch results from SQL queries
## we will need to use a database cursor.
cursor = connection.cursor()

## select records the the TRADE table
df = pd.read_sql_query("SELECT * FROM TRADE", connection)
print(df)
print ("--------------------------------------------")
print(df.to_string(index=False))
print ("--------------------------------------------")

countRecords = len(df)
print ("Number of items = %d" % (countRecords))


sumPrice = df['ItemPrice'].sum()
print ("Sum of ItemPrice = %.2f" % (sumPrice))

avgPrice = df['ItemPrice'].mean()
print("Avg. of ItemPrice = %.2f" % (avgPrice))

minPrice = df['ItemPrice'].min()
print("Min. of ItemPrice = %.2f" % (minPrice))

maxPrice = df['ItemPrice'].max()
print("Max. of ItemPrice = %.2f" % (maxPrice))
print ("--------------------------------------------")

# Count Statistics of each Category
labelsCategoryCount = ['Food', 'Stationary', 'Furniture', 'Electronics']
valuesCategoryCount = df['Category'].value_counts(sort=False).values
dfCategoryCount = pd.DataFrame({"Category": labelsCategoryCount, "Count": valuesCategoryCount})
print(dfCategoryCount)
print ("--------------------------------------------")
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
sns.countplot(x=df['Category'], data=df)
plt.xlabel("Category")
plt.ylabel("Count of Items in each Category")
plt.subplot(1, 2, 2)
plt.pie(valuesCategoryCount, labels=labelsCategoryCount, autopct='%1.2f%%')
plt.title("% Count of items in each Category")

plt.show(block=False)


# Price Statistics of each Category
grouped = df.groupby('Category')

# Aggregate the data
itemPriceByCategory = grouped.agg({'ItemPrice': 'sum'})
print(itemPriceByCategory)
print ("--------------------------------------------")

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
ax = sns.barplot(x='Category', y='ItemPrice', data=itemPriceByCategory)
plt.xlabel("Category")
plt.ylabel("Sum of Item Price in each Category")

plt.subplot(1, 2, 2)
plt.pie(itemPriceByCategory['ItemPrice'], labels=itemPriceByCategory.index, autopct='%1.2f%%')
plt.title("% ItemPrice of each Category")
plt.show(block=False)

# Count and Price Statistics of each Category
countByCategory = df.groupby(['Category'])['Category'].count()
print(countByCategory)
print ("--------------------------------------------")
pricetByCategory = df.groupby(['Category'])['ItemPrice'].sum()
print(pricetByCategory)


df_Count_Price = pd.DataFrame({"Count":countByCategory,"Price":pricetByCategory})
ax = df_Count_Price.plot.bar(color=["SkyBlue","IndianRed"], rot=0, title="Count & Price of items in each Category")


#connection.close()