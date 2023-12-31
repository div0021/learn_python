import math
# Ternary Operator
# meaning = 2
# print('Right On!') if meaning > 10 else print('Nt today')

# #literal assignment
first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# #constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

## concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#Casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "'s."
print(statement)

#Mulitple lines
multiline = ''''
Hey,how are you?

I was just checking in.
                      All good?


'''
print(multiline)

#escaping special characters
sentance = 'I\'m back at work!\tHey!\n\nWhere\'s this\\located?'
print(sentance)

#string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)
print(len(multiline))

multiline += "                               "
multiline = "                      " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

#Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

#string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

#Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))

#Boolean data type
myvalue = False  #True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#Numeric data type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

#complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

#Build in function for numbers
print(abs(gpa))
print(abs(-1 * gpa))
print(round(gpa))
print(round(gpa, 1))

#modules are alway on the top of file

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
print(math.pi)

#Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

#Error if you attemp to case incorrect data
# zip_value = int("New york")
