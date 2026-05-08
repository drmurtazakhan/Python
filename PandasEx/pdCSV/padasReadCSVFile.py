import pandas as pd

df = pd.read_csv('R:\PythonKhan\DataFiles\CSV\IWD_20Tweets.csv', encoding = "utf-8")

# df = pd.read_csv('R:\PythonKhan\DataFiles\CSV\data.csv')

print(df)

print ("------------------------")
row, col = df.shape

print ("Number of rows: " + str(row))
print ("Number of cols: " + str(col))

# use to_string() to print the entire DataFrame.
# print(df.to_string())

# Check your system's maximum rows with the
print(pd.options.display.max_rows)
# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.
