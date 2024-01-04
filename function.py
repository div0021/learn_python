#function


def hello_world():
    print("Hello World!")


hello_world()  # Call the function


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return (num1 + num2)


total = sum(4, 5)
print(total)

#None is special type which comes from NoneType class.


# having multiple argument but don't know number of parameters and the collection which is going to store these value is tuple
def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "Alix", "muk")


# kwargs means key word arguments
def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", second="Div", third="Dip")
