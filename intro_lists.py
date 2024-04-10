# list is the data structre we can store the any data type 

'''numbers = [1 , 2,3,4,5,6,]
print(numbers)

words = ['ram' , 'prasad', 'amarapu' , 'mahesh' , 'ramya' , 'gayatri']
print(words)

mixlist = [1,2,3.4,6,7.56,'ram' , 'prasad', 'amarapu' , None]
print(mixlist)

print(mixlist[6])'''

# adding data to list 

'''mixlist = [1,2,3.4,6,7.56,'ram' , 'prasad', 'amarapu' , None]
words = ['ram' , 'prasad', 'amarapu' , 'mahesh' , 'ramya' , 'gayatri']

mixlist.append('hero') # adding lists
mixlist.append('B_wood') # adding lists
mixlist.append('T_wood') # adding lists
mixlist.insert(1,'H_wood')
lists = mixlist + words
print(lists)
mixlist.extend(words)
mixlist.append(words)

print(mixlist)
'''

# deleteing the data from thge lists

'''# pop method 
lists.pop()
print(lists)

# delete operator 
del lists[3]
print(lists)

# remove method 
lists.remove(2)
print(lists)'''


# in keyword in the lists 
'''fruits = ['orange', 'mango' , 'apppple', 'graps', 'kiwi', 'pear', 'banana']

if 'mango' in fruits :
    print("fruit is present")
else:
    print("fruit is not present")
# count sort reverse clear copy methods 
fruits = ['orange', 'mango' , 'apppple', 'graps', 'kiwi', 'pear', 'banana']
numbers = [1,3,2,7,4,6,3,7,9]
print(fruits.count('orange'))  #count function 
'''
# fruits.sort()  #sort function 
# numbers.sort()

'''print(sorted(numbers)) # sorted function 
print(numbers) 
print(fruits)'''

# numbers.clear()  #clear method 
# print(numbers)

# new_numbers = numbers.copy()
# print(new_numbers)

#####################- is vs == --- #####################
# it is used for the compare the any things
'''fruits1 = ['orange', 'mango' , 'apppple', 'graps']
fruits2 = ['graps', 'kiwi', 'pear', 'banana']
fruits3 = ['orange', 'mango' , 'apppple', 'graps', 'kiwi', 'pear', 'banana']
print(fruits1 ==  fruits2)
print(fruits1 ==  fruits3)
print(fruits2 ==  fruits3) # == is used for the check the both the liust having the same objects or not 
print(fruits2 is fruits3) # is used for the both lists ae in the same memory or not 
print(fruits2 is fruits3)
'''
##################split and join method ######################
'''user_data = "ram prasad amarapu 24 ".split()
print(user_data)
user_data = "ram,prasad,amarapu,24 ".split(",")
print(user_data)

first_name,second_name,third_name,age = "ram prasad amarapu 24 ".split()
print(first_name)
print(second_name)
print(third_name)
print(age)
print(user_data)
user_data = "ram prasad amarapu 24 ".split()
print(user_data)
#######join -method###########
user_data = ['ram' 'prasad' 'amarapu' '24']
print(",".join(user_data))'''

####################list vs arry ##########################
# in python we have the array module 
# in array we can store the same data like int or string ot float
# in list we can store the any datat type 
#javascript = python list
##############lists in looping ###################

fruits = ['orange', 'mango' , 'apppple', 'graps', 'kiwi', 'pear', 'banana']

for fruit in fruits:
    print(fruit)

i = 0 

while i < len(fruits):
     print(fruits[i])
     i += 1

a = "RamPrasadAmarapu"
x = 0
y = 0
# print(a[1])
print(len(a))
for i in a :
    if (i.islower()):
     x += 1
    else:
     y += 1
    
print(f'total numer of lower cases are {x}' )
print(f'total numer of capital cases are {y}' )
      

string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)