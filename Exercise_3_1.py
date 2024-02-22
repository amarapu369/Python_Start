# Excercise on the nested Iif else loop 


# import random
# number = int(random.random())
# print(number)
# relnum = 5
# num = int(input("enter your gussing number: \n"))
# if relnum == num:
#     print("you won")
# else:
#     if relnum < num :
#         print("your number is greater than the actual number")
#     else:
#         print("your number is less than the actuall number")


# exercise 2
# watch coco movie with condition name start with a or A and age above 10 
'''        
name = "amarapu"
age  = 10
# print(name[0].lower())
if (name[0] == "a" or name[0] == "A") and age >= 10 :
# if name[0].lower() == "a" and age > 10 :
    print("you can watch coco movie")
else:
    print("sorry, you cannot watch coco")
'''

# while loop exercise 
# n natural number sum 1 to n using the while loop 
'''
total = 0
i = 1
n = int(input("enter the number : "))
# print(type(n))
while i <= n :
    total += i 
    i += 1 
    # print(total)
print (total)
'''

# example 2: sum of the digits in multi digits number 
'''
n = input("enter multi digit number: \n")
total = 0
i = 0
l = len(n)
# print(l)
# print(type(l))
while i < l:
    total += int(n[i])
    i += 1
    # print(total)
print(total)  
'''
# example 3 find the string repeating number 

i = 0 
name = input("enter your name : ")
l = len(name)
temp_var = ""
while i < l :
    if name[i] not in temp_var:
        temp_var += name[i]
    # print(name[i] , ":" , name.count(name[i]))
        print(f"letter {name[i]} is repeted in yor name is  :  {name.count(name[i])} times")
    i += 1
