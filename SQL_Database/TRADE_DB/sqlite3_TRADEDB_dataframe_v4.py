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
print(df)
print ("--------------------------------------------")

# print dataframe without index
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
itemCountByCategory = grouped.agg({    
    'ItemCode': 'first',
    'PurchaseDate': 'first',
    'ItemName': 'count',
    'ItemPrice': 'first',
    'Category': 'first'
    })
print(itemCountByCategory)
print ("--------------------------------------------")


# Create a figure and a set of subplots.
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
ax = sns.barplot(x='Category', y='ItemName', data=itemCountByCategory)
plt.xlabel("Category")
plt.ylabel("Count of Items in each Category")

# Create a pie chart in the second subplot
plt.subplot(1, 2, 2)
plt.pie(itemCountByCategory['ItemName'], labels=itemCountByCategory.index, autopct='%1.2f%%')
plt.title("% Count of Items in each Category")
plt.show(block=False)

# Aggregate the data in each category by sum of ItemPrice
itemPriceByCategory = grouped.agg({
    'ItemCode': 'first',
    'PurchaseDate': 'first',
    'ItemName': 'first',
    'ItemPrice': 'sum',
    'Category': 'first'
    })
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

connection.close()


## ResearchGate: http://www.researchgate.net/profile/Murtaza_Khan2/
## LinkedIn: https://www.linkedin.com/in/dr-murtaza-ali-khan-3b368019
## Google Scholar: https://scholar.google.com/citations?user=n0JDQ0sAAAAJ
## Scopus: https://www.scopus.com/authid/detail.uri?authorId=7410318323
## GitHub: https://github.com/drmurtazakhan
