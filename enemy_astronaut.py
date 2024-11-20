import pygame
import math
from math import atan2, degrees, radians, cos, sin
from astronaut import Astronaut


class EnemyAstronaut(Astronaut):
    def __init__(self, player, screen, x, y, WIDTH, HEIGHT, bullet_group, theta=270, color='white'):
        super().__init__(screen, x, y, WIDTH, HEIGHT, bullet_group, theta, color)
        self.player = player
        self.is_moving = False
        self.is_shooting = False

    def track_player(self):
        # Calculate the difference in position between the enemy and the player
        delta_x = self.player.x - self.x
        delta_y = self.player.y - self.y

        # Check the distance to avoid jittering when close to the player
        distance_squared = delta_x**2 + delta_y**2
        if distance_squared > 25:  # Chase if the player is more than 5 units away
            # Set the speed of the enemy astronaut
            self.speed = .5  # Adjust the speed as needed

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
