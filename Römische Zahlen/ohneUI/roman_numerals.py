def int_to_roman(num):
    roman_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100,  'C'), (90,  'XC'), (50,  'L'), (40,  'XL'),
        (10,   'X'), (9,   'IX'), (5,   'V'), (4,   'IV'),
        (1,    'I')
    ]
    result = ""
    for (value, symbol) in roman_map:
        while num >= value:
            result += symbol
            num -= value
    return result

def roman_to_int(s):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0
    for char in reversed(s.upper()):
        value = roman_map[char]
        if value < prev_value:
            result -= value
        else:
            result += value
            prev_value = value
    return result

# ==== Testbereich ====
if __name__ == "__main__":
    print("Wähle eine Richtung:")
    print("1: Arabisch → Römisch")
    print("2: Römisch → Arabisch")
    wahl = input("Deine Wahl: ")

    if wahl == "1":
        zahl = int(input("Gib eine Zahl zwischen 1 und 3999 ein: "))
        if 1 <= zahl <= 3999:
            print("Römisch:", int_to_roman(zahl))
        else:
            print("Ungültiger Bereich.")
    elif wahl == "2":
        römisch = input("Gib eine römische Zahl ein: ")
        try:
            print("Arabisch:", roman_to_int(römisch))
        except KeyError:
            print("Ungültige römische Zahl.")
    else:
        print("Ungültige Eingabe.")
