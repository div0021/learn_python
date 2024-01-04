# This happen when function call itself


def add_one(num):
    if num >= 9:
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)


print(add_one(1))

# do above task using loops

for i in range(2, 11):
    print(i)
