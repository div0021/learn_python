# list is one of four collection data type in python that store or hold multiple values

users = ['Dave', 'Jhon', 'Sara']
data = ['dave', 22, True]
emptylist = []
print('Dave' in emptylist)

print(users[0])
print(users[-1])
print(users[-2])

print(users.index('Sara'))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Elsa')
print(users)

users += ['Json']
print(users)
users.extend(['Robert', 'tom'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

#Replace values
users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
# print(data)

data.clear()
print(data)

users[1:2] = ['dave']

users.sort()
print(users)

users.sort(key=str.lower)  #this only work on same type of data type
print(users)

nums = [3, 43, 24, 25, 52, 43244, 2, 43, 24]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

#keeping the list unaffected
print(sorted(nums, reverse=True))
print(nums)

#Way to make copy of list

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
numscopy.sort()
print(numscopy)
print(mycopy)
print(mynums)

#Checking the type of lists

print(type(nums))

mylist = list([1, "Niel", "Your"])
print(mylist)

#Tuples
mytuple = tuple(('Dave', 344, True))
anotherTruple = (
    2,
    3,
    5,
    34,
    2,
    3,
    2,
    2,
    2,
    3,
)  #It's called packing a tuple.

print(mytuple)
print(type(mytuple))
print(type(anotherTruple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anotherTruple
print(one)
print(two)
print(hey)

print(anotherTruple.count(2))
