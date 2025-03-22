
import csv

# open an existing file for reading -
# csvfile = open('Salary_Data.csv', newline='')

csvfile = open('C:/0MAK/RW/PythonKhan/DataFiles/CSV/Salary_Data.csv', newline='')

# make a new variable - c - for Python's CSV reader object -
c = csv.reader(csvfile)

# read whatever you want from the reader object
# print it or use it any way you like
rows = []
for row in c:
    print( row[0] )

# save and close the file
csvfile.close()




