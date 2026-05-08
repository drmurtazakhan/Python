import numpy as np

# i - integer
# b - boolean
# u - unsigned
# integer
# f - float
# c - complex
# float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode
# string
# V - fixed
# chunk
# of
# memory
# for other type(void)

arr = np.array([2, 4, 6, 8, 10, 12])
print(arr)
print(arr.dtype)
print('------------------------')
arr = np.array(['apple', 'banana', 'cherry'])
print(arr)
print(arr.dtype)
print('------------------------')
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
print('------------------------')
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)