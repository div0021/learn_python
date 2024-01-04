#Exception error


class JustNotCoolError(Exception):
    pass


x = 2
try:
    #custom exception raise
    #raise Exception("I'm a custom exception.")
    raise JustNotCoolError("This is not cool man!")

    #print(x)
    #print(x /0)
    print(x / 1)

    #rasing you own error
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means something is probably undefined..")
except ZeroDivisionError:
    print("Please do not divide by zero.")
except Exception as error:
    print(error)
else:
    print("No errors!")
finally:
    print("I'm going to print with or without an error.")
