#!/usr/bin/env python3

# This is a practice file for exploring the print function in Python.
# The print function is used to output text to the console.
# It can take multiple arguments, and it has optional parameters for formatting.

# Printing various strings to the console
print('Hello World!')
print('This text is the argument to the print function.')
print('This text is printed to the console.')

# Call the print function with no arguments
print()

# Test the print function with the new line character
print('This is a test of the \nprint function on a new line.')

# Print two different strings on the same line with the end parameter
print('Here we have one line.' ,end=' ')
print('This is the continuation of that line.')

# The next line fails because the keyword argument 'end' must be the last argument.
# print(end = ' ', 'This is another print statement.')

# Test the print function with the sep parameter
print('I', 'am', 'separating', 'these', 'words', 'with', 'a', 'dollar', 'sign', sep='$')

# Strings can be duplicated using the multiplication operator
print('Duplication' * 2)

# Print an ASCII box using a single print statement
print('*****', '*   ***', '*   * *', '*   ***', '*****', sep='\n')

# Print the value of "123" in octal, hexadecimal, and decimal formats
print(0o123, 0x123, 123, sep=' | ')

# Print Boolean value comparisons
print('Is true greater than false?', True > False)
print('Is true less than false?', True < False)
