import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)
print('------------------------')

# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.
# Create a simple Pandas Series from a list:
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Return the first value of the Series:
print('first value of the Series: ' , myvar[0])