def print_board(board):
    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---+---+---')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---+---+---')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()

def check_win(board, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diags
    ]
    for line in wins:
        if all(board[i] == player for i in line):
            return True
    return False

def check_draw(board):
    return all(cell in ['x', 'o'] for cell in board)

import random

def tictactoe():
    board = ['1','2','3','4','5','6','7','8','9']
    while True:
        print_board(board)
        # Spielerzug
        move = input("Dein Zug (x), Feld (1-9): ")
        if move not in '123456789' or board[int(move)-1] in ['x','o']:
            print('Ungültiger Zug!')
            continue
        board[int(move)-1] = 'x'
        if check_win(board, 'x'):
            print_board(board)
            print('Du gewinnst!')
            break
        if check_draw(board):
            print_board(board)
            print('Unentschieden!')
            break
        # Computerzug
        free = [i for i, cell in enumerate(board) if cell not in ['x', 'o']]
        if free:
            comp_move = random.choice(free)
            board[comp_move] = 'o'
            print(f"Computer setzt auf Feld {comp_move+1}.")
            if check_win(board, 'o'):
                print_board(board)
                print('Computer gewinnt!')
                break
            if check_draw(board):
                print_board(board)
                print('Unentschieden!')
                break

if __name__ == '__main__':
    tictactoe()