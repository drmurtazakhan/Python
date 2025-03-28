# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:53:04 2024

@author: Dr. Murtaza Ali Khan
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3


connection = sqlite3.connect("PRODUCT");

cursor = connection.cursor()


df = pd.read_sql_query("SELECT * FROM ITEM", connection)
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
