# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:53:04 2024

@author: Dr. Murtaza Ali Khan
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3


## Connect to SQLite database 
connection = sqlite3.connect("TRADE_DB");

# Create a cursor object 
cursor = connection.cursor()

## Load CSV data into Pandas DataFrame 
df = pd.read_csv('TRADE.csv')
print(df)


## Write the data to a sqlite table 
df.to_sql('TRADE', connection, if_exists='replace', index=False) 


for row in cursor.execute('SELECT * FROM TRADE'): 
	print(row) 
    
# Close connection to SQLite database 
connection.close()                         

