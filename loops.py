#While loop
# value = 1
# while value < 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1
# value = 1
# while value < 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Loop completed")

##For loop

names = ["Tom", "div", "vinay"]

# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "div":
#         break
#     print(x)
# else:
#     print("Loop ends")

# for x in names:
#     if x == "div":
#         continue
#     print(x)
# else:
#     print("loop ends")

#ranges

# for x in range(2, 5):
#     print(x)

# for x in range(0, 100, 5):
#     print(x)
# else:
#     print("Glad that\'s over!")

names = ["Div", "Tom", "zoo"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")
