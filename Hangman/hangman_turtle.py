import turtle
import random


WORDS = [
    'python', 'programm', 'entwicklung', 'spiel', 'computer',
    'hangman', 'schule', 'lernen', 'algorithmus', 'funktion',
    'variable', 'liste', 'turtle', 'klasse', 'objekt', 'fenster',
    'grafik', 'zeichen', 'terminal', 'benutzer'
]

MAX_TRIES = 8

wn = turtle.Screen()
wn.title('Turtle Hangman')
wn.setup(600, 400)
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(3)

text_t = turtle.Turtle()
text_t.hideturtle()
text_t.penup()

def draw_gallows():
    t.clear()
    t.penup()
    t.goto(-150, -100)
    t.pendown()
    t.forward(100)
    t.backward(50)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(30)
    t.penup()
    t.home()
    t.setheading(0)

def draw_hangman(tries):
    parts = [
        lambda: (t.penup(), t.goto(0, 70), t.pendown(), t.circle(20)), # Kopf
        lambda: (t.penup(), t.goto(0, 70), t.right(90), t.pendown(), t.forward(60)), # Körper
        lambda: (t.penup(), t.goto(0, 40), t.right(45), t.pendown(), t.forward(35)), # rechter Arm
        lambda: (t.penup(), t.goto(0, 40), t.setheading(225), t.pendown(), t.forward(35)), # linker Arm
        lambda: (t.penup(), t.goto(0, 10), t.setheading(315), t.pendown(), t.forward(35)), # rechtes Bein
        lambda: (t.penup(), t.goto(0, 10), t.setheading(225), t.pendown(), t.forward(35)), # linkes Bein
        lambda: (t.penup(), t.goto(-7, 85), t.setheading(0), t.pendown(), t.circle(3)), # rechtes Auge
        lambda: (t.penup(), t.goto(7, 85), t.setheading(0), t.pendown(), t.circle(3)), # linkes Auge
    ]
    draw_gallows()
    for i in range(MAX_TRIES - tries):
        parts[i]()
    t.penup()
    t.home()
    t.setheading(0)

def show_word(word, guessed):
    text_t.clear()
    text_t.goto(0, -140)
    display = ' '.join([letter if letter in guessed else '_' for letter in word])
    text_t.color('black')
    text_t.write(display, align='center', font=('Arial', 28, 'bold'))

def show_message(msg, color='red'):
    text_t.goto(0, 120)
    text_t.color(color)
    text_t.write(msg, align='center', font=('Arial', 20, 'bold'))

def main():
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()
    tries = MAX_TRIES
    state = {'done': False}

    draw_gallows()
    show_word(word, guessed)
    text_t.goto(0, 90)
    text_t.color('blue')
    text_t.write('Drücke eine Taste, um zu raten!', align='center', font=('Arial', 14, 'normal'))

    def on_keypress(key):
        if state['done']:
            return
        text_t.clear()
        letter = key.lower()
        if not letter.isalpha() or len(letter) != 1:
            show_message('Bitte einen einzelnen Buchstaben!', 'orange')
            return
        if letter in guessed or letter in wrong:
            show_message('Schon geraten!', 'orange')
            return
        if letter in word:
            guessed.add(letter)
            show_message(f'Richtig: {letter}', 'green')
            if all(l in guessed for l in word):
                show_word(word, guessed)
                show_message(f'Gewonnen! Das Wort war: {word}', 'green')
                state['done'] = True
                return
        else:
            wrong.add(letter)
            nonlocal tries
            tries -= 1
            show_message(f'Falsch: {letter}', 'red')
            if tries == 0:
                draw_hangman(tries)
                show_word(word, guessed)
                show_message(f'Verloren! Das Wort war: {word}', 'red')
                state['done'] = True
                return
        draw_hangman(tries)
        show_word(word, guessed)
        text_t.goto(0, 90)
        text_t.color('blue')
        text_t.write(f'Falsche Buchstaben: {", ".join(sorted(wrong))}', align='center', font=('Arial', 14, 'normal'))

    # Turtle-event: Tastendruck abfangen (ohne Umlaute, da diese zu Fehlern führen)
    for char in 'abcdefghijklmnopqrstuvwxyz':
        wn.onkey(lambda c=char: on_keypress(c), char)
        wn.onkey(lambda c=char: on_keypress(c), char.upper())
    wn.listen()
    wn.mainloop()

if __name__ == '__main__':
    main()
