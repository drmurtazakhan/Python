
import csv
import os
import numpy as np

# Clearing the Screen
os.system('cls')

name = 'Salary_Data'
ext = 'csv'
filename = name + '.' + ext

arr = np.loadtxt(filename, delimiter=",", dtype=str)

print ("Contents of array: ")
print(arr)

print('------------------------')
print ("The length of array is: " + str(len(arr)))


# The strip() method removes both leading and trailing whitespace

