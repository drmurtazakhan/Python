# import libraries
from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd

# Creating dataset 
item =[ 'Detergent', 'Paper Towels', 'Honey', 'Toilet Paper',
'Kitchen Trash Bags', 'Brownie Mix', 'Toothpaste',
'Fish', 'Chicken drums', 'Chair', 'Walnut', 'Headphone']

 
price = [17, 5.5, 32, 2.5, 10, 7.5, 22, 40, 15, 35, 28, 18]

df = pd.DataFrame({"Item": item, "Price": price})

print(df);
print ("--------------------------------------------")

## defining bin edges
## Each bin includes the left edge, but does not include the right edge,
## except for the last bin which includes both edges.

binEdges =  [0, 10, 20, 30, 40];

# Creating histogram

hist, bins = np.histogram(price, bins = binEdges)

# printing histogram
print()
print('Bin edges = ',bins)
print('Hist (count of items in each edge) = ',hist)


# Creating plot
fig = plt.figure(figsize =(10, 7))

plt.hist(price, bins = binEdges) 

plt.title("Numpy Histogram") 
 
# show plot
plt.show()