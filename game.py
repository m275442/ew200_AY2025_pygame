import pygame
from helpers import build_background, kill_sprites
from astronaut import Astronaut
from enemy_astronaut import EnemyAstronaut
from random import randint

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
WIDTH = 1280
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))

 # make background
background = build_background(WIDTH,HEIGHT)
grass = pygame.image.load('assets/tile_39.png')
TILESIZE = grass.get_width()

# make score
score = [0]

# make a sprite group and bullet group
astronaut_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
all_astronauts_group = pygame.sprite.Group()

# make player1 
astronaut1 = Astronaut(screen, WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, bullet_group)

# make an enemy astronaut
enemy1 = EnemyAstronaut(astronaut1,screen, 400,400, WIDTH, HEIGHT, bullet_group, color='white')

# add player1 to group
astronaut_group.add(astronaut1) 
enemy_group.add(enemy1)

num_enemies = [1]

# spawn enemy function
def spawn_enemies(WIDTH, HEIGHT, num_enemies, enemy_group):
    # check the number of ships, and spawn more as needed
    # get the number of ships right now
    n = len(enemy_group)
    for i in range(n, num_enemies[0]):
        x = randint(0, WIDTH)
        y = randint(0, 2 * TILESIZE)
        speed = randint(1, 5)
        enemy = EnemyAstronaut(astronaut1, screen, x,y, speed,  WIDTH, HEIGHT, bullet_group, color='white')
        enemy_group.add(enemy)


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

# update positions
    # update the astronaut's position
    astronaut_group.update()
    # update enemy position
    enemy_group.update()
    # update bullet position
    bullet_group.update()


# draw sprites
    # draw the ship
    astronaut_group.draw(screen)
    # draw bullets
    bullet_group.draw(screen)
    # draw enemies
    enemy_group.draw(screen)
    

# check for ship collision kill them
    kill_sprites(enemy_group, bullet_group, score,  num_enemies)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()