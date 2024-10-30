# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:23:25 2024

@author: Khan M
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('MonthlyRegionalSales201920.csv')

print(df)
print ("--------------------------------------------")
df = df[df['Year'] == 2019]

print(df)
print ("--------------------------------------------")

df = df.drop('Year', axis=1)

print(df)
print ("--------------------------------------------")

ax = df.plot.bar(rot=0)
ax.set_xticklabels(df.Month)
plt.xlabel('Month')
plt.show()



