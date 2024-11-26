import pygame
from random import randint

def build_background(WIDTH, HEIGHT):
    # Load images
    tower_left = pygame.image.load('assets/tile_46.png')
    small_tree = pygame.image.load('assets/tile_72.png')
    water = pygame.image.load('assets/tile_73.png')    
    grass = pygame.image.load('assets/tile_39.png')
    sand_edge_left = pygame.image.load('assets/tile_06.png')
    sand_edge = pygame.image.load('assets/tile_07.png')
    sand_edge_right = pygame.image.load('assets/tile_09.png')
    
    TILE_SIZE = grass.get_width()
    
    # Create a surface for the background
    background = pygame.Surface((WIDTH, HEIGHT))
    
    # Fill the background with grass tiles
    for i in range(0, WIDTH, TILE_SIZE):
        for n in range(0, HEIGHT, TILE_SIZE):
            background.blit(grass, (i, n))

    # Add water
    for i in range(0, WIDTH, TILE_SIZE):
        for n in range(0, 2 * TILE_SIZE, TILE_SIZE):
            background.blit(water, (i, n))

    # Add sand
    background.blit(sand_edge_left, (0, TILE_SIZE))
    for i in range(TILE_SIZE, WIDTH - TILE_SIZE, TILE_SIZE):
        background.blit(sand_edge, (i, TILE_SIZE))
    background.blit(sand_edge_right, ((WIDTH - TILE_SIZE), TILE_SIZE))

    

    # Add tree
    background.blit(small_tree, (TILE_SIZE, 2 * TILE_SIZE))

    return background  # Return the constructed background surface

background = build_background(1280,768)


def kill_sprites(ship_group, bullet_group, score, num_enemies):
        # check for bullets hitting ships
    coll_dict = pygame.sprite.groupcollide(ship_group,bullet_group,0,0)

    # check and see if a bullet collides with something that is not its mother
    for s,bs in coll_dict.items():
        # ship is k, bullet list is v
        # check for non empty values
        if bs:
            #loop over each bullet check its mom
            for b in bs:
                # check if bullet.mom is the player
                if b.mom != s:
                    # kill the astronaut
                    s.kill()
                    # kill the bullet
                    b.kill()
                    score[0] += 1
                    # increase the number of spawned ships by chance
                    if randint(0,10)<3:
                        num_enemies[0]+=1