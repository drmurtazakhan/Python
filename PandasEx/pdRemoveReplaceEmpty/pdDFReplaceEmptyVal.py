import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())

print(df.head(5))
print('-----------------------------')

# The fillna() method allows us to replace empty cells with a value:
# Replace NULL values with the number 130:
df.fillna(130, inplace = True)

print(df.info())