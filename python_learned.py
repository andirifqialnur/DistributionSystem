# List and Dictionary

mylist = ["sembarang", "sembarang", "sembarang"]
print(mylist)

print(len(mylist))

mylist = ["sembarang", 54, True, 7.89, 'd']
print(type(mylist[0]))
print(type(mylist[1]))
print(type(mylist[2]))
print(type(mylist[3]))
print(type(mylist[4]))

mylist = list((13, 56, 33))
print(mylist)

data = {
	"Name" : "Andi Rifqial Nur",
    "NIM" : 42519030,
    "Age" : 21,
    "Height" : 1.6,
    "color" : ["navy", "black", "white"],
}

print(data["Name"])
print(data["color"][0][1])
print(data["Age"])
print(data["Height"])

print(len(data))
print(type(data))


#  Classess

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print(f"Hello my name is {self.name} and now i'm {self.age}")

p1 = Person("John", 36)
p1.myfunc()

""" 

File Handling 

You have to specified the location first or you can do it in the command like below


"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

---------------------------------------------------------------------------------------------

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


"""
# read file

f = open("C:\\Users\andir\Downloads\sembarang.txt", "r") # 'r' to readfile

print(f.read())
print(f.read(5)) # it will print 5 character in the first file
print(f.readline())
for x in f:
    print(x)
f.close()


# write files

f = open("C:\\Users\andir\Downloads\sembarang.txt", "a") # 'a' to appendfile | 'w' to writefile

f.write("sembarang mo situ")
f.close()


# create file

f = open("C:\\Users\andir\Downloads\sembarang2.txt", "x") # x to createfile
print(f.write())


# delete file (you have to import os first then you can run it with command 'os.remove()')

#remove manually
import os
os.remove("sembarang.txt")

#remove with condition
if os.path.exists("sembarang.txt"):
    os.remove("sembarang.txt")
else:
    print("File doesn't exists")

#remove folder
os.rmdir("example")
