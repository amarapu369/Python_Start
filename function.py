# function is block of the code which will exicute when it's called
# '''
# def my_function():
#     print("my name is ram:")
# my_function()
# '''
# def my_function(fname):
#   print(fname + " Refsnes")
# '''
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")
# '''
# '''

# def my_function(fname, lname):
#   print(fname + "!@#$%^&*" + lname)

# my_function("Emil", "Refsnes")

# '''

# '''
# def my_function(*kids):
#   print("The youngest child is " + kids[0])

# my_function("Emil", "Tobias", "Linus")
# '''
# '''
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child2)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# '''

# '''
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# '''
# '''
# def my_function(s):
#   for x in s :
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits) '''

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def my_function(x, /):
#   print(x)

# my_function(3)

# def my_function(*, x):
#   print(x)

# my_function(x = 3)


# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)


# def tri_recursion(k):
#   if(k > 2):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#     print(result)
#   return result

# print("Recursion Example Results")
# tri_recursion(3)

######################function topic with Harsit vasist #############################

# function 
# n = "Ramprasad"
# print(len(n))
# here len is function whic is designed by python itsels
# def add_two(a,b) :
#   return a+b
# total = add_two(5,2)
# print(add_two(6,7))
# print(total)

############### print vs return##################

# def add_three(a,b,c):
#   return a+b+c
# k = add_three(5,3,6)
# print(add_three(5,8,6))

# def add_three(a,b,c):
#   print(a+b+c)
# add_three(5,3,6)

# but better to use the return is best in functions


