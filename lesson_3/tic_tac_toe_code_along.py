import os
import random

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'

def prompt(message):
    print(f'==> {message}')


def display_board(board):
    os.system('clear')

    prompt(f'Player is {PLAYER_MARKER}')
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


def join_or(valid_choices):
    if len(valid_choices) > 2:
        joined_choices = valid_choices[:-1]
        or_str = ', or '
        last_choice = valid_choices[-1]

        return ', '.join(joined_choices) + or_str + last_choice
    else:
        return ''.join(valid_choices)


def player_choice(board):
    while True:
        valid_choices = [str(square) for square in empty_squares(board)]
        prompt(f'Choose a square ({join_or(valid_choices)}):')
        square = input().strip()

        if square in valid_choices:
            break

        prompt('Sorry that\'s not a valid square')

    board[int(square)] = PLAYER_MARKER


def computer_choice(board):
    if empty_squares(board):
        square = random.choice(empty_squares(board))

        board[square] = COMPUTER_MARKER


def is_winner(board):
    return bool(detect_winner(board))


def detect_winner(board):
    winning_lines = [
                    [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows

                    [1, 4, 7], [2, 5, 8], [3, 6, 9],# columns

                    [1, 5, 9], [3, 5, 7], # diagonals
                ]
    for line in winning_lines:
        sq1, sq2, sq3 = line

        if (board[sq1] == PLAYER_MARKER
                and board[sq2] == PLAYER_MARKER
                and board[sq3] == PLAYER_MARKER):

            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):

            return 'Computer'

    return None


def board_full(board):
    return len(empty_squares(board)) == 0


def tic_tac_toe():
    board = initialize_board()

    while True:
        display_board(board)
        player_choice(board)

        if is_winner(board) or board_full(board):
            break

        computer_choice(board)

        if is_winner(board) or board_full(board):
            break

    display_board(board)

    if is_winner(board):
        prompt(f'The {detect_winner(board)} wins!')
        prompt('Play again? (y/n)')
        play_again = input().lower()
    else:
        prompt('It\'s a tie!')
        prompt('Play again? (y/n)')
        play_again = input().lower()

    while play_again not in 'yn' or not play_again:
        prompt('Please enter a valid input (\'y\' or \'n\').')
        prompt('Play again? (y/n)')
        play_again = input().lower()

    if play_again == 'y':
        tic_tac_toe()
    else:
        prompt('Thanks for playing!')

tic_tac_toe()