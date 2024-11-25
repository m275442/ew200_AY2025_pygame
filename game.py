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
score_font = pygame.font.Font('assets/Exo2-VariableFont_wght.ttf',48)

# Render the score text
def draw_score(screen, score):
    score_text = score_font.render(f"Score: {score[0]}", True, (255, 50, 50))  # red color
    screen.blit(score_text, (20, 20))  # Top-left corner of the screen

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

num_enemies = [5]

# spawn enemy function
def spawn_enemies(WIDTH, HEIGHT, num_enemies, enemy_group):
    # Get the current number of enemies
    n = len(enemy_group)
    # Spawn enemies until the count matches the desired number
    for i in range(n, num_enemies[0]):
        x = randint(0, WIDTH)
        y = randint(0, 2 * TILESIZE)
        speed = randint(1, 5)
        enemy = EnemyAstronaut(astronaut1, screen, x, y, WIDTH, HEIGHT, bullet_group, color='white')
        enemy_group.add(enemy)

spawn_enemies(WIDTH, HEIGHT, num_enemies, enemy_group)


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
    

# check for collision kill them
    kill_sprites(enemy_group, bullet_group, score,  num_enemies)

    draw_score(screen, score)

# Increase difficulty progressively based on score
    if score[0] % 5 == 0 and score[0] != 0:  # Every 5 points, increase difficulty
        num_enemies[0] += 1
        score[0] += 1  # To prevent repeated increases for the same score
        print(f"Increasing difficulty! New enemy count: {num_enemies[0]}")

    spawn_enemies(WIDTH, HEIGHT, num_enemies, enemy_group)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()