import numpy as np

arr = np.array([2, 4, 6, 8, 10, 12])

print(arr[1:4])

# Slice elements from the beginning to index 4 (not included):
print(arr[:4])

# Slice from the index 3 from the end to index 1 from the end:
print(arr[-3:-1])

# Return every other element from index 1 to index 5 (not included):
print(arr[1:5:2])

# Return every other element from the entire array:
print(arr[::2])

#  count the number of elements
#  print('number of elements: ',  np.size(arr))
