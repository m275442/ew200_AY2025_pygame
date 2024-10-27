import pygame
from helpers import build_background
from astronaut import Astronaut

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
WIDTH = 1280
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))

 # make background
background = build_background(WIDTH,HEIGHT)


# make player1 
astronaut1 = Astronaut(WIDTH/2,HEIGHT/2)
astronaut1.draw(screen)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        astronaut1.theta -= 90
        pygame.time.delay(100)
    if keys[pygame.K_LEFT]:
        astronaut1.theta += 90
        pygame.time.delay(100)
    if keys[pygame.K_UP]:
        astronaut1.x += 1
        pygame.time.delay(100)
    if keys[pygame.K_DOWN]:
        astronaut1.x -= 1
        pygame.time.delay(100)

    # update the astronaut's position
    astronaut1.update()

    # Blit the background to the screen
    background = build_background(WIDTH,HEIGHT)
    screen.blit(background,(0,0))

    # draw the astronaut
    astronaut1.draw(screen)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()