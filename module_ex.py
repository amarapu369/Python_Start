# # import mymodule as md
# # md.greeting("Jonathan")
# # a = md.person1["country"]
# # print(a)
import datetime
import platform
import math
import json
import re
# # x = platform.system()
# # print(x)

# # import platform
# # # x = dir(version)
# # a = [ platform.system() ,platform.release() , platform.version() ]
# # print(a)

# # from mymodule import person1

# # print (person1["country"])

# # x = datetime.datetime.now()
# # print(x)

# # print(x.year)
# # print(x.strftime("%A"))
# x = datetime.datetime.now()

# # print(x)

# # print(x.strftime("%a"))# %a	Weekday, short version	Wed	
# # print(x.strftime("%A"))# %A	Weekday, full version	Wednesday	
# # print(x.strftime("%w"))# %w	Weekday as a number 0-6, 0 is Sunday	3	
# # print(x.strftime("%d"))# %d	Day of month 01-31	31	
# # print(x.strftime("%b"))# %b	Month name, short version	Dec	
# # print(x.strftime("%B"))# %B	Month name, full version	December	
# # print(x.strftime("%m"))# %m	Month as a number 01-12	12	
# # print(x.strftime("%y"))# %y	Year, short version, without century	18	
# # print(x.strftime("%Y"))# %Y	Year, full version	2018	
# # print(x.strftime("%H"))# %H	Hour 00-23	17	
# # print(x.strftime("%I"))# %I	Hour 00-12	05	
# # print(x.strftime("%p"))# %p	AM/PM	PM	
# # print(x.strftime("%M"))# %M	Minute 00-59	41	
# # print(x.strftime("%S"))# %S	Second 00-59	08	
# # print(x.strftime("%f"))# %f	Microsecond 000000-999999	548513	
# # print(x.strftime("%z"))# %z	UTC offset	+0100	
# # print(x.strftime("%Z"))# %Z	Timezone	CST	
# # print(x.strftime("%j"))# %j	Day number of year 001-366	365	
# # print(x.strftime("%U"))# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# # print(x.strftime("%W"))# %W	Week number of year, Monday as the first day of week, 00-53	52	
# # print(x.strftime("%c"))# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# # print(x.strftime("%C"))# %C	Century	20	
# # print(x.strftime("%x"))# %x	Local version of date	12/31/18	
# # print(x.strftime("%X"))# %X	Local version of time	17:41:00
# # print(x.strftime("%%"))#  %%	A % character	%	
# # print(x.strftime("%G"))# %G	ISO 8601 year	2018	
# # print(x.strftime("%u"))# %u	ISO 8601 weekday (1-7)	1	
# # print(x.strftime("%V"))# %V	ISO 8601 weeknumber (01-53)	01		

# x = min(5, 10, 25)
# y = max(5, 10, 25)
# print(x)
# print(y)
# x = abs(-7.25)
# print(x)
# x = pow(4, 3)
# print(x)
# x = math.sqrt(64)
# print(x)

# x = math.ceil(1.4)
# y = math.floor(1.4)
# print(x) # returns 2
# print(y) # returns 1

# x = math.pi
# print(x)



# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])


# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)
# # the result is a JSON string:
# print(y)

# import json

# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))

# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# y = json.dumps(x, indent=2)
# z = json.dumps(x, indent=4, separators=(". ", " = "))
# k = json.dumps(x, indent=4, sort_keys=True)
# print(k)
# # print(z)
# # print(y)
# # print(json.dumps(x))
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
y = re.findall("S.*a", txt)
print(y)


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)


txt = "The rain in Spain"
x = re.search("r", txt)

print("The first white-space character is located in position:", x.start())


txt = "The rain in Spain"
x = re.split("a", txt)
print(x)


txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)


txt = "The rain in Spain"
x = re.sub("a", "9", txt)
print(x)