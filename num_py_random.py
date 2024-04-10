from numpy import random

# # this is for random int value 
# x = random.randint(100)
# print(x)
# # this is for random float value 
# x = random.rand(100)
# print(x)
# # this is for random array 
# x=random.randint(100, size=(4,5))

# print(x)

# x = random.choice([3, 5, 7, 9], size=(3, 5))

# print(x)
'''

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.2, 0.4], size=(100))

print(x)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

random.shuffle(arr)

print(arr)
'''
#################------------------######################################
'''import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([-1,0, 1, 2, 3, 4, 5])
plt.show()

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()
'''
#################### normal distrubution ######################

'''
x = random.normal(size=(2, 3))
print(x)
x = random.normal(loc = 1,scale=2, size=(2, 3))

print(x)'''
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
'''
sns.distplot(random.normal(size=1000), hist=False)

plt.show()

print(random.normal(size=1000))
'''
#################### binominal  distrubution ######################
'''x = random.binomial(n=10, p=0.5, size=1000)
sns.distplot(x, hist=True, kde=False)

plt.show()
print(x)'''
####################  difference between the normal and binominal distrubution ######################


'''sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()'''
#################### poission distrubution ######################

'''x = random.poisson(lam=2, size=1000)
print(x)
sns.distplot(x,kde=False)
plt.show()'''
#################### normal & poission distrubution ######################

'''sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()'''
#################### binominal & poission distrubution ######################
'''sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()
'''
#######################################################################33

# sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

'''# plt.show()

# x = random.poisson(lam=50, size=1000)
# print(x)
sns.distplot(random.poisson(lam=50, size=1000),kde=False,label= 'poisson')
plt.show()'''

######################################uniform distrubution function #######################
'''x = random.uniform(size=(2, 3))
print(x)
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()'''
######################################logistic distrubution function #######################
'''x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
sns.distplot(random.logistic(size=1000), hist=False)
plt.show()'''
##############################-multi nominal distrubution #############
'''x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)'''
##############################-multi nominal distrubution #############
'''x = random.exponential(scale=2, size=(2, 3))

print(x)
sns.distplot(random.exponential(size=1000), hist=False)
plt.show()
'''
##############################-multi nominal distrubution #############
'''x = random.chisquare(df=2, size=(2, 3))
print(x)

sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()'''
##############################-Rayleigh distrubution #############
'''x = random.rayleigh(scale=2, size=(2, 3))
print(x)
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()'''

#############################pareto distrubution###########################################3

'''x = random.pareto(a=2, size=(2, 3))
print(x)

sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()
'''

##########################zipf distrubution##############################333
x = random.zipf(a=2, size=(2, 3))
print(x)


x = random.zipf(a=2, size=1000)
sns.distplot(x[x<222], kde=False)
plt.show()