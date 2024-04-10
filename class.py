# class Person:
#     def __init__(self, name, age, section ):
#         self.name = name
#         self.age = age
#         self.section = section
# p1 = Person("John", 36 , "A")

# print(p1.name)
# print(p1.age)
# print(p1.section)


# class Person:
#   def __init__(self, name, age,):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

# p1 = Person("John", 36)

# print(p1)

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my age is",abc.age )

# p1 = Person("John", 36)
# p1.myfunc()

# class Student(Person):
#    def __init__(self, fname, lname):
#      self.fname = fname
#      self.lname = lname
#    def printname(self):
#        print("your full name is " , self.lname,self.fname)
# x = Student("Mike", "Olsen")
# x.printname()

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)