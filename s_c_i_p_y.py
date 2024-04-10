from scipy import constants as cnt
import scipy
from scipy.optimize import root
from math import cos
from scipy.optimize import minimize

'''print(cnt.liter)
print(cnt.pi)
print(dir(cnt))
print(scipy.__version__)
print(cnt.yotta)    #1e+24
print(cnt.zetta)    #1e+21
print(cnt.exa)      #1e+18
print(cnt.peta)     #1000000000000000.0
print(cnt.tera)     #1000000000000.0
print(cnt.giga)     #1000000000.0
print(cnt.mega)     #1000000.0
print(cnt.kilo)     #1000.0
print(cnt.hecto)    #100.0
print(cnt.deka)     #10.0
print(cnt.deci)     #0.1
print(cnt.centi)    #0.01
print(cnt.milli)    #0.001
print(cnt.micro)    #1e-06
print(cnt.nano)     #1e-09
print(cnt.pico)     #1e-12
print(cnt.femto)    #1e-15
print(cnt.atto)     #1e-18
print(cnt.zepto)    #1e-21
print(cnt.kibi)    #1024
print(cnt.mebi)    #1048576
print(cnt.gibi)    #1073741824
print(cnt.tebi)    #1099511627776
print(cnt.pebi)    #1125899906842624
print(cnt.exbi)    #1152921504606846976
print(cnt.zebi)    #1180591620717411303424
print(cnt.yobi)    #1208925819614629174706176
print(cnt.gram)        #0.001
print(cnt.metric_ton)  #1000.0
print(cnt.grain)       #6.479891e-05
print(cnt.lb)          #0.45359236999999997
print(cnt.pound)       #0.45359236999999997
print(cnt.oz)          #0.028349523124999998
print(cnt.ounce)       #0.028349523124999998
print(cnt.stone)       #6.3502931799999995
print(cnt.long_ton)    #1016.0469088
print(cnt.short_ton)   #907.1847399999999
print(cnt.troy_ounce)  #0.031103476799999998
print(cnt.troy_pound)  #0.37324172159999996
print(cnt.carat)       #0.0002
print(cnt.atomic_mass) #1.66053904e-27
print(cnt.m_u)         #1.66053904e-27
print(cnt.u)           #1.66053904e-27
'''
'''def eqn(x):
  return x + cos(x)
# enq =  x + cos(x) we have to use function other wise we will get error x is not defined 
myroot = root(eqn, 0)

print(myroot.x)
print(myroot)'''



'''def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)
print(mymin.x)
'''
###############data sparing #################3
'''
'''
# print(csr_matrix(arr1))
# print(csr_matrix(arr))
# print(csr_matrix(arr).data)
# print(csr_matrix(arr).count_nonzero)
# print(csr_matrix(arr_new).eliminate_zeros)
# print(csr_matrix(arr_new).data)
# print(csr_matrix(arr_new).sum_duplicates)
# print(csr_matrix(arr_new).tocsc)

#######################scipy graphs################
'''import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

arr = np.array([[0, 1, 2],[1, 0, 0],[2, 0, 0]])
newarr = csr_matrix(arr)
print(connected_components(newarr))
print(dijkstra(newarr, return_predecessors=True, indices=0))
'''
##################spatial data##################
'''import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()
'''

###################### spatial data########################
'''import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

# plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()
'''
# ------------------polygone---------------------
'''import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

plt.show()'''

'''from scipy.spatial import KDTree
points = [(1, -1), (2, 3), (-2, 3), (2, -3)]
kdtree = KDTree(points)
res = kdtree.query((0, 1))

print(res)'''
# -------------------------------------------
'''from scipy.spatial.distance import euclidean
p1 = (1, 0)
p2 = (10, 2)
res = euclidean(p1, p2)
print(res)'''

# ---------------------------------------
'''from scipy.spatial.distance import cityblock

p1 = (1, 0)
p2 = (10, 2)
res = cityblock(p1, p2)
print(res)
'''
#---------------------------------------------------
'''from scipy.spatial.distance import cosine
p1 = (1, 0)
p2 = (10, 2)
res = cosine(p1, p2)
print(res)
'''
# ---------------------------
'''from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)
res = hamming(p1, p2)
print(res)
'''
# ---------------------------------matlab array---------------------
'''from scipy import io
import numpy as np

arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})
new_data = io.loadmat('arr.mat')
print(new_data)
'''
# --------------------------------------------------
'''from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])
# Export:
io.savemat('arr.mat', {"vec": arr})
# Import:
mydata = io.loadmat('arr.mat')
print(mydata)
mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec']) # here we can print the data from the matlab file '''
###########################insterploation________________________

'''from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
'''
#####-----------------------------------------------------
from scipy.interpolate import UnivariateSpline
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = UnivariateSpline(xs, ys)
newarr = interp_func(np.arange(2.1, 3, 0.1))
print(newarr)

#############3------------------------
from scipy.interpolate import Rbf
import numpy as np
721
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)