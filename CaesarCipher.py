#!/usr/bin/env python3

def setup(shift_value):
    try:
        shift_value = int(shift_value)
    except:
        print('Please try again and enter a valid number to shift the cipher.')
    
    if shift_value < 0 or shift_value > 26:
        print('Please try again and enter a number between 1 and 25 to shift the cipher.')
    else:
        encipher(original_string, shift_value)
        
def encipher(original_string, shift_value):
    ciphertext = ''
    message = 'times'
    if shift_value == 1:
        message = 'time'
    for character in original_string:
        if character.isalpha():
            if character.isupper():
                for i in range(shift_value):
                    if character == 'Z':
                        character = 'A'
                    else:
                        character = chr(ord(character) + 1)
                ciphertext = ciphertext + character
            elif character.islower():
                for j in range(shift_value):
                    if character == 'z':
                        character = 'a'
                    else:
                        character = chr(ord(character) + 1)
                ciphertext = ciphertext + character
        else:
            ciphertext = ciphertext + character
    
    print(f'Your enciphered message is:\n{ciphertext}\nShifted {shift_value} {message}.')
            
if __name__ == '__main__':
    original_string = input('Please enter a message to encode: ')
    shift_value = input('Please enter an amount to shift the cipher, from 1 to 25: ')
    setup(shift_value)
