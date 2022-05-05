import pygame 
from pygame.locals import *
# Initialize pygame
pygame.init()

# Game Window
screen = pygame.display.set_mode(1000, 1000)

# Title and Icon
pygame.display.set_caption("Neither World")
icon = pygame.image.load()
pygame.display.set_icon(icon)


# Game Loop
running = True

while running:
    screen.fill(0, 0, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
