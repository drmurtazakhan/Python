import numpy as np
print(np.__version__)
print('-------------------')
# create a NumPy ndarray object by using the array() function.
arr1 = np.array([1, 3, 5, 7, 9])

print(arr1)
print(type(arr1))
print('-------------------')

# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray
my_list = [2, 4, 6, 8, 10]
print(my_list)
print(type(my_list))
print('-------------------')
arr2 = np.array(my_list)
print(arr2)
print(type(arr2))
print('-------------------')
