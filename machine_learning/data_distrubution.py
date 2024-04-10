import numpy
import matplotlib.pyplot as plt
# random data distrubution 
'''x = numpy.random.uniform(0.0, 5.0, 10000)
print(x)
plt.hist(x,100)
plt.show()
'''
# normal data distrubution 
'''y = numpy.random.normal(5.0 , 1.0 , 10000)
print(y)
plt.hist(y,100)
plt.show()
'''
# some of the example for the scattered plot 

'''x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
plt.scatter(x,y)
plt.show()'''
#  random data distrubution 
'''x = numpy.random.uniform(0.0, 5.0, 10000)
y = numpy.random.uniform(1.0,6.0, 10000)
plt.scatter(x,y)
plt.show()'''

# regression 
'''import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()'''

# linear regression 
'''
import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

# print(slope)
# print(r)
# print(p)
# print(intercept)
# print(std_err)
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))
# print(mymodel)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()'''

# bad fit for the linear reggression 

'''import matplotlib.pyplot as plt
from scipy import stats

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]


slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r)
def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()'''

######################ploynomial regression ####################
'''import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

plt.scatter(x, y)
plt.show()'''

#ploynominal regression 

'''import numpy
import matplotlib.pyplot as plt

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
# print(mymodel)
myline = numpy.linspace(1, 22, 100)
# print(myline)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()
'''
# ploynominal regression relation 
'''
import numpy
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))
'''
#########33bad fit for the polynominal regression ############3333
'''from sklearn.metrics import r2_score
import numpy
import matplotlib.pyplot as plt

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x)))

myline = numpy.linspace(2, 95, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()'''

############################## multiple regression ##############################

'''import pandas
from sklearn import linear_model

df = pandas.read_csv("data.csv")

x = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x, y)

print(f"regression coffecent is : {regr.coef_}")

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[2300, 1300]])
predictedCO2_1 = regr.predict([[3300, 1300]])
predictedCO2_2 = regr.predict([[2300, 2300]])

print(predictedCO2)
print(predictedCO2_1)
print(predictedCO2_2)'''
##################################scale ############################333

'''import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]

scaledX = scale.fit_transform(X)

print(scaledX)
'''
# co2 predection using the scaled values 

import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()

df = pandas.read_csv("data.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)

