import numpy
from scipy import stats
# mean of the array 
'''speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
y = numpy.median(speed)
z = stats.mode(speed)
print(x)
print(y)
print(z)
'''

# standered deviation  of the array example 
import numpy

'''speed = [86,87,88,86,87,85,86,2]
speed1 = [32,111,138,28,59,77,97]
x_v  = numpy.var(speed)
x = numpy.std(speed)
z_v =numpy.var(speed1)
z = numpy.std(speed1)
y = numpy.mean(speed)
print(x_v)
print(x)
print(z_v)
print(z)
print(y)'''

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

a = numpy.percentile(ages, 90)

print(a)