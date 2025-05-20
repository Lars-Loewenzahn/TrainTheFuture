import math

print("loaded")
# --- Flächen und Umfänge ---
class rechteck:
    def __init__(self, **kwargs):
        self._a = kwargs.get('a')
        self._b = kwargs.get('b')
        self._flaecheninhalt = kwargs.get('flaecheninhalt')
        self._umfang = kwargs.get('umfang')

    def seite_a(self):
        if self._flaecheninhalt is not None and self._b is not None:
            return self._flaecheninhalt / self._b
        elif self._umfang is not None and self._b is not None:
            return (self._umfang / 2) - self._b
        return None
    def seite_b(self):
        if self._flaecheninhalt is not None and self._a is not None:
            return self._flaecheninhalt / self._a
        elif self._umfang is not None and self._a is not None:
            return (self._umfang / 2) - self._a
        return None
    def flaeche(self):
        if self._a is not None and self._b is not None:
            return self._a * self._b
        return None
    def umfang_(self):
        if self._a is not None and self._b is not None:
            return 2 * (self._a + self._b)
        return None
    
    @staticmethod
    def flaecheninhalt(a, b):
        return a * b
    @staticmethod
    def umfang(a, b):
        return 2 * (a + b)

class quadrat:
    def __init__(self, **kwargs):
        self._a = kwargs.get('a')
        self._flaecheninhalt = kwargs.get('flaecheninhalt')
        self._umfang = kwargs.get('umfang')
    @staticmethod
    def flaecheninhalt(a):
        return a * a
    @staticmethod
    def umfang(a):
        return 4 * a
    def seite(self):
        if self._flaecheninhalt is not None:
            return math.sqrt(self._flaecheninhalt)
        elif self._umfang is not None:
            return self._umfang / 4
        return None
    def flaeche(self):
        if self._a is not None:
            return self._a ** 2
        return None
    def umfang_(self):
        if self._a is not None:
            return 4 * self._a
        return None

class dreieck:
    def __init__(self, **kwargs):
        self._a = kwargs.get('a')
        self._h = kwargs.get('h')
        self._flaecheninhalt = kwargs.get('flaecheninhalt')
        self._b = kwargs.get('b')
        self._c = kwargs.get('c')
        self._umfang = kwargs.get('umfang')
    @staticmethod
    def flaecheninhalt(a, h):
        return (a * h) / 2
    @staticmethod
    def umfang(a, b, c):
        return a + b + c
    def grundseite(self):
        if self._flaecheninhalt is not None and self._h is not None:
            return 2 * self._flaecheninhalt / self._h
        return None
    def hoehe(self):
        if self._flaecheninhalt is not None and self._a is not None:
            return 2 * self._flaecheninhalt / self._a
        return None
    def seite_b(self):
        if self._umfang is not None and self._a is not None and self._c is not None:
            return self._umfang - self._a - self._c
        return None
    def seite_c(self):
        if self._umfang is not None and self._a is not None and self._b is not None:
            return self._umfang - self._a - self._b
        return None
    def flaeche(self):
        if self._a is not None and self._h is not None:
            return (self._a * self._h) / 2
        return None
    def umfang_(self):
        if self._a is not None and self._b is not None and self._c is not None:
            return self._a + self._b + self._c
        return None

class kreis:
    def __init__(self, **kwargs):
        self._r = kwargs.get('radius')
        self._a = kwargs.get('flaecheninhalt')
        self._u = kwargs.get('umfang')

    def radius_von_flaeche(self):
        if self._a is not None:
            return math.sqrt(self._a / math.pi)
        return None

    def radius_von_umfang(self):
        if self._u is not None:
            return self._u / (2 * math.pi)
        return None

    def flaeche(self):
        if self._r is not None:
            return math.pi * self._r * self._r
        return None

    def umfang(self):
        if self._r is not None:
            return 2 * math.pi * self._r
        return 3

    @staticmethod
    def umfang_von_radius(r):
        return 2 * math.pi * r

    @staticmethod
    def flaecheninhalt(r):
        return math.pi * r * r

class trapez:
    def __init__(self, **kwargs):
        self._a = kwargs.get('a')
        self._b = kwargs.get('b')
        self._h = kwargs.get('h')
        self._flaecheninhalt = kwargs.get('flaecheninhalt')
    @staticmethod
    def flaecheninhalt(a, b, h):
        return ((a + b) * h) / 2
    def hoehe(self):
        if self._flaecheninhalt is not None and self._a is not None and self._b is not None:
            return 2 * self._flaecheninhalt / (self._a + self._b)
        return None
    def seite_a(self):
        if self._flaecheninhalt is not None and self._b is not None and self._h is not None:
            return (2 * self._flaecheninhalt / self._h) - self._b
        return None
    def seite_b(self):
        if self._flaecheninhalt is not None and self._a is not None and self._h is not None:
            return (2 * self._flaecheninhalt / self._h) - self._a
        return None
    def flaeche(self):
        if self._a is not None and self._b is not None and self._h is not None:
            return ((self._a + self._b) * self._h) / 2
        return None

class parallelogramm:
    @staticmethod
    def flaecheninhalt(a, h):
        return a * h
    @staticmethod
    def umfang(a, b):
        return 2 * (a + b)

class raute:
    @staticmethod
    def flaecheninhalt(e, f):
        return (e * f) / 2
    @staticmethod
    def umfang(a):
        return 4 * a

# --- Prozentrechnung ---
def prozentwert(p, G):
    return (p / 100) * G

def prozentsatz(W, G):
    return (W / G) * 100

def grundwert(W, p):
    return W * 100 / p

# --- Bruchrechnung ---
def bruch_addieren(a, b, c, d):
    # a/b + c/d
    return (a*d + c*b, b*d)

def bruch_multiplizieren(a, b, c, d):
    # a/b * c/d
    return (a*c, b*d)

# --- Pythagoras ---
def pythagoras_a(c, b):
    return math.sqrt(c**2 - b**2)

def pythagoras_b(c, a):
    return math.sqrt(c**2 - a**2)

def pythagoras_c(a, b):
    return math.sqrt(a**2 + b**2)

# --- Zinsrechnung ---
def zinsen(K, p, t):
    # K = Kapital, p = Zinssatz (%), t = Zeit in Jahren
    return K * p * t / 100

# --- Dreisatz ---
def dreisatz(a1, b1, a2):
    # a1 verhält sich zu b1 wie a2 zu x
    return b1 * a2 / a1

# --- Einheitenumrechnung ---
def cm2_to_m2(cm2):
    return cm2 / 10000

def m2_to_cm2(m2):
    return m2 * 10000

def l_to_ml(l):
    return l * 1000

def ml_to_l(ml):
    return ml / 1000

# --- Weitere nützliche Formeln ---
def mittelwert(liste):
    return sum(liste) / len(liste)

def summe_arithm_reihe(a1, an, n):
    return n * (a1 + an) / 2

def summe_geometr_reihe(a1, q, n):
    return a1 * (1 - q**n) / (1 - q)

# --- Physik: Geschwindigkeit, Dichte, Kraft ---
def geschwindigkeit(s, t):
    return s / t

def dichte(m, V):
    return m / V

def kraft(m, a):
    return m * a
