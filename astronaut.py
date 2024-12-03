import pygame
import math
from bullet import Bullet
from math import cos, sin, pi, radians
pygame.mixer.init()

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

            self.health = 100  # Health starts at 100
            self.max_health = 100  # Maximum health
        else:
            self.orig_image2 = pygame.image.load('assets/spaceAstronauts_007.png')
            self.orig_image = pygame.image.load('assets/spaceAstronauts_008.png')

            self.health = 5  # Health starts at 5 for enemies
            self.max_health = 5  # Maximum health
        # health bar stuff
        self.health_bar_length = 100  # Length of health bar in pixels
        self.health_bar_height = 10  # Height of health bar
        self.health_bar_offset = -30  # Offset from the top of the astronaut sprite
        self.image = self.orig_image # keep orig image to never be rotated
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0
        self.bullet_group = bullet_group
        # Shooting timers
        self.shoot_time = 0
        self.shoot_wait = 200  # Time between shots (ms)
        self.shoot_duration = 100  # Duration of shooting animation (ms)
        self.is_shooting = False
        self.shoot_sound = pygame.mixer.Sound('assets/shoot.ogg')
        # explosion stuff
        self.explosion_image = pygame.image.load('assets/explosion1.png')
        self.explosion_image = pygame.transform.scale_by(self.explosion_image, 6)
        self.explosion_timer = 0
        self.explosion_length = 500
        self.mask = pygame.mask.from_surface(self.image)
        # damage stuff
        self.last_hit_time = 0
        self.hit_cooldown = 200
        self.damage = 10

    def draw_health_bar(self):
        # Calculate the health bar position and size
        bar_length = (self.health / self.max_health) * self.health_bar_length
        bar_x = self.rect.centerx - self.health_bar_length // 2
        bar_y = self.rect.top + self.health_bar_offset

        # Draw the health bar background (red for lost health)
        pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, self.health_bar_length, self.health_bar_height))

        # Draw the current health (green)
        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, bar_length, self.health_bar_height))

    def take_damage(self,damage):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_hit_time > self.hit_cooldown:
            self.health -= damage
            self.last_hit_time = current_time
            if self.health <= 0:
                self.health = 0
                self.die()

    def die(self):
        self.kill()

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
        speed = 4

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
            self.theta += 4  # Adjust the increment as needed for smoother rotation


        if keys[pygame.K_LEFT]:
            # Rotate counterclockwise (increase the angle)
            self.theta -= 4

        
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
            # play the shoot sound
            self.shoot_sound.play()

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

        # Update image based on state
        if self.is_shooting:
            self.image = pygame.transform.rotozoom(self.orig_image3, -self.theta, 1)
            if pygame.time.get_ticks() - self.shoot_time > self.shoot_duration:
                self.is_shooting = False
        elif self.is_moving:
            if self.counter % 24 < 12:
                self.image = pygame.transform.rotozoom(self.orig_image, -self.theta, 1)
            else:
                self.image = pygame.transform.rotozoom(self.orig_image2, -self.theta, 1)
            self.counter += 1
        # Reset image to the original when not moving
        else:
            self.image = pygame.transform.rotozoom(self.orig_image, -self.theta, 1)


        self.rect = self.image.get_rect(center=(self.x, self.y))

        # draw health bar
        self.draw_health_bar()

        # check border
        self.check_border()

