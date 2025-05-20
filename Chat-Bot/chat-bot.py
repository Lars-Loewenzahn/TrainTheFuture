def antwort(text):
    text = text.lower()
    if 'hallo' in text or 'hi' in text:
        return 'Hallo! Wie kann ich dir helfen?'
    elif 'hilfe' in text:
        return 'Ich bin ein einfacher Chatbot. Frag mich nach dem Wetter oder sag Hallo!'
    elif 'wetter' in text:
        return 'Das Wetter ist heute schön!'
    elif 'tschüss' in text or 'bye' in text or 'auf wiedersehen' in text:
        return 'Tschüss! Bis zum nächsten Mal.'
    else:
        return 'Das habe ich leider nicht verstanden.'

def main():
    print('Willkommen beim einfachen Chatbot! ("tschüss" zum Beenden)')
    while True:
        user = input('Du: ')
        bot = antwort(user)
        print('Bot:', bot)
        if 'tschüss' in user.lower() or 'bye' in user.lower() or 'auf wiedersehen' in user.lower():
            break

if __name__ == '__main__':
    main()
