#!/usr/bin/env python3

# This practice file is a function that splits a string into a list of words on the blank space character.


def mysplit(strng):
    output = []
    word = ''
    for ch in range(len(strng)):
        # If the character is not a space, append it to the current word
        if ord(strng[ch]) != 32:
            word = word + strng[ch]
        # If the character is a space or the end of the string
        if ord(strng[ch]) == 32 or ch == len(strng) - 1:
            # If the word is not empty, append it to the output list
            if len(word) != 0:
                output.append(word)
            # Reset the word to start a new one
            word = ''
    return output

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))