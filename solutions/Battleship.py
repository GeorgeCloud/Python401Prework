from random import *

board = []

ship_row = randrange(5)
ship_col = randrange(5)

for x in range(0, 5):
    board.append(['O'] * 5)

def print_board(board):
    for row in board:
        print ' '.join(row)

print_board(board)

print 'Boat Location (Debugger) = Row: {0}, Column: {1}'.format(ship_row, ship_col)

for turn in range(4):
    print 'Turn', turn + 1
    guess_row = int(raw_input('Guess Row: '))
    guess_col = int(raw_input('Guess Col: '))

    if guess_row == ship_row and guess_col == ship_col:
        print 'Congratulations! You sank my battleship!'
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print 'Oops, that\'s not even in the ocean.'
        elif board[guess_row][guess_col] == 'X':
            print 'You guessed that one already.'
        else:
            print 'You missed my battleship!'
            board[guess_row][guess_col] = 'X'
            if (turn == 3):
                print 'Game Over'
        print_board(board)
