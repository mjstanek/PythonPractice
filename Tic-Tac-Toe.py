# !/usr/bin/env python3

import random

board = [[False for i in range(3)] for j in range (3)]

board[0] = ['1', '2', '3']
board[1] = ['4', 'X', '6']
board[2] = ['7', '8', '9']

rows = {
    1 : 0,
    2 : 0,
    3 : 0,
    4 : 1,
    5 : 1,
    6 : 1,
    7 : 2,
    8 : 2,
    9 : 2
}

columns = {
    1 : 0,
    2 : 1,
    3 : 2,
    4 : 0,
    5 : 1,
    6 : 2,
    7 : 0,
    8 : 1,
    9 : 2
}

victory_conditions = {
    1 : [1, 2, 3],
    2 : [1, 5, 9],
    3 : [1, 4, 7],
    4 : [2, 5, 8],
    5 : [3, 6, 9],
    6 : [3, 5, 7],
    7 : [4, 5, 6],
    8 : [7, 8, 9]
}

occupied_spaces = "X", "O"
# print(board)


def display_board(board):

    print("Here's the updated board:")

    for row in board:
        if row == board[0]:
            print(' +---+---+---+')
        print(" |" ," | ".join(row), "|")
        if row != board[2]:
            print(' +---+---+---+')
        if row == board[2]:
            print(' +---+---+---+')

    enter_move(board)


def enter_move(board):

    move = int(input("Please enter the number of the square you want: "))

    while True:

        if move <= 0 or move > 10:
            move = int(input("Please enter the VALID number of the square you want: "))

        else:

            if board[rows[move]][columns[move]] not in occupied_spaces:
                board[rows[move]][columns[move]] = "O"
                break

            elif board[rows[move]][columns[move]] in occupied_spaces:
                move = int(input("Hmm, it seems that spot is taken, please try again: "))

    victory_for(board, "O")

def make_list_of_free_fields(board):

    free_spots = []

    for cell in range(1, 10):
        if board[rows[cell]][columns[cell]] not in occupied_spaces:
            free_spots.append(int(board[rows[cell]][columns[cell]]))

    choice = random.choice(free_spots)
    board[rows[choice]][columns[choice]] = "X"
    victory_for(board, "X")

def victory_for(board, sign):

    v = 0
    winner = False
    owned_cells = []
    claimed_cells = []

    for spot in board[0]:
        v += 1
        if sign in spot:
            owned_cells.append(v)
        elif spot == "X" or "O":
            claimed_cells.append(v)

    for spot in board[1]:
        v += 1
        if sign in spot:
            owned_cells.append(v)
        elif spot == "X" or "O":
            claimed_cells.append(v)

    for spot in board[2]:
        v += 1
        if sign in spot:
            owned_cells.append(v)
        elif spot == "X" or "O":
            claimed_cells.append(v)

    if len(owned_cells) >= 3:
        for condition in victory_conditions.values():
            if condition in owned_cells or condition == owned_cells:
                winner = True

    if winner == False and len(owned_cells) != 9:
        if sign == "X":
            display_board(board)
        else:
            make_list_of_free_fields(board)
    elif winner == False and len(owned_cells) == 9:
        print("We tied, nice job.")
    elif winner == True:
        for row in board:
            print(" | ".join(row))
            if row != board[2]:
                print('--+---+---')
        if sign == "X":
            print("HA! My skills are unmatched. Good game!")
        else:
            print("Woah woah woah. You beat me? Good job, I guess")
        
def initialize():
    begin = input("Would you like to play Tic-Tac-Toe with me? Enter Y or N: ")
    if type(begin) == str:
        begin = begin.replace(" ", "").upper()
        if begin == "Y":
            print("All right! Dibs on X, I go first!")
            display_board(board)
        elif begin == "N":
            print("Aww man, really? Okay, maybe next time.")
        else:
            print("Wow, not good at following instructions, are we?")
    else:
        print("Bro did you even try to hit a letter?")
        print("Come back when you can find a keyboard that works. Or glasses.")
        
if __name__ == "__main__":
    initialize()
