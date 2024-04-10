import numpy as np 
 #truncatiom --it remove the decimal value and give the fraction value which is near zero 
arr = np.trunc([-33.2891, 33.45365])
print(arr)
# fix --- it is also sameas the truncation 
arr = np.fix([-33.2891, 33.45365])
print(arr)

# around ---it will give the

arr = np.around([-33.2891, 33.45365],2)
print(arr)
# floor -it will eliminate the 
arr = np.floor([-3.1666, 3.6667])
print(arr)

#The ceil() function rounds off decimal to nearest upper integer.

arr = np.ceil([-3.1666, 3.6667])
print(arr)