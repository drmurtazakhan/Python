import numpy as np
import csv
import pandas as pd

# read csv using csv package
rows = []
with open("Salary_Data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
file.close()

print(header)
print(rows)
print('------------------------')

# read csv using pandas package
# use to_string() to print the entire DataFrame.
# df = pd.read_csv('Salary_Data.csv')
# print(df.to_string())

# without to_string
df = pd.read_csv('Salary_Data.csv')
print(df)

# print(newarr)
# print(newarr.dtype)

# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
print('max rows:', pd.options.display.max_rows)


