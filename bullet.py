import pygame
from math import sin, cos, radians
class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, mom, x,y,theta,speed = 5):
        self.screen = screen
        self.x = x
        self.y = y
        self.mom = mom
        self.speed = speed
        self.theta = theta # degrees
        self.image = pygame.image.load('assets/cannonBall.png')
        self.rect = self.image.get_rect()
        # place the bullet
        self.rect.center = (self.x,self.y)