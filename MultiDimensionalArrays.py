# !/usr/bin/env python3

# This is a practice file for multi-dimensional arrays in Python.
# Multi-dimensional arrays are used to store data in a grid-like structure.

# List comprehension
# This is a way to create a list using only a single line of code.

comprehensive_list = [x**2 for x in range(10)]
# print("List created using list comprehension:", comprehensive_list)

# Multi-dimensional arrays can be created using nested lists.

# Chessboard example
# This creates an 8x8 grid representing a chessboard.

# Each cell is initialized with a placeholder value, such as '-'.
chessboard = [['--' for i in range(8)] for j in range(8)]

# To call a single cell, we can use the row and column indices.

# The corners are filled with 'R' for rooks.
chessboard[0][0] = 'BR'
chessboard[0][7] = 'BR'
chessboard[7][0] = 'WR'
chessboard[7][7] = 'WR'

# The  next cells are filled with 'N' for knights.
chessboard[0][1] = 'BN'
chessboard[0][6] = 'BN'
chessboard[7][1] = 'WN'
chessboard[7][6] = 'WN'

# The next cells are filled with 'B' for bishops.
chessboard[0][2] = 'BB'
chessboard[0][5] = 'BB'
chessboard[7][2] = 'WB'
chessboard[7][5] = 'WB'

# The King and Queen are placed in their respective positions.
chessboard[0][3] = 'BQ'
chessboard[0][4] = 'BK'
chessboard[7][3] = 'WQ'
chessboard[7][4] = 'WK'

# Add in the Pawns using 'P' and list comprehension.
chessboard[1][0:8] = ['BP' for k in range(8)]
chessboard[6][0:8] = ['WP' for l in range(8)]

# Display the chessboard
print("Chessboard (8x8 grid):")
for row in chessboard:
    print(" ".join(row))

# Python is not limited to 2D arrays; it can handle multi-dimensional arrays of any size.

# If a condo has 20 rooms per floor, 10 floors, and 5 condos, 
# we can represent this as a 3D array.

condos = [[[False for room in range(20)] for floor in range(10)] for unit in range(5)]

# To access a specific room in a specific floor of a specific condo, we can use three indices.
# The indicies are condo number, floor number, and room number.
# This will set the 11th room on the 5th floor of the 3rd condo as occupied.
condos[2][4][10] = True  