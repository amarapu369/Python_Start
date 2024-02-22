'''first_name = 'Ram'
second_name = 'Prasads'
full_name = first_name+ " " +second_name
print(full_name)
# print(full_name + 3)
print(full_name + str(3))
print(full_name * 3)'''

# string formatting 
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# age = "36"
# txt = "My name is John, I am " + age
# print(txt)

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

a = "RamPrasad Amarapu"
# print('my name is ' + a)

# a = "RamPrasad Am\tarapu"
a = "RamPrasad Amarapu"
# print('my name is ' + a.lower())
# print('my name is ' + a.upper())
# print('my name is ' + a.lower())

# print('my name is ' + a.capitalize()) # capitalize()	Converts the first character to upper case
# print('my name is ' + a.casefold()) # casefold()Converts string into lower case
# print('my name is ' + a.center(40,'@') + " my age i don't know") # center() Returns a centered string
# print( a.count('r')) # count()	Returns the number of times a specified value occurs in a string
# k = print(a.encode('utf-8')) # encode(UTF-8)	Returns an encoded version of the string
# print(k)
'''
print('my name is ' + str(a.endswith("u"))) # endswith()	Returns true if the string ends with the specified value
print('my name is ' + a.expandtabs(10)) # expandtabs()	Sets the tab size of the string
print('my name is ' + str(a[::-1].find("r", 3))) # find() Searches the string for a specified value and returns the position of where it was found
print(a[-1])
print(len(a))
print(a[::-1])
'''
print('my name is ' + a.format(4)) # format()	Formats specified values in a string
# print('my name is ' + a.lower()) # format_map()	Formats specified values in a string
# print('my name is ' + a.lower()) # index()	Searches the string for a specified value and returns the position of where it was found
# print('my name is ' + a.lower()) # isalnum()	Returns True if all characters in the string are alphanumeric
# print('my name is ' + a.lower()) # isalpha()	Returns True if all characters in the string are in the alphabet
# print('my name is ' + a.lower()) # isascii()	Returns True if all characters in the string are ascii characters
# print('my name is ' + a.lower()) # isdecimal()	Returns True if all characters in the string are decimals
# print('my name is ' + a.lower()) # isdigit()	Returns True if all characters in the string are digits
# print('my name is ' + a.lower()) # isidentifier()	Returns True if the string is an identifier
# print('my name is ' + a.lower()) # islower()	Returns True if all characters in the string are lower case
# print('my name is ' + a.lower()) # isnumeric()	Returns True if all characters in the string are numeric
# print('my name is ' + a.lower()) # isprintable()	Returns True if all characters in the string are printable
# print('my name is ' + a.lower()) # isspace()	Returns True if all characters in the string are whitespaces
# print('my name is ' + a.lower()) # istitle()	Returns True if the string follows the rules of a title
# print('my name is ' + a.lower()) # isupper()	Returns True if all characters in the string are upper case
# print('my name is ' + a.lower()) # join()	Joins the elements of an iterable to the end of the string
# print('my name is ' + a.lower()) # ljust()	Returns a left justified version of the string
# print('my name is ' + a.lower()) # lstrip()	Returns a left trim version of the string
# print('my name is ' + a.lower()) # lower()	Converts a string into lower case
# print('my name is ' + a.lower()) # maketrans()	Returns a translation table to be used in translations
# print('my name is ' + a.lower()) # partition()	Returns a tuple where the string is parted into three parts
# print('my name is ' + a.lower()) # replace()	Returns a string where a specified value is replaced with a specified value
# print('my name is ' + a.lower()) # rfind()	Searches the string for a specified value and returns the last position of where it was found
# print('my name is ' + a.lower()) # rindex()	Searches the string for a specified value and returns the last position of where it was found
# print('my name is ' + a.lower()) # rjust()	Returns a right justified version of the string
# print('my name is ' + a.lower()) # rpartition()	Returns a tuple where the string is parted into three parts
# print('my name is ' + a.lower()) # rsplit()	Splits the string at the specified separator, and returns a list
# print('my name is ' + a.lower()) # rstrip()	Returns a right trim version of the string
# print('my name is ' + a.lower()) # split()	Splits the string at the specified separator, and returns a list
# print('my name is ' + a.lower()) # splitlines()	Splits the string at line breaks and returns a list
# print('my name is ' + a.lower()) # startswith()	Returns true if the string starts with the specified value
# print('my name is ' + a.lower()) # strip()	Returns a trimmed version of the string
# print('my name is ' + a.lower()) # swapcase()	Swaps cases, lower case becomes upper case and vice versa
# print('my name is ' + a.lower()) # title()	Converts the first character of each word to upper case
# print('my name is ' + a.lower()) # translate()	Returns a translated string
# print('my name is ' + a.lower()) # upper()	Converts a string into upper case
# print('my name is ' + a.lower()) # zfill()	Fills the string with a specified number of 0 values at the beginning

# string formating 
name = "RAM"
age = 26
print("hello {} your age is {}".format( name, age))   #Python 3
print(f"hello {name} your age is {age +2}")  # Python 3.6

