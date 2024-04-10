price = 49
# txt = "The price is {} dollars"
txt = "The price is {:.2f} dollars"
# print(txt.format(price))
print(f"The price is {price} dollars")


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))