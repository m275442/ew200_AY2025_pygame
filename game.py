import pygame

# pygame setup
pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
running = True
grass = pygame.image.load('tile_39.png')
tower_left = pygame.image.load('tile_46.png')
small_tree = pygame.image.load('tile_72.png')
water = pygame.image.load('tile_73.png')
TILE_SIZE = grass.get_width()


 # make background
for i in range(0,WIDTH,TILE_SIZE):
    for n in range(0,HEIGHT,TILE_SIZE):
        screen.blit(grass,(i,n))

# add water
for i in range(0,WIDTH, TILE_SIZE):
    screen.blit(water,(i,0))

# add tower
screen.blit(tower_left,(2*TILE_SIZE,3*TILE_SIZE))

# add tree
screen.blit(small_tree,(TILE_SIZE,2*TILE_SIZE))


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