# !/usr/bin/env python3

# This is a practice file for tuples and dictionaries in Python.

# Tuples
# Tuples are similar to lists, but they are immutable
# This means that once a tuple is created, it cannot be changed
# Tuples are usually defined using parentheses ()

tuple1 = (1, 2, 3)
tuple2 = 4, 5, 6
print("Tuple 1:", tuple1, "Tuple 2:", tuple2)

# Tuples can be crated empty
empty_tuple = ()

# Tuples can also contain only one item, but a comma is required
single_item_tuple = (1,)

# Accessing elements in a tuple is similar to lists
print("First element of tuple1:", tuple1[0])
print("Last element of tuple2:", tuple2[-1])

# Tuples can be unpacked into variables
a, b, c = tuple1
print("a + b + c =", a + b + c)

# Duplicates in tuples are allowed, just like in lists
tuple_with_duplicates = (1, 2, 2, 3, 4)
print("Tuple with duplicates:", tuple_with_duplicates)

# The count() method can be used to count the number of occurrences of an item in a tuple
print("Count of 2 in tuple_with_duplicates:", tuple_with_duplicates.count(2))

# Dictionaries
# Dictionaries are used to store data in key-value pairs
# They are defined using curly braces {}
spanish_animals = {
    "dog": "perro",
    "cat": "gato",
    "bird": "pájaro",
    "horse": "caballo",
    "pig": "cerdo"
}

print("Spanish Animals Dictionary:", spanish_animals)

# Accessing values in a dictionary is done using the key
# This also means that each key must be unique
# (Keys are case-sensitive, if they are strings)
print("The Spanish word for dog is:", spanish_animals["dog"])
# Dictionaries are also one-way mappings
# This means that you cannot use the value and return the key

# Dictionaries are mutable, meaning you can add, remove, or change items
# Adding a new key-value pair
spanish_animals["fish"] = "pez"
print("Updated dictionary:", spanish_animals)
# Key-value pairs can also be updated by assigning a new value to an existing key
spanish_animals["dog"] = "perrito"
print("Updated dictionary with new dog value:", spanish_animals)

# Two more update methods are the update() method and the del instruction
# The update() method can be used to add multiple key-value pairs at once
spanish_animals.update({"rabbit": "conejo", "snake": "serpiente"})
print("Dictionary after update method:", spanish_animals)
# The del instruction can be used to remove a key-value pair
del spanish_animals["cat"]
print("Dictionary after deleting cat:", spanish_animals)

# Dictionaries are also non-ordered, meaning the order of items is not guaranteed
# However, you can iterate over the keys or values
for key in spanish_animals.keys():
    print("Key:", key, "| Value:", spanish_animals[key])
# Similarly, you can iterate over the values
# This will not return the keys, however
for value in spanish_animals.values():
    print("Value:", value)
# You can also iterate over both keys and values
for key, value in spanish_animals.items():
    print("Key:", key, "| Value:", value)