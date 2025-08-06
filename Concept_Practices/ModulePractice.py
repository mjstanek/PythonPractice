#!/usr/bin/env python3

# This is a practice file for importing and using modules in Python.

# Modules must first be imported before they can be used.
# The math module provides access to mathematical functions and constants.
import math

# By using the as keyword, we can give a module a different name for easier reference.
import matplotlib as mpl

# We can also import specific functions or classes from a module.
from matplotlib import pyplot as plt

# The dir() function returns a list of valid attributes for the specified module.
for item in dir(math):
    print(item, end=', ')
else:
    print("\n")

# We can name our own functions the same as a module's function, but it will override the module's function within the current scope.
# The module's function can still be accessed by using the module name.

print("Here is me calling a custom sin function and a module's sin function.")
def sin(x):
    return "This is a custom sin function."
print(sin(0))
print(math.sin(0), "is the math module's sin function.")

import module 
# print('Imported module:', module)
# We can access functions defined in the imported module.
list_1 = [i for i in range(2, 11, 2)]
list_2 = [j for j in range(0,25)]
print('Sum of list_2:', module.list_sum(list_2))
print('Product of list_1:', module.list_product(list_1))

# We can use the sys module to access system-specific parameters and functions.
import sys

# For example, we can print the directories Python searches for modules.
print("Python module search paths:")
for path in sys.path:
    print(path)
