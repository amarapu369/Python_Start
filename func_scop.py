#scop 
x = 6 
def func():
    global x
    x = 5 
    return x
def func2():
    return x
func()
print(x)
print(func2())