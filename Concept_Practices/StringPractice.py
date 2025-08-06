#!/usr/bin/env python3

# This practice file is for strings and string operations in Python.

# Strings are immutable sequences of characters.
# Strings can be defined using single quotes, double quotes, or triple quotes for multi-line strings.
# Strings can have their length checked using the len() function.
# Strings can also be empty.
# Strings use the backslash as an escape character for special characters like quotes and newlines, and it is not included in the string length.

string1 = "Hello, World!"
string2 = ''
string3 = 'I\'m a string with an escape character.'
string4= '''1
2'''

print('String 1:', string1, 'Length:', len(string1))
print('String 2:', string2, 'Length:', len(string2))
print('String 3:', string3, 'Length:', len(string3))
print('String 4:', string4, 'Length:', len(string4), 'The length does include the newline character "\\n" and the end of the first line')

# Strings can be concatenated using the + operator.
# Strings can also be repeated using the * operator.

string5 = 'h'
string6 = 'i'
print('Concatenated String:', string5 + string6)
print('Repeated String:', string5 * 3)

# The ord() function returns the Unicode code point of a character.
# It can only be used with a single character.

print('Unicode code point of "h":', ord(string5))
print('Unicode code point of "i":', ord(string6))

# The chr() function returns the character corresponding to a Unicode code point.

print('Character for Unicode code point 104:', chr(104))
print('Character for Unicode code point 105:', chr(105))

# Please note that calling chr(ord('character')) will return the same character.
# And vice versa, ord(chr(code_point)) will return the same code point.

print('Character for Unicode code point of "h":', chr(ord(string5)))
print('Unicode code point of "i":', ord(chr(ord(string6))))

# Strings can be indexed, sliced, and iterated over, much like lists.

for i in range(len(string1)):
    print(f'Index {i}: {string1[i]}')

print('Part of string 3:', string3[6:12])

# In/Not In operators can be used to check if a substring exists within a string.

print('Is "World" in string1?', 'World' in string1)
print('Is "GoodBye" in string1?', 'GoodBye' in string1)
print('Is "Hello" not in string1?', 'Hello' not in string1)
print('Is "Moon" in string2?', 'Moon' in string2)

# As strings are immutable, they cannot be changed in place.
# the del, append, insert, and pop methods do not work on strings.
# The following lines of code will raise an error if uncommented.

# del string1[0]  # Raises TypeError: 'str' object doesn't support item deletion
# string1[0] = 'h'  # Raises TypeError: 'str' object does not support item assignment
# string1.append('!')  # Raises AttributeError: 'str' object has no attribute 'append'
# string1.insert(0, 'H')  # Raises AttributeError: 'str' object has no attribute 'insert'
# string1.pop()  # Raises AttributeError: 'str' object has no attribute 'pop'

# To modify a string, we can create a new string with the desired changes.

string1_modified = 'h' + string1[1:]
print('Modified String 1:', string1_modified)

# We can also modify a string by setting the variable to a new value.

string1 = string1 + '!'
print('String 1 after modification:', string1)

# The min() and max() functions work on strings, but they compare based on Unicode code points.

print('Minimum character in string1:', min(string1))
print('Maximum character in string1:', max(string1))

# The index() method returns the index of the first occurrence of a substring in a string.

print('"ll" in string1 at index:', string1.index('ll'))
print('"o" in string1 at index:', string1.index('o'))

# If the substring is not found, index() raises a ValueError.
# That is why we can use the find() method, which returns -1 if the substring is not found.

print('"xyz" in string1?')
try:
    print('yes, at:', string1.index('xyz'))
except ValueError as e:
    print('ValueError:', e)

print('"xyz" in string1 at index:', string1.find('xyz'))  # Returns -1 if not found

# find() can also be called with start and end parameters to limit the search range.

print('Index of "l" in string1 starting from index 3:', string1.find('l', 3, 5))
print('Index of "l" in string1 starting from index 5:', string1.find('l', 5))

# The rfind() method returns the highest index of the substring if found, and -1 otherwise.

print('Last index of "l" in string1:', string1.rfind('l'))
print('Last index of "o" in string1:', string1.rfind('o'))

# The count() method returns the number of occurrences of a substring in a string.

print('Count of "l" in string1:', string1.count('l'))
print('Count of "o" in string1:', string1.count('o'))

# Strings can be cast into a list using the list() function.
string_as_list = list(string1)
print('String as list:', string_as_list)

# The capitalize() method capitalizes the first character of a string and makes all other characters lowercase.
print('abcd' + ' after capitalize():', 'abcd'.capitalize())
print('AbCd' + ' after capitalize():', 'AbCd'.capitalize())
print(' ABCD' + ' after capitalize():', ' ABCD'.capitalize())
print('123' + ' after capitalize():', '123'.capitalize())

# The center() method centers a string within a specified width, padding with spaces by default.
# If the original string is longer than the specified width, it will not be truncated.

