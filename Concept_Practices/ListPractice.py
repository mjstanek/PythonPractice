# !/usr/bin/env python3

# This file is to demonstrate the use of lists in Python.
# Lists are used to store multiple items in a single variable.
# Lists are created using square brackets [].

numbers = [5, 2, 9, 1, 5, 6]
print("Original list:", numbers)

# Values can be reassigned using their index.
numbers[0] = 10
print("Updated list:", numbers)

# This can also be done with negative indices.
numbers[2] = numbers[-1] # Sets the third item to the last item in the list.
print("New list with negative index:", numbers)

# Elements within a list can be accessed using their index.
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# The length of a list can be found using the len() function.
print("Length of the list:", len(numbers))

# Items within a list can be deleted using the del statement.
del numbers[3]  # Deletes the fourth item in the list.
print("List after deletion:", numbers)

# List Methods
# Lists have several built-in methods that can be used to manipulate them.

# Append 
# This method adds an item to the end of the list.
numbers.append(7)
print("List after appending 7:", numbers)

# Insert
# This method inserts an item at a specified index.
# The arguments are the index and the item to be inserted.
numbers.insert(1, 8)
print("List after inserting 8 at index 1:", numbers)

# Remove 
# This method removes the first occurrence of a specified item.
numbers.remove(5)
print("List after removing 5:", numbers)

# Pop 
# This method removes and returns the last item in the list.
# If an index is specified, it removes and returns the item at that index.
popped_value = numbers.pop()
print("Popped value:", popped_value)
print("List after popping:", numbers)

# Sort
# This method sorts the items in the list in ascending order.
numbers.sort()
print("Sorted list:", numbers)

# Reverse 
# This method reverses the order of the items in the list.
# Note that this does not sort the list, it simply reverses the current order.
numbers.reverse()
print("Reversed list:", numbers)

# Slicing
# Lists can be sliced to create a new list from a portion of the original list.
sliced_list = numbers[1:4]  # Gets a slice from index 1 to 3 (4 is not included).
print("Sliced list (index 1 to 3):", sliced_list)

# Assigining lists to other lists copies the reference, not the values.
# This means that changes to one list will affect the other.
list_a = [1]
list_b = list_a
list_a.append(2)
print("List A:", list_a) 
print("List B:", list_b)

# However, slicing the list creates a new list with the values copied.
list_c = list_a[:]
list_a.append(3)
print("List A after appending 3:", list_a)
print("List C after slicing:", list_c)

# Slicing can take a start, end, and step value.
# The syntax is list[start:end:step].
start_list = numbers[2:]  
print("List from index 2 to end:", start_list)
end_list = numbers[:3]
print("List from start to index 3:", end_list)
step_list = numbers[::2]  
print("List with every second item:", step_list)
# These same slicing methods can be used with the del statement to remove items.
# del numbers[1:3]  # Deletes items from index 1 to 2

# Lists can be created as empty objects.
new_list = []

print("This list is created empty:", new_list)

print('Looping through the string "Hello World".')
for i in "Hello World":
    new_list.append(i)

print("The same list has been populated with characters from the string:", new_list)

# Python has built in functionality to check if an item is in a list.
print("Is 'H' in the list?", 'H' in new_list)
print("Is 'X' in the list?", 'X' in new_list)
print("Is 'Q' not in the list?", 'Q' not in new_list)

# Multiple Item swapping
# This can be done using tuple unpacking.
swap_list = ['apple', 3, 'cherry', 7.5, 'mint chocolate chip', '35']
print("Original swap list:", swap_list)
swap_list[0], swap_list[4] = swap_list[4], swap_list[0]  # Swaps the first and fifth items.
swap_list[1], swap_list[3] = swap_list[3], swap_list[1]  # Swaps the second and fourth items.
print("List after swapping:", swap_list)

"""
# Beatles exercise
beatles = []
print("Members before the band was founded: ", beatles)

# Add in the original members
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Original members:", beatles)

# Ask for user input to add two more members
# (Stu Sutcliffe and Pete Best)
for i in range(2):
    beatles.append(input('Please add Stu and Pete: '))
print("Members with Stu and Pete:", beatles)

# Stu and Pete leave the band
for i in range(2):
    del beatles[-1]
print("Good bye, Stu and Pete", beatles)

# Ringo Starr joins the band
beatles.insert(0 ,'Ringo Starr')
print("Welcome, Ringo!", beatles)

# testing list length
print("The Fab", len(beatles))
"""

# Checking for elements in a list
# Checking for a specific number in a list
list_to_check = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lucky_number = 7

for number in list_to_check:
    if number == lucky_number:
        print(f"Found your lucky number: {lucky_number}!")
        break

# Removing duplicates from a list
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Option 1
# Using a secondary list to store deletion indices
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
delete_indicies = []

for number in range(len(my_list) - 1):
    # print('number:', number, 'value:', my_list[number])
    if my_list[number] in my_list[number + 1:]:
        delete_indicies.append(number)

for index in reversed(delete_indicies):
    del my_list[index]

print("List after removing duplicates:", my_list)

# Option 2
# Maintaining a single list
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
index = len(my_list) - 1

for number in range(len(my_list) - 1):
    # print('number:', number, 'value:', my_list[number])
    if my_list[index] in my_list[:index]:
        del my_list[index]
    index -= 1

print("List after removing duplicates:", my_list)
