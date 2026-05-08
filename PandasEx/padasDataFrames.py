import pandas as pd
import os

# Clearing the Screen
os.system('cls')

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# Create a DataFrame from two Series:

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45],
   "value": [70, 80, 98]
}

df = pd.DataFrame(data)

print(df)
print('------------------------')

#  access row 1
print(df.loc[1])
print('------------------------')

#  access row 1 of column 1
print(df.iat[1,1])

#  access row 1 of column 'duration'  (row 1 of column 1)
result = df.at[1, 'duration']
print("Output:",result)


print('------------------------')

#  access two rows: 0 and 1
print(df.loc[[0, 1]])