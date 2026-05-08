import pandas as pd
import os

# Clearing the Screen
os.system('cls')

# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# Create a DataFrame from two Series:

data = {
  "Item": ["   Water Bottle ", " Tissue  Box", "   Light Bulb     "],     
   "Price": [100, 200, 300]
}

df = pd.DataFrame(data)

print(df)
print('------------------------')

# Remove spaces from column values
df['Item'] = df['Item'].apply(lambda x: x.strip())


print(df)
