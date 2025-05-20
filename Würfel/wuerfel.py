import turtle
import random

# Fenster und Turtle einrichten
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
turtle.title('Turtle Würfel')

wn = turtle.Screen()
wn.setup(400, 400)

text_t = turtle.Turtle()
text_t.hideturtle()
text_t.penup()

# Würfelpunkte-Positionen
DOTS = {
    1: [(0, 0)],
    2: [(-30, 30), (30, -30)],
    3: [(-30, 30), (0, 0), (30, -30)],
    4: [(-30, 30), (30, 30), (-30, -30), (30, -30)],
    5: [(-30, 30), (30, 30), (0, 0), (-30, -30), (30, -30)],
    6: [(-30, 30), (30, 30), (-30, 0), (30, 0), (-30, -30), (30, -30)]
}

def draw_die(number):
    t.clear()
    t.penup()
    t.goto(-50, 50)
    t.pendown()
    t.pensize(3)
    t.color('black')
    for _ in range(4):
        t.forward(100)
        t.right(90)
    # Punkte zeichnen
    t.penup()
    t.color('black')
    for x, y in DOTS[number]:
        t.goto(x, y)
        t.dot(20, 'black')
    # Zahl anzeigen
    t.goto(0, -80)
    t.color('blue')
    t.write(f'{number}', align='center', font=('Arial', 28, 'bold'))

def show_text(msg):
    text_t.clear()
    text_t.goto(0, 120)
    text_t.color('red')
    text_t.write(msg, align='center', font=('Arial', 18, 'bold'))

def roll(x=None, y=None):
    number = random.randint(1, 6)
    draw_die(number)
    show_text('Click me')

def main():
    wn.tracer(0)
    roll()  # Erster Wurf
    wn.onclick(roll)
    wn.mainloop()

if __name__ == '__main__':
    main()
