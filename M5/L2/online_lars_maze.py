from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width , win_height))
display.set_caption("Maze")
background = transform.scale(image.load("M5/L2/background.jpg"), (win_width, win_height))

FPS = 60
game = True
clock = time.Clock()

while game:
    window.blit(background, (0,0))

    events = event.get()
    for e in events:
        if e.type == QUIT:
            game = False
        

    # keys_pressed = key.get_pressed()
    # # SPRTIE 1
    # if keys_pressed[K_UP] and y1 > 0:
    #     y1 -= speed
    # if keys_pressed[K_DOWN] and y1 < 395:
    #     y1 += speed
    # if keys_pressed[K_LEFT] and x1 > 0:
    #     x1 -= speed
    # if keys_pressed[K_RIGHT] and x1 < 595:
    #     x1 += speed


    display.update()
    clock.tick(FPS)