# !/usr/bin/env python3

# This is a practice function to check if two strings are anagrams of each other.

# Initialization function
# Prompts user for input and calls the anagram checker function
def initialize():
    print("Anagram Checker Initialized")
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    if anagram_checker(string1, string2):
        print(f'"{string1}" and "{string2}" are anagrams.')
    else:
        print(f'"{string1}" and "{string2}" are not anagrams.')

# Anagram checker function
# Checks if two strings are anagrams by comparing their letters
def anagram_checker(string1, string2):
    # Removes spaces and standardizes case
    string1 = string1.replace(" ", "").lower()
    string2 = string2.replace(" ", "").lower()
    # Length and sanity check
    if len(string1) != len(string2):
        return False
    # Checks to see if all the letters are used in both strings
    for letter in string1:
        if letter not in string2:
            return False
    for letter in string2:
        if letter not in string1:   
            return False
    return True

if __name__ == "__main__":
    initialize()
