# function for the last indexvalue
# def last_char(x):
#     return x[-1]

# y = input("enter your name")
# print(last_char(y))

# function for the odd or even 
# def odd_even(x):
#     if x%2 == 0:
#         return "even"
#         # print("your number is even! ")
#     else:
#         return "odd"
#         # print("your number is odd")

# print(odd_even(10))

# dry coding for the above code 
# def odd_even(x):
#     if x%2 == 0:
#         return "even"
#     return "odd"
# print(odd_even(9))
    
################ one more method###########
# def is_even(x):
#     if x%2 == 0:
#         return True
#     else:
#         return False
# print(is_even(9))

################ one more method###########
# def is_even(x):
#         return x%2 == 0
# print(is_even(10))

# ############# with argument ##########
# def song():
#      return "pwan kalyan is great actor"
# print(song())


####################EXERCISE############################
# def bigger(x,y):
#      if x > y :
#           return "x is bigger than the y"
#      else:
#           return "y is bigger than x"

# a = int(input("enter the firat number: \n"))
# b = int(input("enter the second number: \n"))
# print(bigger(a,b))

###############another  method ##########

def bigger(x,y):
     if x > y :
          return x
     else:
          return y

############## function for the three number gretest################

# def gretest(a,b,c):
#      if a > b and a > c :
#           return a
#      elif b > a and b >c :
#           return b
#      else:
#           return c

################# function inside function ####################

def gretest(a,b,c):
   k = bigger(a,b)
   return bigger(k,c)
x = input("enter the first number :")
y = input("enter the second number :")
z = input("enter the thired number :")
print(f"{gretest(x,y,z)}  is the biggest among the all numbers!")

######-KISS -Keep it simple stupid ########################
 