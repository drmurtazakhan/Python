import pandas as pd

df = pd.read_csv('data3.csv')
print(df.info())


print(df.loc[0:5])


# Let's try to convert all cells in the 'Date' column into dates.
# Pandas has a to_datetime() method for this:

df['Date'] = pd.to_datetime(df['Date'])

print(df.loc[0:5])