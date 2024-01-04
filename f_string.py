person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)

message = "\n{} has {} coins left".format(person, coins)

print(message)

message = "\n{1} has {0} coins left".format(coins, person)

print(message)

message = "\n{person} has {coins} coins left".format(person=person,
                                                     coins=coins)

print(message)

player = {"person": "Div", "coins": 2}

message = "\n{person} has {coins} coins left".format(**player)

print(message)

### f_string
message = f"\n{person} has {coins} coins left."
print(message)
message = f"\n{person} has {24 * 5} coins left."
print(message)
message = f"\n{person.lower()} has {coins} coins left."

print(message)

message = f"\n{player['person']} has {2 * 5} coins left."

print(message)

## You can pass formating options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.1f}")

for num in range(1, 11):
    print(f"\n2.25 times {num} is {2.25 * num:.1f}")

for num in range(1, 11):
    print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}")
