import pygame
import math
from bullet import Bullet
from math import cos, sin, pi, radians

class Astronaut(pygame.sprite.Sprite):
    def __init__(self, screen, x,y, WIDTH, HEIGHT, bullet_group, theta=0,color='black'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.screen_w = WIDTH
        self.screen_h = HEIGHT
        self.screen = screen
        self.speed = 0
        self.theta = theta
        self.color = color
        if color == 'black':
            self.orig_image = pygame.image.load('assets/spaceAstronauts_004.png')
            self.orig_image2 = pygame.image.load('assets/spaceAstronauts_005.png') # image with hands out
            self.orig_image3 = pygame.image.load('assets/spaceAstronauts_006.png') # shooting
        else:
            self.orig_image = pygame.image.load('assets/spaceAstronauts_007.png')
            self.orig_image2 = pygame.image.load('assets/spaceAstronauts_008.png')
        self.image = self.orig_image # keep orig image to never be rotated
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        self.bullet_group = bullet_group
        # Shooting timers
        self.shoot_time = 0
        self.shoot_wait = 500  # Time between shots (ms)
        self.shoot_duration = 200  # Duration of shooting animation (ms)
        self.is_shooting = False
    
    def deg_to_rad(self, deg):
        # converts deg to rad
        rad = (deg/180) * pi
        return rad
    
    def check_keys(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False
        self.is_shooting = False

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
            self.is_moving = True  # Set flag to True when moving

        if keys[pygame.K_DOWN]:
            # Move backward in the direction the sprite is facing
            self.x -= speed * math.cos(angle_rad)
            self.y -= speed * math.sin(angle_rad)
            self.is_moving = True  # Set flag to True when moving

        if keys[pygame.K_RIGHT]:
            # Rotate clockwise (reduce the angle)
            self.theta += 5  # Adjust the increment as needed for smoother rotation


        if keys[pygame.K_LEFT]:
            # Rotate counterclockwise (increase the angle)
            self.theta -= 5

        
        if keys[pygame.K_SPACE]:
            # activate shoot
            self.is_shooting = True
            self.shoot()
    

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

    def shoot(self):
        # only shoot if the time has elapsed
        if pygame.time.get_ticks() - self.shoot_time > self.shoot_wait:
            # we are allowed to shoot now
            self.is_shooting = True
            self.shoot_time = pygame.time.get_ticks()
            
            # if we have waited long enough, then make bullet

            # offset so it shoots from astronaut gun 
             # Offset the bullet's spawn position
            offset_x = self.rect.width / 2  # Right edge of the sprite
            offset_y = self.rect.height / 4  # Adjust to a point near the top

            # Rotate the offsets based on the current rotation
            angle_rad = radians(self.theta)
            rotated_x = offset_x * cos(angle_rad) - offset_y * sin(angle_rad)
            rotated_y = offset_x * sin(angle_rad) + offset_y * cos(angle_rad)

            # Calculate the final bullet spawn position
            bullet_x = self.x + rotated_x
            bullet_y = self.y + rotated_y

            b = Bullet(self.screen, self, bullet_x, bullet_y, self.theta)
            # put the bullet in a group
            self.bullet_group.add(b)
    
    def track_player(self):
        # This code is in my enemy ship class
        pass

    def update(self):

        # Check keys only if the astronaut is influenced by key input
        if self.color == 'black':   
            self.check_keys()
        else:
            self.track_player()

        # Update rect's center to match the new (x, y) position
        self.rect.center = (self.x, self.y)

        # Change image only if the astronaut is moving
        if self.is_moving:
            if self.counter % 24 < 12:  # Toggle images to create walking effect
                self.image = pygame.transform.rotozoom(self.orig_image, -self.theta, 1)
            else:
                self.image = pygame.transform.rotozoom(self.orig_image2, -self.theta, 1)
            self.counter += 1  # Increment the counter when moving
        # change image if astronaut is shooting
        elif self.is_shooting:
            self.image = pygame.transform.rotozoom(self.orig_image3, -self.theta, 1)
            if pygame.time.get_ticks() - self.shoot_time > self.shoot_duration:
                self.is_shooting = False

        else:
            # Reset image to the original when not moving
            self.image = pygame.transform.rotozoom(self.orig_image, -self.theta, 1)


        self.rect = self.image.get_rect(center=(self.x, self.y))

        # check border
        self.check_border()



        

        