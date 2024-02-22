# # mylist = "apple", "banana", "cherry"
# # print(type(mylist))

# # thislist = ["apple", "banana", "cherry"]
# # print(len(thislist))
# # thislist = ["apple", "banana", "cherry"]
# # print(thislist[-1])

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)
# # thislist = ("apple", "banana", "cherry")
# # thislist[1] = "blackcurrant"
# # print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon" "ram" ,"dsf"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(3, "RAmprasad")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# tropical.extend(thislist)
# print(thislist)
# changing the item with refered value
# thislist = ["apple", "banana", "cherry"]
# thislist[0] = "blackcurrant"
# print(thislist)
'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
'''
'''

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
'''

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# # thislist.remove("banana")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist.pop(0)
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# del thislist[1]
# print(thislist)

'''
thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
'''


# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)


# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist]
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "m" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
'''

# ****************** Important *********************

# newlist = [expression for item in iterable if condition == True]

# newlist = [x for x in fruits if x != "apple"]

# newlist = [x if x != "banana" else "orange" for x in fruits]

# newlist = ['hello' for x in fruits]


# thislist = ["Apple", "orange", "mango", "kiwi", "Pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23, 0]
# thislist.sort()
# print(thislist)

# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "orange", "Kiwi", "Cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)


######################### tuple #####################################
# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# thistuple = ("apple",)
# print(type(thistuple))

# #NOT a tuple
# thistuple = ("apple")
# print(type(thistuple))


# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)


# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# (green, yellow, *red) = fruits

# print(green)
# print(yellow)
# print(red)

# thisset = {"apple", "banana", "cherry", "apple"}

# print(thisset)



# thisset = {"apple", "banana", "cherry", False, True, 0}

# print(thisset)

############### dictionary######################3
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["model"])

'''


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("year")
print(x)
x = thisdict.keys()
print(x)
'''

'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "whie"
car["cost"] = 2100000
print(car["cost"])
print(x) #after the change
z = car.keys()
x = car.values()
y = car.items()
print(x)
print(y)
print(z)


'''
'''
###################3nested dict###################3\
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
'''



# -------------------------------------------------------
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child1"]["name"])