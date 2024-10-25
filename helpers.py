import pygame

def build_background(WIDTH,HEIGHT):
    tower_left = pygame.image.load('assets/tile_46.png')
    small_tree = pygame.image.load('assets/tile_72.png')
    water = pygame.image.load('assets/tile_73.png')    
    grass = pygame.image.load('assets/tile_39.png')
    sand_edge_left = pygame.image.load('assets/tile_06.png')
    sand_edge = pygame.image.load('assets/tile_07.png')
    sand_edge_right = pygame.image.load('assets/tile_09.png')
    TILE_SIZE = grass.get_width()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
     # make background
    for i in range(0,WIDTH,TILE_SIZE):
        for n in range(0,HEIGHT,TILE_SIZE):
            screen.blit(grass,(i,n))

    # add water
    for i in range(0,WIDTH, TILE_SIZE):
        for n in range(0,2*TILE_SIZE,TILE_SIZE):
            screen.blit(water,(i,n))

    # add sand 
    screen.blit(sand_edge_left,(0,TILE_SIZE))
    for i in range(TILE_SIZE,WIDTH-TILE_SIZE,TILE_SIZE):
        screen.blit(sand_edge,(i,TILE_SIZE))
    screen.blit(sand_edge_right,(9*TILE_SIZE,TILE_SIZE))

    # add tower
    screen.blit(tower_left,(2*TILE_SIZE,3*TILE_SIZE))

    # add tree
    screen.blit(small_tree,(TILE_SIZE,2*TILE_SIZE))