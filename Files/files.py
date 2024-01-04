# r=Read
# a=Append
# w=write
# x=create

import os

# Read - error if it doesn't exist

f = open("./Files/names.txt", "r")
#print(f.read())  # read the whole file
#print(f.read(7))

#read the lines of file
# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist.\n")
finally:
    f.close()

#Append - create the file if it doesn't exist

f = open("Files/names.txt", "a")

f.write("Joe\n")
f.close()

f = open("Files/names.txt", "r")

print(f.read())
f.close()

# Write (override)
f = open("Files/context.txt", "w")
f.write("I delete all the text")
f.close()

f = open("./Files/context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Open a files for writing, create the file if it does not exist.
f = open("./Files/newNames.txt", "w")
f.close()

#Another way to create file, but return an error if the file exists.

if not os.path.exists("./Files/tom.txt"):
    f = open("./Files/tom.txt", "x")  #x means create
    f.close()

# Delete a file

# avoid an error if it doesn't exist

if os.path.exists("./Files/tom.txt"):
    os.remove("./Files/tom.txt")
else:
    print("The file you wish to delete not exist.")

## General way of handling
with open("./Files/more_names.txt") as f:
    content = f.read()

with open("./Files/names.txt", "w") as f:
    f.write(content)
