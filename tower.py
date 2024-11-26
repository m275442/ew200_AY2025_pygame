import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, screen, x,y, WIDTH, HEIGHT):
        self.screen = screen
        self.x = x
        self.y = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.health = 250
        self.orig_image = pygame.image.load('assets/tower.png')
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    