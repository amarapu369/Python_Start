def febionacci_series(x):
    a = 0
    b = 1 
    if x == 1:
        print(a)
    elif x == 2 :
        print(a,b)
    else:
        print(a,b , end = " ")
        for i in range(x-2):
            c = a + b
            a = b
            b = c
            print(b , end = " ")

z = int(input("enter the number of the fibonacci seq you need:\n"))
febionacci_series(z)
       
        







# # practice
# for i in range(15):
#     print(i , end = " , ")