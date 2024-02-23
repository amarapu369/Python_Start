# lambda was the anonymous function 
# it can take any number of inputs in single expression
#  lambda arguments : expression

# example
# x = lambda a : a + 10
# print(x(100))

# x = lambda a,b : a + b
# print(x(2,4))


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


class MyClass:
  x = 5