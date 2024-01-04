squared = lambda num: num * num
print(squared(2))

addTwo = lambda num: num + 2

print(addTwo(12))

sum_TO = lambda a, b: a + b
print(sum_TO(2, 2))


############################
def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

##############################
lambda num: num * num

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

###################filter

lambda num: num % 2 != 0

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

###################
from functools import reduce

lambda acc, curr: acc + curr

numbers = [1, 2, 3, 4, 5, 6, 7, 2]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)
print(total)

print(sum(numbers, 10))

lambda acc, curr: acc + len(curr)

names = ['Dave', "John", "Jungle"]

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
