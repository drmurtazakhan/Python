import pandas as pd
import os

# Clearing the Screen
os.system('cls')

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# Create a DataFrame from two Series:

data = {
  "Item": ["Water Bottle", "Tissue Box", "Light Bulb"],  
   "Code": ["WB253", "TB563", "LB789"],  
   "Price": [100, 200, 300]
}

df = pd.DataFrame(data)

print(df)
print('------------------------')


#  access row 1 , column 2
result = df.iat[1,2]
print("result:",result)

# modify result
result = result + 50;

# update result in df
df.iat[1,2] = result

#  access row 1 , column 2
result =df.iat[1,2]
print("result:",result)

print('------------------------')
print(df)