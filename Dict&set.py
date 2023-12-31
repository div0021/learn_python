#Dictionary

band = {"vocals": "Plant", "guitar": "Tommy Lee"}
brand2 = dict(vocals="Plants", guitar="Tom")
print(band)
print(brand2)
print(type(band))
print(len(band))

#Accessing Values
print("Vocals: ", band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

# list of key/values pairs as tuples
print(band.items())

#verify a key exist
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPG"})
print(band)

print(band.pop("bass"))

print(band)

band['drum'] = "Bonham"
print(band)

print(band.popitem())  #tuple
print(band)

#Delete and clear
band['drum'] = "Bonham"
del band["drum"]
print(band)

brand2.clear()
print(brand2)
del brand2

#copy dictonaries
#way not to create copy.
# band2 = band  #create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2['drums'] = 'Dave'
# print(band)

#way to copy
band2 = band.copy()
band2['drums'] = "Dave"
print(band)
print(band2)

# or use dict constructor
band3 = dict(band)
print(band3)

# Nested dictonaries
member1 = {
    "name": "Plant",
    "instrument": "guitar",
}
member2 = {"name": "Page", "instrument": "bass"}
band = {"member1": member1, "member2": member2}

print(band)
print(band["member1"]["name"])
# print(band.memeber1.name)   Not working

#Sets

nums = {
    1,
    2,
    4,
    6,
    7,
    8,
}
nums2 = set((
    1,
    2,
    4,
    5,
    6,
    57,
))
print(nums2)
print(nums)
print(type(nums))
print(len(nums))

#No duplicate are allowed
nums = {
    1,
    3,
    3,
    5,
    3,
    2,
}
print(nums)

#True is dupe of 1, False is a dupe of zero
nums = {1, True, False, 2, 5, 0, False}
print(nums)

#check if a value is in a set
print(2 in nums)

#but you cannot refer to an element in the set with an index position or key

# Add a new element to set
nums.add(32)
print(nums)

#Add elements from one set to another
morenums = {52, 62, 72}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples and dictonaries etc.

#Merge two sets to create a new set
one = {1, 3, 5}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

#Keep only duplicates
one = {1, 3, 5}
two = {2, 3, 5}
one.intersection_update(two)
print(one)

#Not to keep duplicate only
one = {1, 3, 5}
two = {2, 5, 7}
one.symmetric_difference_update(two)
print(one)
