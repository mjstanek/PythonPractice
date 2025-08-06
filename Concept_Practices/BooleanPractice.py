#!/usr/bin/env python3

# This is a practice file for boolean operations in Python.

# Boolean values identify if a condition is True or False.

# To compare values, we use comparison operators:
# == (equal to), != (not equal to), < (less than), > (greater than),
# <= (less than or equal to), >= (greater than or equal to).

# The following statements are True:
print(1 == 1)
print(1 == 1.0)
print(1 < 2)

# The following statements are False:
print(1 == 2)
print(1 < 1)
print(1 >= 2)

# Variables must be defined before they can be used.
x = 1
print (x == 1)

# Attempting to use an undefined variable will raise a NameError.
# print(y == 1) 

# Boolean expression evaluation with user input
n = int(input("Please enter a number: "))
print("Is you number greater than 10? ", n > 10)

# Boolean expressions and if statements

# Spathiphyllum shout out
plant = input("Can you think of a plant? ")
if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not {plant}!")

# Nested if statements
year = int(input("Enter a year: "))
if year < 1582:
    print('There were no leap years before the Gregorian calendar.')
elif year % 4 != 0:
    print('This is a standard, 365-day year.')
elif year%100 == 0:
    if year%400 != 0:
        print('This is a standard, 365-day year.')
    else:
        print('This is a leap year with 366 days.')   
else:
    print('This is a leap year with 366 days.')
