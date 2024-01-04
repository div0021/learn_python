name = "Div"

# def greeting(firstname):
#     color = "blue"
#     print(color)
#     print(name)
#     print(firstname)

# def greeting(name):
#     color = "blue"
#     print(color)
#     print(name)  #this variable is local not global

# greeting("zpp")
# print(color)

count = 1


def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Loo")


another()
