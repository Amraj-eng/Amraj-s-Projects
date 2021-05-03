import pygame
from pygame.locals import *

pygame.init()

width = 500
height = 500
step = 40
vel = 4

red = (255, 0, 0)
yellow = (255, 255, 0)
colour_state = False
colour = red

x = (width - step)/2
y = (height - step)/2

isJump = False

window = pygame.display.set_mode((width, height))
running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                #colour = yellow
                colour_state = not colour_state
            #else:
                #colour = red

    pressed = pygame.key.get_pressed()

    if isJump:
        y, isJump, count = jump(y, count)

    else:

        if pressed[pygame.K_SPACE]:
            count = 10
            isJump = True
        if pressed[pygame.K_UP]: 
            y -= vel
        if pressed[pygame.K_DOWN]: 
            y += vel 

    if pressed[pygame.K_LEFT]: 
        x -= vel
    if pressed[pygame.K_RIGHT]: 
        x += vel


# check collision with window border

    if x < vel:
        x = 0

    if x > (width - step - vel):
        x = width - step

    if y < vel:
        y = 0

    if y > (height - step - vel):
        y = height - step

    if colour_state:
        colour = yellow
    else:
        colour = red


    def jump (y, count):
        isJump = True
        jump = 1 

        if count > -11:

            if count > 0:
                neg = -1
            else:
                neg = 1

            y += jump * neg* (count)**2
            count -= 1

        else:
            isJump = False
        
        return y, isJump, count

    window.fill((0, 0, 0))

    pygame.draw.rect(window, colour, pygame.Rect(x, y, step, step))
    pygame.display.flip()
    clock.tick(30)
