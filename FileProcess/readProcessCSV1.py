import numpy as np
import csv
import pandas as pd

import os
 
# Clearing the Screen
os.system('cls')

#name = 'Salary_Data'
name = 'IWD2_small'

ext = 'csv'
filename = name + '.' + ext

arr = []
with open(filename, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    

    for row in csvreader:
        arr.append(row)


file.close()

print ("The header of array: ")
print(header)
print('------------------------')

print ("Contents of array: ")
print(arr)
print('------------------------')

print ("First record of array: ")
print(arr[0])
print ("Last record of array: ")
print(arr[len(arr)-1])
print('------------------------')

print ("The length of array is: " + str(len(arr)))


