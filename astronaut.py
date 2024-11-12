import pygame
import math
from math import cos, sin, pi

class Astronaut(pygame.sprite.Sprite):
    def __init__(self,x,y, WIDTH, HEIGHT,theta=0,color='black'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen_w = WIDTH
        self.screen_h = HEIGHT
        self.speed = 0
        self.theta = theta
        self.color = color
        if color == 'black':
            self.orig_image = pygame.image.load('assets/spaceAstronauts_004.png')
        else:
            self.orig_image = pygame.image.load('assets/spaceAstronauts_007.png')
        self.image = self.orig_image # keep orig image to never be rotated
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def deg_to_rad(self, deg):
        # converts deg to rad
        rad = (deg/180) * pi
        return rad
    
    def check_keys(self):
        keys = pygame.key.get_pressed()

        # Convert angle to radians (pygame uses degrees, but math functions use radians)
        # Note: Adding 90 degrees (or pi/2 radians) aligns the "forward" movement to start facing right
        angle_rad = math.radians(self.theta)

        # Speed of movement
        speed = 5

        # Check for input and update position based on the angle
        # Check for input and update position based on the angle
        if keys[pygame.K_UP]:
            # Move forward in the direction the sprite is facing
            self.x += speed * math.cos(angle_rad)
            self.y += speed * math.sin(angle_rad)

        if keys[pygame.K_DOWN]:
            # Move backward in the direction the sprite is facing
            self.x -= speed * math.cos(angle_rad)
            self.y -= speed * math.sin(angle_rad)

        if keys[pygame.K_RIGHT]:
            # Rotate clockwise (reduce the angle)
            self.theta += 5  # Adjust the increment as needed for smoother rotation

        if keys[pygame.K_LEFT]:
            # Rotate counterclockwise (increase the angle)
            self.theta -= 5

    def check_border(self):
        # make sure our ship rect is inside of some rect we set
        border_rect = pygame.rect.Rect(0,0,self.screen_w, self.screen_h)
        if not border_rect.contains(self.rect):
            # Reposition the astronaut to stay within bounds
            if self.rect.left < 0:
                self.rect.left = 0
                self.x = self.rect.centerx
            if self.rect.right > self.screen_w:
                self.rect.right = self.screen_w
                self.x = self.rect.centerx
            if self.rect.top < 0:
                self.rect.top = 0
                self.y = self.rect.centery
            if self.rect.bottom > self.screen_h:
                self.rect.bottom = self.screen_h
                self.y = self.rect.centery


    def update(self):

        # Check keys only if the astronaut is influenced by key input
        if self.color == 'black':   
            self.check_keys()

        # Update rect's center to match the new (x, y) position
        self.rect.center = (self.x, self.y)

        # Rotate the image based on the current angle (self.theta)
        # Negative to match rotation direction in Pygame's coordinate system
        self.image = pygame.transform.rotozoom(self.orig_image, -self.theta, 0.7)
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # check border
        self.check_border()



        

        