center = 'Hello'
print(f'[{center.center(20)}] - Width 20')
print(f'[{center.center(10)}] - Width 10')
print(f'[{center.center(5)}] - Width 5')  # No change, as the string is not longer than the width

# If we call the center() method with two arguments, the second argument specifies the character to use for padding.
print(f'[{center.center(20, "#")}] - Width 20 with # padding')
print(f'[{center.center(10, "$")}] - Width 10 with $ padding') 
print(f'[{center.center(5, "*")}] - Width 5 with * padding')  # No change, as the string is not longer than the width

# The endswith() method checks if a string ends with a specified suffix.
# The startswith() method checks if a string starts with a specified prefix.

print('Does string1 end with "!"?', string1.endswith('!'))
print('Does string1 end with "earth"?', string1.endswith('earth'))
print('Does string1 start with "hey"?', string1.startswith('hey'))
print('Does string1 start with "Hello"?', string1.startswith('Hello'))

# The isalnum() method checks if a string contains only alphanumeric characters (letters and numbers).

print('Is "Hello123" alphanumeric?', 'Hello123'.isalnum())
print('Is "Hello 123" alphanumeric?', 'Hello 123'.isalnum())
print('Is "Hello_123" alphanumeric?', 'Hello_123'.isalnum())

# The isalpha() method checks if a string contains only alphabetic characters (letters).

print('Is "Hello" alphabetic?', 'Hello'.isalpha())
print('Is "Hello123" alphabetic?', 'Hello123'.isalpha())
print('Is "Hello 123" alphabetic?', 'Hello 123'.isalpha())

# Conversely, the isdigit() method checks if a string contains only digits (numbers).

print('Is "123" a digit?', '123'.isdigit())
print('Is "123abc" a digit?', '123abc'.isdigit())
print('Is "123,456" a digit?', '123,456'.isdigit())

# The islower() method checks if all characters in a string are lowercase.

print('Is "hello" lowercase?', 'hello'.islower())
print('Is "Hello" lowercase?', 'Hello'.islower())
print('Is "HELLO" lowercase?', 'HELLO'.islower())

# The isupper() method checks if all characters in a string are uppercase.

print('Is "HELLO" uppercase?', 'HELLO'.isupper())
print('Is "Hello" uppercase?', 'Hello'.isupper())
print('Is "hello" uppercase?', 'hello'.isupper())

# The isspace() method checks if a string contains only whitespace characters (spaces, tabs, newlines).

print('Is "   " a space?', '   '.isspace())
print('Is "\\t\\n" a space?', '\t\n'.isspace())
print('Is "Hello" a space?', 'Hello'.isspace())

# The join() method concatenates a list of strings into a single string, using the specified separator.
# The string the join method is called on is used as the separator.
# The argument passed to the join method must be an iterable (like a list or tuple) of strings.

separator = '/\\'
join_list = ['Mountain', 'Lake', 'Beach']
print('Join list with separator:', separator.join(join_list))

# The lower() method converts all characters in a string to lowercase.
# The upper() method converts all characters in a string to uppercase.

string7 = 'aBcDeFgH'
print('Original string:', string7)
print('Uppercase string:', string7.upper())
print('Lowercase string:', string7.lower())

# The swapcase() method swaps the case of all characters in a string.

print('Swapcase string:', string7.swapcase())
print('Swapcase on string3:', string3.swapcase())

# The title() method capitalizes the first character of each word in a string.

print('Title case string:', string3.title())

# Strip, lstrip, and rstrip methods remove whitespace from the beginning and/or end of a string.
# Strip removes whitespace from both ends, lstrip removes from the left end, or leading, and rstrip removes from the right end, or trailing.

string8 = '   Hello, World!   '
print('Original string:','[', string8,']')
print('Stripped string:','[', string8.strip(),']')
print('Left stripped string:','[', string8.lstrip(),']')
print('Right stripped string:','[', string8.rstrip(),']')

# These methods can also take an optional argument to specify which characters to remove.

string9 = '---Hello, World!---'
print('Original string with dashes:','[', string9,']')
print('Stripped string with dashes:','[', string9.strip('-'),']')
print('Left stripped string with dashes:','[', string9.lstrip('-'),']')
print('Right stripped string with dashes:','[', string9.rstrip('-'),']')

# The replace() method replaces ALL occurrences of a substring with another substring in a string.

string10 = 'This is a test string. This is only a test.'
print('Original string:', string10)
print('Replaced "test" with "example":', string10.replace('test', 'example'))
print('Replaced "is" with "was":', string10.replace('is', 'was'))

# The replace() method can also take an optional third argument to limit the number of replacements.

print('Replaced "is" with "was" only once:', string10.replace('is', 'was', 1))

# The split() method splits a string into a list of substrings based on a specified separator.
# If no separator is specified, it splits on whitespace by default.

string11 = 'apple,banana,cherry'
print('Original string:', string11)
print('Split by comma:', string11.split(','))
print('Split by whitespace:', 'Hello World'.split())
print('Split on the letter "O":', 'Hello World'.split('o'))
