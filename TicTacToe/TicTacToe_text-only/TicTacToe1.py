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

def tictactoe():
    board = ['1','2','3','4','5','6','7','8','9']
    current = 'x'
    while True:
        print_board(board)
        move = input(f"Spieler {current}, wähle Feld (1-9): ")
        if move not in '123456789' or board[int(move)-1] in ['x','o']:
            print('Ungültiger Zug!')
            continue
        board[int(move)-1] = current
        if check_win(board, current):
            print_board(board)
            print(f'Spieler {current} gewinnt!')
            break
        if check_draw(board):
            print_board(board)
            print('Unentschieden!')
            break
        current = 'o' if current == 'x' else 'x'

if __name__ == '__main__':
    tictactoe()
