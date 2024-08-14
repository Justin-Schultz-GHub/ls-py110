import os
import random

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'
PLAYERS = ['Player', 'Computer']

WINNING_LINES = [
                    [1, 2, 3], [4, 5, 6], [7, 8, 9], # rows

                    [1, 4, 7], [2, 5, 8], [3, 6, 9],# columns

                    [1, 5, 9], [3, 5, 7], # diagonals
                ]


def find_player1():
    prompt('Choose who will go first (1. Player, 2. Computer, 3. Random): ')
    player1 = input()

    while player1 not in '123':
        prompt('Please input a valid choice (1. Player, 2. Computer, 3. Random): ')
        player1 = input()

    match player1:
        case '1':
            return 'Player'
        case '2':
            return 'Computer'
        case '3':
            return 'Random'

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
    square = find_vulnerable_square(board)
    if square:
        board[square] = COMPUTER_MARKER
        print(square)

    elif empty_squares(board):
        square = random.choice(empty_squares(board))

        board[square] = COMPUTER_MARKER

def find_vulnerable_square(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

        markers = [board[sq1], board[sq2], board[sq3]]

        if markers.count(COMPUTER_MARKER) == 2 and markers.count(INITIAL_MARKER) == 1:
            return line[markers.index(INITIAL_MARKER)]

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

        markers = [board[sq1], board[sq2], board[sq3]]

        if markers.count(PLAYER_MARKER) == 2 and markers.count(INITIAL_MARKER) == 1:
            return line[markers.index(INITIAL_MARKER)]

    if board[5] == INITIAL_MARKER:
        return 5

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

        markers = [board[sq1], board[sq2], board[sq3]]

        if markers.count(COMPUTER_MARKER) >= 1 and markers.count(PLAYER_MARKER) == 0:
            return line[markers.index(INITIAL_MARKER)]

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

        markers = [board[sq1], board[sq2], board[sq3]]

        if markers.count(COMPUTER_MARKER) == 2 and markers.count(PLAYER_MARKER) == 0:
            return line[markers.index(INITIAL_MARKER)]

    return None

def is_winner(board):
    return bool(detect_winner(board))


def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

        if (board[sq1] == PLAYER_MARKER
                and board[sq2] == PLAYER_MARKER
                and board[sq3] == PLAYER_MARKER):

            return 'Player'
        if (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):

            return 'Computer'

    return None


def board_full(board):
    return len(empty_squares(board)) == 0


def tic_tac_toe():
    board = initialize_board()

    player1 = find_player1()
    player2 = random.choice(PLAYERS)

    if player1 not in PLAYERS:
        player1 = random.choice(PLAYERS)

        while player1 == player2:
            player1 = random.choice(PLAYERS)

    while player2 == player1:
        player2 = random.choice(PLAYERS)

        while player2 == player1:
            player2 = random.choice(PLAYERS)

    while True:
        display_board(board)

        if player1 == PLAYERS[0]:
            player_choice(board)

            if is_winner(board) or board_full(board):
                break

            computer_choice(board)

            if is_winner(board) or board_full(board):
                break
        if player1 == PLAYERS[1]:
            computer_choice(board)

            if is_winner(board) or board_full(board):
                break

            display_board(board)
            player_choice(board)

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