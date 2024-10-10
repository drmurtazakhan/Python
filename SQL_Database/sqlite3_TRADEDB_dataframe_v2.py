# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:53:04 2024

@author: Dr. Murtaza Ali Khan
"""

# Import data analysis libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Establish connection with database TRADE_DB
connection = sqlite3.connect("TRADE_DB");
cursor = connection.cursor()

# Read data from the 'ITEM' table in the database into a pandas dataframe.
df = pd.read_sql_query("SELECT * FROM ITEM", connection)

# print dataframe
print(df.to_string(index=False))
print ("--------------------------------------------")

# Calculate and print descriptive statistics for ItemPrice column.
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


# Grouping basedon Category column
grouped = df.groupby('Category')

# Aggregate the data in each category by count of ItemName
itemCountByCategory = grouped.agg({'ItemName': 'count'})
print(itemCountByCategory)
print ("--------------------------------------------")

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
ax = sns.barplot(x='Category', y='ItemName', data=itemCountByCategory)
plt.xlabel("Category")
plt.ylabel("Count of Items in each Category")

plt.subplot(1, 2, 2)
plt.pie(itemCountByCategory['ItemName'], labels=itemCountByCategory.index, autopct='%1.2f%%')
plt.title("% Count of Items in each Category")
plt.show(block=False)


connection.close()