# creat dataframe with string and number columns
import pandas as pd

# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])
  
# print dataframe.
print(df)
print ("------------------------")
# apply the dtype attribute to find types of columns
dfType = df.dtypes
print("Types of dataframe columns:")
print(dfType)
print ("------------------------")
