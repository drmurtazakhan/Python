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

arr = np.array([0.0, 2.1, 3.1])
print(arr)
print(arr.dtype)

newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)

print('------------------------')
