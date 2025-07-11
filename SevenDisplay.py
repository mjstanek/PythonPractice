#!/usr/bin/env python3

# This file takes user input of a number and displays it in a seven-segment style format.
# Each digit is represented by a dictionary with keys for each line of the segment.

zero ={1 : '###', 2 : '# #', 3 : '# #', 4 : '# #', 5 : '###'}
one = {1 : '  #', 2 : '  #', 3 : '  #', 4 : '  #', 5 : '  #'}
two = {1 : '###', 2 : '  #', 3 : '###', 4 : '#  ', 5 : '###'}
three = {1 : '###', 2 : '  #', 3 : '###', 4 : '  #', 5 : '###'}
four = {1 : '# #', 2 : '# #', 3 : '###', 4 : '  #', 5 : '  #'}
five = {1 : '###', 2 : '#  ', 3 : '###', 4 : '  #', 5 : '###'}
six = {1 : '###', 2 : '#  ', 3 : '###', 4 : '# #', 5 : '###'}
seven = {1 : '###', 2 : '  #', 3 : '  #', 4 : '  #', 5 : '  #'}
eight = {1 : '###', 2 : '# #', 3 : '###', 4 : '# #', 5 : '###'}
nine = {1 : '###', 2 : '# #', 3 : '###', 4 : '  #', 5 : '###'}
digits = [zero, one, two, three, four, five, six, seven, eight, nine]
display = []

def seven_display(display):
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    line5 = ''
    
    for number in display:
        line1 = line1 + ' ' + number[1]
        line2 = line2 + ' ' + number[2]
        line3 = line3 + ' ' + number[3]
        line4 = line4 + ' ' + number[4]
        line5 = line5 + ' ' + number[5]

    print(line1) 
    print(line2)
    print(line3)
    print(line4)
    print(line5)

def start_display():
    number = input('Please enter a number to display: ')
    valid = True
    for i in number:
        try:
            display.append(digits[int(i)])
        except ValueError:
            print('Please enter only positive digits.')
            valid = False
            break

    if valid:
        seven_display(display)

if __name__ == '__main__':
    start_display()
