# learning for loop in this one 
# here we using the range funbction 
# code printing 10 times
'''
for i in range(10): #  if range 10 means 0 to 9
    print(f"{i}.my name is Ram prasad")


for i in range(1,12): #  if range 10 means 1 to 11
    print(f"{i}.my name is Ram prasad")

'''
# for loop example 1 :
    # sum of the first n natural number
'''
total = 0 
n = int(input("enter the number : "))
for i in range(n):
    total += i 
print (total) 

total = 0 
n = input("enter the number : ")
for i in range(int(n)):
    total += i 
print (total) 
'''

# example 2 for loop 
# user input need to be sum of all digits 
'''
total = 0 
n = input("enter the number : ")
for i in range (len(n)):
    total += int(n[i])

print(total)

'''
# example 3 : charcter repated in  entered string 
'''
name = input("enter your name : ")
temp = ""

for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]
'''

# BEARK AND CONTINUE KEYWORD
''''
for i in range(10):
    if i == 9:
        break                # break keyword
    print(f"{i}:my name is Ram")

# continue keyword
    for i in range(11):
        if i == 3:
            continue              # contoine keyword
        print(f"{i}:my name is Ram")
        '''

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# for x in range(2,20,2):
#     print(x)
# #  print 10 9 8 7 6 5 4 3


# for x in range(10,-1,-1):
#     print(x)
# for loop with string
# name = "Ramprasad"
# for x in range(len(name)):
#     print(name[x])

# name = "Ramprasad"
# for x in name:
#     print(x)

n = input("enter the number : ")
total = 0
for x in n :
    total += int(x)
print(total)