import pygame
from helpers import build_background, kill_sprites
from astronaut import Astronaut
from enemy_astronaut import EnemyAstronaut
from tower import Tower
from random import randint
from enemy_spawner import spawn_wave, draw_wave_info
from upgrade import show_upgrade_menu

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

# make health
health = [20]
health_font = pygame.font.Font('assets/Exo2-VariableFont_wght.ttf',48)

# make a sprite group and bullet group
astronaut_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
all_astronauts_group = pygame.sprite.Group()
tower_group = pygame.sprite.Group()

# make player1 
astronaut1 = Astronaut(screen, WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, bullet_group)
# add player1 to group
astronaut_group.add(astronaut1) 

# make tower
tower = Tower(screen, WIDTH/2, HEIGHT - TILESIZE, WIDTH, HEIGHT)
# add tower to group
tower_group.add(tower)


# Wave variables
num_enemies = [5]
current_wave = 1  # Start with wave 1
time_between_waves = 2000 # 2 seconds between waves (in milliseconds)
last_wave_time = pygame.time.get_ticks()  # Track the last wave time
wave_active = False  # Whether the current wave is still active
wave_font = pygame.font.Font('assets/Exo2-VariableFont_wght.ttf', 48)



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

# wave info
    draw_wave_info(screen,current_wave,WIDTH,wave_font)

# update positions
    # update the astronaut's position
    astronaut_group.update()
    # update enemy position
    enemy_group.update()
    # update bullet position
    bullet_group.update()
    # update tower health
    tower_group.update()


# draw sprites
    # draw the ship
    astronaut_group.draw(screen)
    # draw bullets
    bullet_group.draw(screen)
    # draw enemies
    enemy_group.draw(screen)
    # draw tower
    tower_group.draw(screen)
    

# check for collision kill them
    kill_sprites(enemy_group, bullet_group, score,  num_enemies)

# Check for collisions between the player and enemies
    collisions = pygame.sprite.spritecollide(astronaut1, enemy_group, False, pygame.sprite.collide_mask)

    if collisions:  # If any collisions occurred
        astronaut1.take_damage(5)  # Reduce health by 5
        # make each enemy that collides back up
        for enemy in collisions:
            enemy.back_up()

# Check for collisions and reduce health
    tower_collisions = pygame.sprite.spritecollide(tower, enemy_group, False, pygame.sprite.collide_mask)
    if tower_collisions:
        tower.take_damage(10)
        for enemy in tower_collisions:
            enemy.back_up()

    draw_score(screen, score)

     # Wave-based spawning logic
    if not wave_active and pygame.time.get_ticks() - last_wave_time > time_between_waves:
        # Show upgrade menu every 5 waves
        print(f"Current wave before upgrade check: {current_wave}")
        if current_wave % 2 == 0 and current_wave > 0:
            print(f"Wave {current_wave}: Showing upgrade menu.")  # Debug log
            show_upgrade_menu(
                screen, WIDTH, HEIGHT, astronaut1, tower,
                player_health_upgrade=20,
                player_damage_upgrade=5,
                tower_health_upgrade=50
            )

        # Start a new wave after the menu
        wave_active = True
        spawn_wave(current_wave, WIDTH, HEIGHT, enemy_group, astronaut1, tower, screen, bullet_group, TILESIZE, enemies_per_wave=current_wave * 3)



    # Check if the wave is cleared
    if wave_active and len(enemy_group) == 0:
        wave_active = False
        last_wave_time = pygame.time.get_ticks()  # Reset wave timer
        current_wave += 1  # Increase wave count
        print(f"Wave {current_wave - 1} cleared!")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()