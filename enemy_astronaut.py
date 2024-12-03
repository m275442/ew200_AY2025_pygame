import pygame
import math
from math import atan2, degrees, radians, cos, sin
from astronaut import Astronaut


class EnemyAstronaut(Astronaut):
    def __init__(self, player, tower, screen, x, y, WIDTH, HEIGHT, bullet_group, theta=270, color='white', health=50, damage=5):
        super().__init__(screen, x, y, WIDTH, HEIGHT, bullet_group, theta, color)
        self.player = player
        self.tower = tower
        self.health = health
        self.is_moving = False
        self.is_shooting = False
        self.attack_target = tower # default to attacking the tower instead of the player
        # health bar stuff
        self.health_bar_length = 100  # Length of health bar in pixels
        self.health_bar_height = 10  # Height of health bar
        self.health_bar_offset = -30  # Offset from the top of the astronaut sprite
        self.max_health = health
        self.damage = damage  # Damage inflicted by this enemy (can be upgraded)

    def track_player(self):
         # Calculate distance to the player and the tower
        player_distance = math.sqrt((self.player.x - self.x)**2 + (self.player.y - self.y)**2)
        tower_distance = math.sqrt((self.tower.x - self.x)**2 + (self.tower.y - self.y)**2)

        # make enemy attack player only within certain radius
        if player_distance < 150:  # prioritize player if within 200 pixels
            self.attack_target = self.player
        else:
            self.attack_target = self.tower
        
        # Calculate the difference in position between the enemy and the player
        delta_x = self.attack_target.x - self.x
        delta_y = self.attack_target.y - self.y

        # Check the distance to avoid jittering when close to the player
        distance_squared = delta_x**2 + delta_y**2
        if distance_squared > 25:  # Chase if the player is more than 5 units away
            # Set the speed of the enemy astronaut
            self.speed = 0.75  # Adjust the speed as needed

            # Calculate the angle to the player
            self.theta = degrees(atan2(delta_y, delta_x))

            # Move toward the player
            direction_x = cos(radians(self.theta))
            direction_y = sin(radians(self.theta))

            # Update the position of the enemy
            self.x += direction_x * self.speed
            self.y += direction_y * self.speed

        else:
            # Stop moving if close enough
            self.speed = 0

    def back_up(self):
        # Calculate the direction to move backward based on the current angle
        angle_rad = radians(self.theta)
        direction_x = -cos(angle_rad)  # Opposite direction
        direction_y = -sin(angle_rad)  # Opposite direction

        # Adjust the position of the enemy
        self.x += direction_x * 20  # The 10 is the distance to back up; adjust as needed
        self.y += direction_y * 20

        # Update the rectangle position
        self.rect.center = (self.x, self.y)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def draw_health_bar(self):
        if self.max_health <= 0:  # Avoid division by zero
            return
        bar_length = max(0, (self.health / self.max_health) * self.health_bar_length)  # Prevent negative length
        bar_x = self.rect.centerx - self.health_bar_length // 2
        bar_y = self.rect.top + self.health_bar_offset

        # Draw the health bar background (red for lost health)
        pygame.draw.rect(self.screen, (255, 0, 0), (bar_x, bar_y, self.health_bar_length, self.health_bar_height))
        # Draw the current health (green)
        pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, bar_length, self.health_bar_height))

    def attack(self):
        # Damage the target (player or tower)
        if self.attack_target == self.tower:
            self.tower.take_damage(self.damage)
        elif self.attack_target == self.player:
            self.player.take_damage(self.damage)

    def update(self):
        super().update()
        self.draw_health_bar()