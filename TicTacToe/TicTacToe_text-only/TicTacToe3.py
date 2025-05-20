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

import math

def minimax(board, depth, is_max):
    if check_win(board, 'o'):
        return 10 - depth
    if check_win(board, 'x'):
        return depth - 10
    if check_draw(board):
        return 0
    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] not in ['x','o']:
                board[i] = 'o'
                score = minimax(board, depth+1, False)
                board[i] = str(i+1)
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] not in ['x','o']:
                board[i] = 'x'
                score = minimax(board, depth+1, True)
                board[i] = str(i+1)
                best = min(best, score)
        return best

def best_move(board):
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] not in ['x','o']:
            board[i] = 'o'
            score = minimax(board, 0, False)
            board[i] = str(i+1)
            if score > best_score:
                best_score = score
                move = i
    return move

def tictactoe():
    board = ['1','2','3','4','5','6','7','8','9']
    # Computer macht den ersten Zug
    move = best_move(board)
    board[move] = 'o'
    print(f"Computer startet auf Feld {move+1}.")
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
        comp_move = best_move(board)
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