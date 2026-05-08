import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())

print(df.head(5))
print('-----------------------------')

# Replace Using Mean, Median, or Mode
# Calculate the MEAN, and replace any empty values with it:

# Mean = the average value (the sum of all values divided by number of values).
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)

# Median = the value in the middle, after you have sorted all values ascending.
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)

# Mode = the value that appears most frequently.
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)