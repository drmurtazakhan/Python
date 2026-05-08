import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())

print(df.head(5))
print('-----------------------------')

# Replace Only For Specified Columns
# The fillna() method allows us to replace empty cells with a value:
# To only replace empty values for one column, specify the column name for the DataFrame:
# Replace NULL values in the "Calories" columns with the number 130
df["Calories"].fillna(130, inplace = True)

print(df.info())