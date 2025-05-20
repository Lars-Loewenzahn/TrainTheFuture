import random

WORDS = [
    'python', 'programm', 'entwicklung', 'spiel', 'computer',
    'hangman', 'schule', 'lernen', 'algorithmus', 'funktion',
    'variable', 'liste', 'turtle', 'klasse', 'objekt', 'fenster',
    'grafik', 'zeichen', 'terminal', 'benutzer'
]

MAX_TRIES = 8


def print_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \/|\/
           |      |
           |     / \
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \/|\/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \/|\/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \/|\/
           |      
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \/|
           |      
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      
           |      
           |      
           -
        ''',
        '''
           --------
           |      |
           |      
           |      
           |      
           |      
           -
        ''',
        '''
           --------
           |      
           |      
           |      
           |      
           |      
           -
        '''
    ]
    print(stages[tries])

def main():
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()
    tries = MAX_TRIES
    print('Willkommen bei Hangman!')
    print('_ ' * len(word))
    while tries > 0:
        print_hangman(tries)
        print('Wort: ', end='')
        display = [letter if letter in guessed else '_' for letter in word]
        print(' '.join(display))
        print(f'Falsche Buchstaben: {", ".join(sorted(wrong))}')
        guess = input('Rate einen Buchstaben: ').lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print('Bitte gib genau einen Buchstaben ein.')
            continue
        if guess in guessed or guess in wrong:
            print('Diesen Buchstaben hast du schon geraten.')
            continue
        if guess in word:
            guessed.add(guess)
            print('Richtig!')
            if all(letter in guessed for letter in word):
                print(f'Glückwunsch, du hast das Wort "{word}" erraten!')
                break
        else:
            wrong.add(guess)
            tries -= 1
            print('Leider falsch.')
    else:
        print_hangman(0)
        print(f'Schade, du hast verloren! Das Wort war: {word}')

if __name__ == '__main__':
    main()
