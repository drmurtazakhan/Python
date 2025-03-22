import csv


#name = 'IWD2_small'
#name = 'Salary_Data'

name = 'diabetes_prediction_dataset'

ext = 'csv'
filename = name + '.' + ext

myFile = open(filename)

print("The content of CSV file is:")

text = myFile.readline()
while text != "":
    text = text.strip()
    print(text)
    text = myFile.readline()
myFile.close()



print('------------------------')


# The strip() method removes both leading and trailing whitespace

