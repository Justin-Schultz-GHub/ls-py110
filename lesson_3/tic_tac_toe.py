"""
My solo attempt at tic tac toe. I made it PvP instead of PvC. I definitely
think there's too much happening with all the if statements, especially in the
win checks, but I was already too far along to change how it worked at that
point and so I was commited to seeing it through.
"""

import os

VALID_CONTINUE = 'yn'

MAX_TURNS = 9

UNCHANGED_CELLS = [['_', '_', '_'], [' ', ' ', ' ']]

VALID_CELLS = [1, 2, 3]


def tic_tac_toe():
    r1_c1, r1_c2, r1_c3 = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
    r2_c1, r2_c2, r2_c3 = ['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']
    r3_c1, r3_c2, r3_c3 = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']

    divider = '|'

    turn = 0

    is_game_over = False


    def player1_win(r1_c1, r1_c2, r1_c3, r2_c1, r2_c2, r2_c3, r3_c1, r3_c2, r3_c3):
        if r1_c1[1] == 'X' and r1_c2[1] == 'X' and r1_c3[1] == 'X':
            return True
        elif r2_c1[1] == 'X' and r2_c2[1] == 'X' and r2_c3[1] == 'X':
            return True
        elif r3_c1[1] == 'X' and r3_c2[1] == 'X' and r3_c3[1] == 'X':
            return True
        elif r1_c1[1] == 'X' and r2_c1[1] == 'X' and r3_c1[1] == 'X':
            return True
        elif r1_c2[1] == 'X' and r2_c2[1] == 'X' and r3_c2[1] == 'X':
            return True
        elif r1_c3[1] == 'X' and r2_c3[1] == 'X' and r3_c3[1] == 'X':
            return True
        elif r1_c1[1] == 'X' and r2_c2[1] == 'X' and r3_c3[1] == 'X':
            return True
        elif r3_c1[1] == 'X' and r2_c2[1] == 'X' and r1_c3[1] == 'X':
            return True

        return False


    def player2_win(r1_c1, r1_c2, r1_c3, r2_c1, r2_c2, r2_c3, r3_c1, r3_c2, r3_c3):
        if r1_c1[1] == 'O' and r1_c2[1] == 'O' and r1_c3[1] == 'O':
            return True
        elif r2_c1[1] == 'O' and r2_c2[1] == 'O' and r2_c3[1] == 'O':
            return True
        elif r3_c1[1] == 'O' and r3_c2[1] == 'O' and r3_c3[1] == 'O':
            return True
        elif r1_c1[1] == 'O' and r2_c1[1] == 'O' and r3_c1[1] == 'O':
            return True
        elif r1_c2[1] == 'O' and r2_c2[1] == 'O' and r3_c2[1] == 'O':
            return True
        elif r1_c3[1] == 'O' and r2_c3[1] == 'O' and r3_c3[1] == 'O':
            return True
        elif r1_c1[1] == 'O' and r2_c2[1] == 'O' and r3_c3[1] == 'O':
            return True
        elif r3_c1[1] == 'O' and r2_c2[1] == 'O' and r1_c3[1] == 'O':
            return True

        return False

    def is_valid_choice(row, column):
        match row:
            case 1:
                if column == 1:
                    if r1_c1 in UNCHANGED_CELLS:
                        return True

                elif column == 2:
                    if r1_c2 in UNCHANGED_CELLS:
                        return True

                elif column == 3:
                    if r1_c3 in UNCHANGED_CELLS:
                        return True

                return False

            case 2:
                if column == 1:
                    if r2_c1 in UNCHANGED_CELLS:
                        return True

                elif column == 2:
                    if r2_c2 in UNCHANGED_CELLS:
                        return True

                elif column == 3:
                    if r2_c3 in UNCHANGED_CELLS:
                        return True

                return False

            case 3:
                if column == 1:
                    if r3_c1 in UNCHANGED_CELLS:
                        return True

                elif column == 2:
                    if r3_c2 in UNCHANGED_CELLS:
                        return True

                elif column == 3:
                    if r3_c3 in UNCHANGED_CELLS:
                        return True

                return False


    def update_board(row, column, marker):
        match row:
            case 1:
                if column == 1:
                    r1_c1[1] = marker
                elif column == 2:
                    r1_c2[1] = marker
                elif column == 3:
                    r1_c3[1] = marker

            case 2:
                if column == 1:
                    r2_c1[1] = marker
                elif column == 2:
                    r2_c2[1] = marker
                elif column == 3:
                    r2_c3[1] = marker

            case 3:
                if column == 1:
                    r3_c1[1] = marker
                elif column == 2:
                    r3_c2[1] = marker
                elif column == 3:
                    r3_c3[1] = marker

    while not is_game_over:
        os.system('clear')

        turn += 1
        print(f'Turn {turn}')

        player = 'Player 1' if turn % 2 == 1 else 'Player 2'
        marker = 'X' if turn % 2 == 1 else 'O'

        row1 = ''.join(r1_c1) + divider + ''.join(r1_c2) + divider + ''.join(r1_c3)
        row2 = ''.join(r2_c1) + divider + ''.join(r2_c2) + divider + ''.join(r2_c3)
        row3 = ''.join(r3_c1) + divider + ''.join(r3_c2) + divider + ''.join(r3_c3)

        board = row1 + '\n' + row2 + '\n' + row3

        print('The current board state is: ')
        print(board)

        row = int(input(f'{player}, enter a row (1-3): '))
        column = int(input(f'{player}, enter a column (1-3): '))

        while row not in VALID_CELLS or column not in VALID_CELLS:
            os.system('clear')
            print(board)

            print('Please enter a valid row and cell.')
            row = int(input(f'{player}, enter a row (1-3): '))
            column = int(input(f'{player}, enter a column (1-3): '))

        while not is_valid_choice(row, column):
            print('This cell has already been taken. Please enter a valid cell.')
            row = int(input(f'{player}, enter a row (1-3): '))
            column = int(input(f'{player}, enter a column (1-3): '))

        update_board(row, column, marker)

        row1 = ''.join(r1_c1) + divider + ''.join(r1_c2) + divider + ''.join(r1_c3)
        row2 = ''.join(r2_c1) + divider + ''.join(r2_c2) + divider + ''.join(r2_c3)
        row3 = ''.join(r3_c1) + divider + ''.join(r3_c2) + divider + ''.join(r3_c3)

        board = row1 + '\n' + row2 + '\n' + row3

        if player1_win(r1_c1, r1_c2, r1_c3, r2_c1, r2_c2, r2_c3, r3_c1, r3_c2, r3_c3):
            os.system('clear')
            print('Player 1 wins!')
            print(board)
            is_game_over = True
        elif player2_win(r1_c1, r1_c2, r1_c3, r2_c1, r2_c2, r2_c3, r3_c1, r3_c2, r3_c3):
            os.system('clear')
            print('Player 2 wins!')
            print(board)
            is_game_over = True
        elif turn == MAX_TURNS:
            os.system('clear')
            print(board)
            print('All squares are filled! It\'s a tie!')
            is_game_over = True

    play_again = input('Play again? (y/n): ').lower()

    while play_again not in VALID_CONTINUE:
        play_again = input('Please enter a valid input (y/n): ').lower()

    if play_again == 'y':
        tic_tac_toe()
    else:
        print('Thanks for playing!')

tic_tac_toe()
