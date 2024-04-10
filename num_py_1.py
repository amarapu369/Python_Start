'''import num_py as np
p = np.array([1, 2, 3, 4, 5])
print(p)
print(type(p))
'''
'''import numpy as np
arr = np.array([4,2])
print(arr)'''

import numpy as np
'''
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)'''

'''a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
'''
'''
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)'''


'''arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

arr = np.array([1, 2, 3, 4])

print(arr)
print(arr.dtype)'''

'''arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)'''

'''arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)


arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)'''

'''arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)'''

'''arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)



arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)


arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)'''

'''arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

  
arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

  
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)'''
'''# stack along row
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)
# stack along column
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 7)

print(newarr)
'''

import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 7)

print(newarr)

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))


arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)