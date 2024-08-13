import os
import random

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'

def prompt(message):
    print(f'==> {message}')


def display_board():
    os.system('clear')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')


def initialize_board():
    return {square: INITIAL_MARKER
            for square in range(1, 10)
            }

def empty_squares(board):
    return [key
            for key, value in board.items()
            if value == INITIAL_MARKER]

def player_choice(board):
    while True:
        valid_choices = [str(square) for square in empty_squares(board)]
        prompt(f'Choose a square ({", ".join(valid_choices)}):')
        square = input().strip()

        if square in valid_choices:
            break

        prompt('Sorry that\'s not a valid square')

    board[int(square)] = PLAYER_MARKER

def computer_choice(board):
    square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER


board = initialize_board()
display_board()

player_choice(board)
computer_choice(board)
display_board()