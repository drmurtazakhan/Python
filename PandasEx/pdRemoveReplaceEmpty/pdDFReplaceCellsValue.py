import pandas as pd

df = pd.read_csv('data3.csv')
print(df.info())

print(df.loc[0:9])

# In row 1 "Pulse" value 1117 seems incorrect.
# Set "Pulse" = 117
# df.loc[1, 'Pulse'] = 117
# print(df.loc[0:5])

# Loop through all values in the "Pulse" column.
# If the value is higher than 120, set it to 120:
for x in df.index:
  if df.loc[x, "Pulse"] > 120:
    df.loc[x, "Pulse"] = 120

print(df.loc[0:9])