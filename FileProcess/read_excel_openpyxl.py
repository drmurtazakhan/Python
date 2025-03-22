import os
import openpyxl

# Clearing the Screen
os.system('cls')


# Provide the path to your Excel file
fileName = 'C:/0MAK/RW/PythonKhan/DataFiles/CSV/ID_Marks2.xlsx'

# Read the Excel file
theFile =  openpyxl.load_workbook(fileName)

 # prints all sheets by their names
print(theFile.sheetnames)

# Selects the sheet that is named “Sheet1” and saves it to a currentSheet variable.
currentSheet = theFile['Sheet1']


# prints the value that is located in the B4 position of the “Sheet1” sheet.
print(currentSheet['B4'].value)