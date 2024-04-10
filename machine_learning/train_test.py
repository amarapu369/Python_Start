import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

'''x = numpy.random.normal(3, 1, 100)
# print(f'x set is the :{x}')
y = numpy.random.normal(150, 40, 100) / x
# print(f'y set is the :{y}')
train_x = x[:80]
# print(train_x)
train_y = y[:80]
plt.title('Train Function')
plt.scatter(train_x, train_y)
plt.show()

test_x = x[80:]
test_y = y[80:]
plt.title('Test Function')
plt.scatter(test_x, test_y)
plt.show()

plt.title('Overal Function')
plt.scatter(x, y)
plt.show()

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()'''

######above example is getting estimated with the linear regression ######################

import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))
r3 = r2_score(test_y, mymodel(test_x))
print(r3)
print(r2)