import pandas as pd

a = [1, 7, 2]

# Create your own labels:
myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
print('------------------------')

# Return the value of "y":
print(myvar["y"])