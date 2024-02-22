# Question average of the three numbers and print in the form of  the string formating 
# types of input 
# a , b, c  = input("enter the first number\n" ).split()
a , b, c = 1,2,3
# a = int(input("enter the first number\n"))
# b = int(input("enter the second number\n" ))
# c = int(input ("enter the thired number\n"))
# print(int(a), int(b) , int(c))
# print(int(b))
# print(int(c))
print(a, b , c) 
# print(c)
# print((a+b+c)/3)
# d = ((a+b+c)/3)
# print(f"average of the three values is : {d}")
# print("average of the three values is  {}".format(d))
print((int(a)+int(b)+int(c))/3)


# Exercise2_2
# name = input("please enter the name:\n")
# print(name[::-1])
# Exercise 2_3
# name , chr = input("enter your name :\n").split(",")
# name.upper()
# chr.upper()
# print(f"your name length is {len(name)}")
# print(f"number of times your cha is repeated :{name.lower().count(chr.lower())}")


# we can slove the spaces issue in input by using the replace 
# name , chr = input("enter your name :\n").split(",")
# print(f"your name length is {len(name)}")
# print(f"number of times your cha is repeated :{name.strip().lower().count(chr.strip().lower())}")
