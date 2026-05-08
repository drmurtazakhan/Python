import numpy as np

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

#  count the number of elements
print('number of elements: ',  np.size(arr))
print('rows: ', np.size(arr,0))
print('columns: ', np.size(arr,1))
