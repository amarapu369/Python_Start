# try:
#   print("x")
# except:
#   print("An exception occurred")


try:
  print(x)
except NameError:
  print("Variable x is not defined\n")
except:
  print("Something else went wrong\n")

try:
  print(x)
except:
  print("Something went wrong\n")
else:
  print("Nothing went wrong0")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")