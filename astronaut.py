import pygame
from math import cos, sin, pi

class Astronaut():
    def __init__(self,x,y,theta=0,color='black'):
        self.x = x
        self.y = y
        self.theta = theta
        self.image = pygame.image.load('assets/spaceAstronauts_004.png')
        