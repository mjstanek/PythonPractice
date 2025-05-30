#!/usr/bin/env python3

print('Hello World!')
print('This text is the argument to the print function.')
print('This text is printed to the console.')
print()
print('This is a test of the \nprint function on a new line.')
print('Here we have one line.' ,end=' ')
print('This is the continuation of that line.')
# The next line fails because the keyword argument 'end' must be the last argument.
# print(end = ' ', 'This is another print statement.')
print('I', 'am', 'separating', 'these', 'words', 'with', 'a', 'dollar', 'sign', sep='$')
print('Duplication' * 2)
print('*****', '*   ***', '*   * *', '*   ***', '*****', sep='\n')
print(0o123, 0x123, 123, sep=' | ')
print('Is true greater than false?', True > False)
print('Is true less than false?', True < False)