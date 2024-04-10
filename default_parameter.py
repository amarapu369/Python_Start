# def user_info(first_name , last_name, age):
#     print(f"my first name is {first_name}")
#     print(f"my last name is {last_name}")
#     print(f"my age name is {age}")

# user_info("RAMPRASAD", "AMARAPU", 27)

# when we mae the any parameter as the default 
# def user_info(first_name , last_name, age = 27):
#     print(f"my first name is {first_name}")
#     print(f"my last name is {last_name}")
#     print(f"my age name is {age}")

# user_info("RAMPRASAD", "AMARAPU")

#variable scope in function 
x = 7
def func():
    global x  
    x = 4 
    print(x)
def func2():
    print(x)

func2()