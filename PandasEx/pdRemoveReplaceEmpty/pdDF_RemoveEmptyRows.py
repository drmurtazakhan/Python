import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())

print(df.head(5))
print('-----------------------------')

# Remove rows that contain empty cells.
# dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()
print(new_df.info())
print('-----------------------------')

# If you want to change the original DataFrame, use the inplace = True argument:
df.dropna(inplace = True)
print(df.info())
print('-----------------------------')