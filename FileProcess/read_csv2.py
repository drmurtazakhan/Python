
import csv
import os
 
# Clearing the Screen
os.system('cls')

name = 'IWD2_small'
#name = 'Salary_Data'
ext = 'csv'
filename = name + '.' + ext

with open(filename, 'r') as file:
    lines = file.readlines()

    print(lines)

file.close()


print('------------------------')




