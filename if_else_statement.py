#syntex of IF 
# if confition :
# age = int(input("enter your name: \n "))
# if age >= 14:
#     print("your valid use")
# else:
#     print("you are not a valid user")
######## if elif else statrement using ##############
# it is used multipule conditions checkimg 
# question :
# 1 to 3 -free
# 4 to 10 -150
# 11 to 60  -250
# above 60 - 200
age = int(input("enter your age :\n"))
if age == 0 :
    print("you can't watch")
elif 0<age<3 :
    print("ticket price: FREE")
elif 3<age<=10 :
    print("ticket price : 150")
elif 10<age<=60 :
    print("ticket price : 250") 
else:
    print("ticket price : 200")  