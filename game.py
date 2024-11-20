import pygame
from helpers import build_background
from astronaut import Astronaut
from enemy_astronaut import EnemyAstronaut

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
WIDTH = 1280
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))

 # make background
background = build_background(WIDTH,HEIGHT)

# make a sprite group and bullet group
astronaut_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

# make player1 
astronaut1 = Astronaut(screen, WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, bullet_group)

# make an enemy astronaut
enemy1 = EnemyAstronaut(astronaut1,screen, 400,400, WIDTH, HEIGHT, bullet_group, color='white')

# add player1 to group
astronaut_group.add(astronaut1) 
astronaut_group.add(enemy1)





while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.QUIT:
            running = False
    
    # Blit the background to the screen
    background = build_background(WIDTH,HEIGHT)
    screen.blit(background,(0,0))

    # update the astronaut's position
    astronaut_group.update()

    # update bullet position
    bullet_group.update()

    # draw the ship
    astronaut_group.draw(screen)

    # draw bullets
    bullet_group.draw(screen)
    

    



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()