from turtle import *

# Setting up the turtle
def setup_turtles():
    global t , t2
    t = Turtle()
    t.speed(0)
    t.width(5)
    t.color("gray")
    t.penup()
    t.hideturtle()
    t2 = Turtle()
    t2.speed(0)
    t2.width(10)
    t2.color("purple")
    t2.penup()
    t2.hideturtle()

def draw_field():
    t.width(5)
    t.color("gray")
    t.penup()
    t.goto(-150, 50)
    t.pendown()
    t.goto(150, 50)
    t.penup()
    t.goto(-150,-50)
    t.pendown()
    t.goto(150, -50)
    t.penup()
    t.goto(50, -150)
    t.pendown()
    t.goto(50, 150)
    t.penup()
    t.goto(-50, 150)
    t.pendown()
    t.goto(-50, -150)
    t.penup()

def draw_cross_r(x,y): # This uses turtle forward and backward
    t2.goto(x,y)
    t2.setheading(45)
    t2.pendown()
    t2.forward(42)
    t2.backward(84)
    t2.forward(42)
    t2.left(90)
    t2.forward(42)
    t2.backward(84)
    t2.penup()

def draw_cross_d(x,y):
    t2.goto(x-40, y+40)
    t2.pendown()
    t2.goto(x+40, y-40)
    t2.penup()
    t2.goto(x+40, y+40)
    t2.pendown()
    t2.goto(x-40, y-40)
    t2.penup()

def draw_circle(x,y):
    t2.goto(x,y-40)
    t2.pendown()
    t2.circle(40)
    t2.penup()

def clean_value(x):
    if x in range(-150, -50):
        x = -100
    elif x in range(-50, 50):
        x = 0
    elif x in range(50, 150):
        x  = 100
    return x



def write_field(x,y, player):
    global feld
    if x == -100 and y == 100:
        if feld[0][0] == " ":
            feld[0][0] = player
            return True
        else:
            return False
    if x == 0 and y == 100:
        if feld[0][1] == " ":
            feld[0][1] = player
            return True
        else:
            return False
    if x == 100 and y == 100:
        if feld[0][2] == " ":
            feld[0][2] = player
            return True
        else:
            return False

    if x == -100 and y == 0:
        if feld[1][0] == " ":
            feld[1][0] = player
            return True
        else:
            return False
    if x == 0 and y == 0:
        if feld[1][1] == " ":
            feld[1][1] = player
            return True
        else:
            return False
    if x == 100 and y == 0:
        if feld[1][2] == " ":
            feld[1][2] = player
            return True
        else:
            return False
    if x == -100 and y == -100:
        if feld[2][0] == " ":
            feld[2][0] = player
            return True
        else:
            return False
    if x == 0 and y == -100:
        if feld[2][1] == " ":
            feld[2][1] = player
            return True
        else:
            return False
    if x == 100 and y == -100:
        if feld[2][2] == " ":
            feld[2][2] = player
            return True
        else:
            return False

def check_win_turtle():
    # Zeilen, Spalten, Diagonalen prüfen
    for i in range(3):
        if feld[i][0] == feld[i][1] == feld[i][2] != " ":
            return feld[i][0]
        if feld[0][i] == feld[1][i] == feld[2][i] != " ":
            return feld[0][i]
    if feld[0][0] == feld[1][1] == feld[2][2] != " ":
        return feld[0][0]
    if feld[0][2] == feld[1][1] == feld[2][0] != " ":
        return feld[0][2]
    return None

def check_draw_turtle():
    for row in feld:
        for cell in row:
            if cell == " ":
                return False
    return True

game_over = False

import math

def feld_to_list():
    # Wandelt das 3x3 feld in eine 1D-Liste um
    return [feld[i][j] for i in range(3) for j in range(3)]

def list_to_feld(lst):
    # Wandelt eine 1D-Liste zurück in das 3x3 feld
    for i in range(3):
        for j in range(3):
            feld[i][j] = lst[i*3+j]

def minimax(board, depth, is_max):
    # board: 1D-Liste
    def check_win(board, player):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        for line in wins:
            if all(board[i]==player for i in line):
                return True
        return False
    def check_draw(board):
        return all(cell in ['x','o'] for cell in board)
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

def computer_move():
    global game_over, player
    board = feld_to_list()
    move = best_move(board)
    if move == -1:
        return
    board[move] = 'o'
    list_to_feld(board)
    # Zeichne Kreis an die richtige Stelle
    pos = [( -100, 100), (0, 100), (100, 100),
           (-100, 0),   (0, 0),   (100, 0),
           (-100,-100), (0, -100), (100, -100)]
    x, y = pos[move]
    draw_circle(x, y)
    winner = check_win_turtle()
    if winner:
        t2.goto(-140, 0)
        t2.color("red")
        t2.write(f"Spieler {winner} gewinnt!", font=("Arial", 24, "bold"))
        game_over = True
        return
    elif check_draw_turtle():
        t2.goto(-100, 0)
        t2.color("blue")
        t2.write("Unentschieden!", font=("Arial", 24, "bold"))
        game_over = True
        return
    player = "x"

def screen_clicked(x,y):
    global player, game_over
    if game_over:
        return
    x = clean_value(x)
    y = clean_value(y)
    if player == "x":
        if write_field(x,y, player):
            draw_cross_d(x,y)
            winner = check_win_turtle()
            if winner:
                t2.goto(-140, 0)
                t2.color("red")
                t2.write(f"Spieler {winner} gewinnt!", font=("Arial", 24, "bold"))
                game_over = True
                return
            elif check_draw_turtle():
                t2.goto(-100, 0)
                t2.color("blue")
                t2.write("Unentschieden!", font=("Arial", 24, "bold"))
                game_over = True
                return
            player = "o"
            computer_move()
        else:
            t2.goto(-180, -180)
            t2.color("orange")
            t2.write("Feld belegt!", font=("Arial", 16, "normal"))
            t2.clear()


player = "x"
feld = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]
setup_turtles()
draw_field()
# draw_cross_d(0,100)
# draw_circle(0,0)

# Computer macht den ersten Zug
computer_move()

scr = t.getscreen()
scr.listen()
scr.onclick(screen_clicked)

mainloop()
