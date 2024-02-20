# while loop in python  
# while loop is used for the run the program in loop for a time or for number of repetations
# we can use the both while and for loop for same work
# example printing hello world 10 time 
i = 1
while i <= 10 :
    # print("my name is RAM ", i , "total was done")
    print(f"{i}.my name is RAM ")
    i = i + 1

# example 1
# sum of the 1 to 10 natural numbers 

total = 0 
i = 0 
while i <= 20 :
    # total = total +i 
    total += i 
    # print (i ,"total at this itteration" ,  total)
    i = i + 1 
print (total)
