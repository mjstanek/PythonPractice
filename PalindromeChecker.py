#!/usr/bin/env python3

def palindrome_checker(string):
    stripped_string = string.replace(' ', '')
    reverso = -1
    valid = True
    for i in range(len(stripped_string)):
        if stripped_string[i].lower() != stripped_string[reverso].lower():
            valid = False
            break
        else:
            reverso -= 1
    if valid:
        print(f'{string.title()} is a plaindrome!')
    else:
        print(f'{string.title()} is not a palindrome.')
        

if __name__ == '__main__':
    string = input('Please enter a word or phrase to see if it is a palindrome: ')
    palindrome_checker(string)
