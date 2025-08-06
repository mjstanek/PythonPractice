#!/usr/bin/env python3

# This is a practice file for variable usage in Python.
# Variables can be assigned values using the equals sign (=).

# Set variable "var" to 1
var = 1

# Print the value of "var"
print(var)

# Reassign "var" to 2
var = 2
print(var)

# Set the variable "var" to the sum of its current value and 1
var = var + 1
print(var)

# Increment the variable "var" by 1
var += 1
print(var)

# Deomnstate variable reassignment
demo = "One Fish"
demo = "Two Fish"
print(demo)

# Variables in mathematical expressions
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  
print(f"Based on the Pythagorean theorem, the hypotenuse \
of a right triangle with sides {a} and {b} is {c:.1f}.")

# Compound assignment operators resolve second
x = 6
y = 3
x /= 2 * y
# The above line is equivalent to x = x / (2 * y)
print(x)
