import os
import pandas as pd

# Clearing the Screen
os.system('cls')


# Provide the path to your Excel file
datafile = 'C:/0MAK/RW/PythonKhan/DataFiles/CSV/ID_Marks.xlsx'

# Read the Excel file
df = pd.read_excel(datafile)

# Display the contents of the Excel file
print(df)


 # list of column headers using the columns property of the dataframe object.
print(df.columns.ravel())




 



