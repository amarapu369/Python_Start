# f = open("demofile.txt", "wt")

# f = open("demofile.txt", "rt")
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.read(10))

# for x in f:
#   print(x)

# f.close()
import os
# f = open("demofile2.txt", "w")
# f.write("Now the file has more content!")
# f.close()

#open and read the 
# file after the appending:
# f = open("demofile3.txt", "x")
# print(f.read())
# x = open("demofile3.txt", "w")
# x.write("my name is Ramprasad")
# x = open("sample.txt","r")
# print(x.read())
# os.remove("demofile2.txt")



if os.path.exists("demofile3.txt"):
  print("yes the file is exist")
  os.remove("demofile3.txt")
else:
  print("The file does not exist")


os.rmdir("myfolder")