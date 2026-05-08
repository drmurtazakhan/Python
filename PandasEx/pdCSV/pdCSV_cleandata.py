import pandas as pd
import re
import os

# Clearing the Screen
os.system('cls')

df = pd.read_csv('R:\PythonKhan\DataFiles\CSV\IWD_20Tweets.csv', encoding = "utf-8", skipinitialspace = True)

print(df)

print ("------------------------")
row, col = df.shape

print ("Number of rows: " + str(row))
print ("Number of cols: " + str(col))
print ("------------------------")
# apply the dtype attribute to find types of columns
dfType = df.dtypes
print("Types of dataframe columns:")
print(dfType)
print ("------------------------")

# remove non ASCII characters
df.text.replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)

# Remove URLs
df['text'] = df['text'].apply(lambda x: re.split('https:\/\/.*', str(x))[0])

# Define the regular expression pattern
pattern = r'[^\w\s]'

# Remove special characters from the 'text' column
df['text'] = df['text'].apply(lambda x: re.sub(pattern, '', x))



# concatenate all the values of a column as a single string
print("text column values as single object")
out = ' '.join(df["text"])

    

print (out)
