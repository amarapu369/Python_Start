"""import numpy as np
# for log base 2 

arr = np.arange(1, 10)
print(np.log2(9))

# for log base 10

arr = np.arange(1, 10)
print(np.log10(9))
# for log base e

arr = np.arange(1, 10)
print(np.log(arr))
"""


##########summation########################33
'''import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

# newarr = np.add(arr1, arr2)
newarr = np.sum([arr1, arr2])
print(newarr)
'''

'''import numpy as np
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)'''

'''import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)'''
'''
import numpy as np

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)
'''
'''
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)


import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)

import numpy as np

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)'''

#####################Difference#############3

'''import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)

import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)

'''
'''import numpy as np

num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)

import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)

import numpy as np

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)
'''
#####################GCD############333
'''import numpy as np

num1 = 6
num2 = 9

x = np.gcd(num1, num2)

print(x)
'''
'''
import numpy as np

x = np.sin(np.pi/2)

print(x)

import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)

import numpy as np

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)

import numpy as np

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)


import numpy as np

base = 3
perp = 4
x = np.hypot(base, perp)
print(x)

import numpy as np
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
'''
import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)