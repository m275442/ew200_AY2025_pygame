import pygame
from helpers import build_background

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
WIDTH = 1280
HEIGHT = 768

 # make background
build_background(WIDTH,HEIGHT)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()