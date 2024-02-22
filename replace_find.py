# tutorial for the replace any string and any space 
name = "ram is the very good boy, he is so talented"
print(name.replace("r","R"))
print(name.replace("is","was"))
print(name.replace("is","was", 1))
print(name.replace("ram","Ramprasad"))
print(name.find("ram"))
print(name.find("is", 5 ))
print(name.replace("is","was", 1).find("is")) #methos 1
pos = (name.find("is"))
print(name.find("is", pos + 1))

