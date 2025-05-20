import pygame
import random
import math

# Initialisieren von Pygame
pygame.init()

# Fenstergröße und Farben definieren
WIDTH, HEIGHT = 500, 500
BACKGROUND_COLOR = (0, 0, 0)
COLORS = {
    "p": (255, 255, 0),  # Gelb
    "s": (255, 0, 0),    # Rot
    "r": (0, 0, 255)     # Blau
}
SHAPES = {
    "p": "square",
    "s": "triangle",
    "r": "circle"
}

# Bildschirm erstellen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Collision")

# Klasse für die Objekte
class GameObject:
    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.color = COLORS[kind]
        self.shape = SHAPES[kind]
        self.radius = 10
        self.speed = random.uniform(2, 4)
        self.direction = random.uniform(0, 2 * math.pi)

    def update_kind(self, kind):
        self.kind = kind
        self.color = COLORS[kind]
        self.shape = SHAPES[kind]

    def move(self):
        # Bewegung berechnen
        self.x += math.cos(self.direction) * self.speed
        self.y += math.sin(self.direction) * self.speed

        # Bildschirmrandkollision
        if self.x <= 0 or self.x >= WIDTH:
            self.direction = math.pi - self.direction
        if self.y <= 0 or self.y >= HEIGHT:
            self.direction = -self.direction

    def draw(self, surface):
        # Objekt zeichnen
        if self.shape == "circle":
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        elif self.shape == "square":
            pygame.draw.rect(surface, self.color, (int(self.x) - self.radius, int(self.y) - self.radius, 2 * self.radius, 2 * self.radius))
        elif self.shape == "triangle":
            points = [
                (int(self.x), int(self.y) - self.radius),
                (int(self.x) - self.radius, int(self.y) + self.radius),
                (int(self.x) + self.radius, int(self.y) + self.radius)
            ]
            pygame.draw.polygon(surface, self.color, points)

# Kollisionsfunktion
def collide(obj1, obj2):
    combo = obj1.kind + obj2.kind
    result = {
        "rs": "r",
        "sr": "r",
        "rp": "p",
        "pr": "p",
        "sp": "s",
        "ps": "s"
    }
    if combo in result:
        new_kind = result[combo]
        obj1.update_kind(new_kind)
        obj2.update_kind(new_kind)

# Abstand zwischen zwei Objekten berechnen
def distance(obj1, obj2):
    return math.sqrt((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2)

# Objekte initialisieren
kinds = ["p", "r", "s"]
objects = []
for i in range(100):
    obj = GameObject(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.choice(kinds))
    objects.append(obj)

# Hauptspiel-Schleife
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BACKGROUND_COLOR)

    # Ereignisse prüfen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Objekte bewegen und zeichnen
    for obj in objects:
        obj.move()
        obj.draw(screen)

    # Kollisionen prüfen
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            if distance(objects[i], objects[j]) <= 20:
                collide(objects[i], objects[j])

    # Bildschirm aktualisieren
    pygame.display.flip()
    clock.tick(12)

pygame.quit()
