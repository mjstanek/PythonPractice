# !/usr/bin/env python3

# This is a practice file for loops in Python.
# Loops will repeat an action(s) until a condition is met.

# The While loop will repeat an action(s) while a condition is True.

#This loop demonstrates the use of a while loop.
# The loop will continue until the counter variable is equal to 0.
# WWhile the counter is not equal to 0, the loop will print the value of the counter and decrement it by 1.
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

# The for loop will repeat an action(s) for a specified number of iterations.

# This loop demonstrates the use of a for loop.
# The loop will iterate over a range of numbers from 0 to 4.
for i in range(5):
    print("Inside the for loop.", i)

# The for loop can also iterate over a list.
for item in ["apple", "banana", "cherry"]:
    print("Inside the for loop with a list.", item)

for x in "Hello World":
    print("Inside the for loop with a string.", x)

# Loops have a break statement that will exit the loop immediately.
# This loop will print the numbers from 0 to 4, but will break when it reaches 3.
for num in range(5):
    if num == 3:
        print("Breaking the loop at", num)
        break
    print("Inside the loop before break.", num)

# The continue statement will skip the current iteration and continue with the next one.
# This loop will print the numbers from 0 to 4, but will skip the number 2.
for num in range(5):
    if num == 2:
        print("Skipping the number", num)
        continue
    print("Inside the loop before continue.", num)

# Else statements can be used with loops.
# In a while loop, the else statement will execute when the loop condition becomes False.
a = 1
while a < 5:
    print(a)
    a += 1
else:
    print("else:", a)
# In a for loop, the else statement will execute when the loop has iterated over all items.
for b in range(5):
    print(b)
else:
    print("else:", b)

# Pyramid wall layer calculation
blocks = int(input("Enter the number of blocks: "))
layers = 0
currentblocks = blocks

while currentblocks > layers:
    layers += 1
    currentblocks -= layers
    
print("The height of the pyramid:", layers)

# Luthat Collatz Theorem
# The Luthar Collatz theorem states that for any positive integer c0,
# if c0 is even, the next number is c0/2, and if c0 is odd, the next number is 3*c0 + 1.
# The sequence will eventually reach 1.
c0 = int(input("Luthar Collatz theorem starting number: "))

while c0 != 1:
    if c0%2 == 0:
        c0 = c0/2
    else:
        c0 = (3*c0)+1
    print(int(c0))

# This loop will print the digits of a number, replacing '0' with 'x'.
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")
    