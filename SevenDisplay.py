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
    # Original function, technically more efficient
    
    # Generates five local variables to hold the individual line outputs
    # line1 = ''
    # line2 = ''
    # line3 = ''
    # line4 = ''
    # line5 = ''

    # Loop through the numbers to display and appends the dictionary of the line
    # into the appropriate line
    # for number in display:
    #     line1 = line1 + ' ' + number[1]
    #     line2 = line2 + ' ' + number[2]
    #     line3 = line3 + ' ' + number[3]
    #     line4 = line4 + ' ' + number[4]
    #     line5 = line5 + ' ' + number[5]

    # Print the lines individually
    # print(line1) 
    # print(line2)
    # print(line3)
    # print(line4)
    # print(line5)

    # Second attempt to make a cleaner, more concise code
    # Technically less efficient because it is a nested loop

    # Create a single variable to hold the output
    output = ''

    # Loop through each line to display
    for line in range(1, len((zero.keys())) + 1):
        # For each line, loop through the numbers in the list to display
        for number in display:
            # Append the output of the number at the specified line to the output variable
            output += number[line] + ' '
        # Once each number to display has been looped through, move to a new line
        output += '\n'

    # Display the output
    print(output)

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
