# import matplotlib as mpl

# print(mpl.__version__)

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250,])

# plt.plot(xpoints, ypoints)
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
'''
xpoints = np.array([1, 12, 5, 7])
ypoints = np.array([3, 10, 11, 15])
font1 = {'family':'serif','color':'blue','size':20, }
font2 = {'family':'serif','color':'green','size':15}
# plt.title("random_numbers_plot", fontdict = font1,  loc = 'center')
plt.title("random_numbers_plot")
plt.xlabel("random1")
# plt.xlabel("random1", fontdict = font2,)
plt.ylabel("random0")
# plt.ylabel("random0", fontdict = font2)
plt.plot(xpoints, ypoints, 'o:g')
# plt.plot(xpoints, ypoints, marker = '*')
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.plot(xpoints, ypoints, '*:k')
plt.grid()
plt.show()
plt.close()

'''
'''
#sub plot 
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 1)
plt.plot(x,y)
# plt.grid()
plt.scatter(x,y)
#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 2)
# plt.plot(x,y)
# plt.grid()
plt.scatter(x,y)
#plot 3
xpoints = np.array([1, 12, 5, 7])
ypoints = np.array([3, 10, 11, 15])
plt.subplot(2,2,3)
# plt.plot(xpoints,ypoints)
plt.title("four plots1",loc = "left", color = "green")
# plt.grid()
plt.scatter(xpoints,ypoints)
# plot 4
xpoints = np.array([1, 12, 5, 7, 8 , 10])
ypoints = np.array([3, 10, 11, 15, 20, 50])
plt.subplot(2,2,4)
# plt.plot(xpoints,ypoints, "o")
plt.scatter(xpoints,ypoints)


plt.title("four plots",loc = "center", color = "green", y = -0.3)
plt.suptitle("subplots")
# plt.grid()
plt.show()'''


############______________-----------------------_________________
'''import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()
'''
'''
#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
plt.scatter(x, y, c = colors, cmap = 'rainbow_r')

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)


plt.show()'''

'''x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes, alpha = 0.2)

plt.show()'''


'''x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, s=sizes, alpha=0.9, cmap='nipy_spectral')

plt.colorbar()

plt.show()'''

'''x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "hotpink",  width= 0.1)
plt.show()'''

'''x = np.random.normal(160, 30, 100)

print(x)
'''
'''
y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.title("pie chart")
plt.show() '''

'''
y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
plt.title("pie chart")
plt.pie(y, labels = mylabels)
plt.show() 
import matplotlib.pyplot as plt

import numpy as np
'''
'''y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode,startangle = 90 , shadow = True)
plt.legend()
plt.show() '''

