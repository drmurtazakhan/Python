import numpy as np

# Create a 3-D array

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr)

#  count the number of elements
print('number of elements: ',  np.size(arr))
print('size of dim 1: ', np.size(arr, 0))
print('size of dim 2: ', np.size(arr, 1))
print('size of dim 3: ', np.size(arr, 2))

print('------------------------')
print('number of dimensions: ',  arr.ndim)

print('------------------------')
print(arr[0])
print('------------------------')
print(arr[1])
print('------------------------')
print(arr[0][1])
print('------------------------')
print(arr[0][1, 2])