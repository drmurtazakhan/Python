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

sql = """SELECT Category, SUM(ItemPrice) AS SumItemPrice FROM ITEM GROUP BY Category;"""
 
itemPriceByCategory = pd.read_sql(sql, connection)
print(itemPriceByCategory)
print ("--------------------------------------------")

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
ax = sns.barplot(x='Category', y='SumItemPrice', data=itemPriceByCategory)
plt.xlabel("Category")
plt.ylabel("Sum of Item Price in each Category")

plt.subplot(1, 2, 2)
plt.pie(itemPriceByCategory['SumItemPrice'], labels=itemPriceByCategory.index, autopct='%1.2f%%')
plt.title("% ItemPrice of each Category")
plt.show(block=False)


connection.close()


## ResearchGate: http://www.researchgate.net/profile/Murtaza_Khan2/
## LinkedIn: https://www.linkedin.com/in/dr-murtaza-ali-khan-3b368019
## Google Scholar: https://scholar.google.com/citations?user=n0JDQ0sAAAAJ
## Scopus: https://www.scopus.com/authid/detail.uri?authorId=7410318323
## GitHub: https://github.com/drmurtazakhan
