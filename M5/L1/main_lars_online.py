from pygame import * 

window = display.set_mode((700,500))

display.set_caption("Catch")

background = transform.scale(image.load("M5/L1/background.png"), (700, 500))

x1, y1 = (100, 300)
x2, y2 = (100, 100)
speed = 10
FPS = 60

sprite1 = transform.scale(image.load('M5/L1/sprite1.png'), (100, 100))
sprite2 = transform.scale(image.load("M5/L1/sprite2.png"), (100, 100))
window.blit(background, (0,0))

game = True

clock = time.Clock()

while game:
    window.blit(background, (0,0))

    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False
        
    keys_pressed = key.get_pressed()
    # SPRTIE 1
    if keys_pressed[K_UP] and y1 > 0:
        y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
        y1 += speed
    if keys_pressed[K_LEFT] and x1 > 0:
        x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
        x1 += speed
    
    # SPRITE 2
    if keys_pressed[K_w] and y2 > 0:
        y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
        y2 += speed
    if keys_pressed[K_a] and x2 > 0:
        x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
        x2 += speed


    display.update()
    clock.tick(FPS)
