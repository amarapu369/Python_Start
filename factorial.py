# find ing the n number factorial 
k = int(input("enter the number of the factorials you want : \n "))
def fact(n):
    return 1 if (n == 0 or n== 1 ) else n * fact(n-1)
i = 0
while i <= k :
    print(f"factorial of {i} = " ,fact(i))
    i += 1