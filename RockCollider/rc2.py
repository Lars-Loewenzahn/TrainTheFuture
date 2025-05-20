import pygame
import random
import math

# Initialisieren
pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Schwarmverhalten")
BACKGROUND_COLOR = (0, 0, 0)

COLORS = {
    "p": (255, 255, 0),
    "s": (255, 0, 0),
    "r": (0, 0, 255)
}
SHAPES = {
    "p": "square",
    "s": "triangle",
    "r": "circle"
}

# Schwarmparameter
SEPARATION_DIST = 50
NEIGHBOR_RADIUS = 50
MAX_SPEED = 3
ALIGNMENT_WEIGHT = 0.05
COHESION_WEIGHT = 0.01
SEPARATION_WEIGHT = 0.1

class GameObject:
    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.color = COLORS[kind]
        self.shape = SHAPES[kind]
        self.radius = 8
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def update_kind(self, kind):
        self.kind = kind
        self.color = COLORS[kind]
        self.shape = SHAPES[kind]

    def move(self, neighbors):
        ax, ay = 0, 0

        avg_vx, avg_vy = 0, 0
        center_x, center_y = 0, 0
        separate_x, separate_y = 0, 0
        total = 0

        for other in neighbors:
            if other is self:
                continue
            if other.kind != self.kind:
                continue  # <--- Nur gleichartige berücksichtigen!

            dist = distance(self, other)
            if dist < NEIGHBOR_RADIUS:
                total += 1
                avg_vx += other.vx
                avg_vy += other.vy
                center_x += other.x
                center_y += other.y
                if dist < SEPARATION_DIST:
                    dx = self.x - other.x
                    dy = self.y - other.y
                    if dist > 0:
                        separate_x += dx / dist
                        separate_y += dy / dist

        if total > 0:
            avg_vx /= total
            avg_vy /= total
            center_x /= total
            center_y /= total

            ax += (avg_vx - self.vx) * ALIGNMENT_WEIGHT
            ay += (avg_vy - self.vy) * ALIGNMENT_WEIGHT
            ax += (center_x - self.x) * COHESION_WEIGHT
            ay += (center_y - self.y) * COHESION_WEIGHT
            ax += separate_x * SEPARATION_WEIGHT
            ay += separate_y * SEPARATION_WEIGHT

        self.vx += ax
        self.vy += ay

        speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
        if speed > MAX_SPEED:
            self.vx = self.vx / speed * MAX_SPEED
            self.vy = self.vy / speed * MAX_SPEED

        self.x += self.vx
        self.y += self.vy

        # Randkollision
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1


        self.vx += ax
        self.vy += ay

        # Geschwindigkeit begrenzen
        speed = math.sqrt(self.vx ** 2 + self.vy ** 2)
        if speed > MAX_SPEED:
            self.vx = self.vx / speed * MAX_SPEED
            self.vy = self.vy / speed * MAX_SPEED

        self.x += self.vx
        self.y += self.vy

        # Randkollision
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

    def draw(self, surface):
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

def distance(obj1, obj2):
    return math.sqrt((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2)

# Objekte erzeugen
objects = [GameObject(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.choice(["p", "r", "s"])) for _ in range(100)]

# Hauptschleife
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for obj in objects:
        obj.move(objects)
        obj.draw(screen)

    # Kollisionslogik
    for i in range(len(objects)):
        for j in range(i + 1, len(objects)):
            if distance(objects[i], objects[j]) < 2 * objects[i].radius:
                collide(objects[i], objects[j])

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
