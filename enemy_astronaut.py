import pygame
from math import atan2, degrees, radians, cos, sin
from astronaut import Astronaut


class EnemyAstronaut(Astronaut):
    def __init__(self, player, screen, x, y, WIDTH, HEIGHT, bullet_group, theta=270, color='white'):
        super().__init__(screen, x, y, WIDTH, HEIGHT, bullet_group, theta, color)
        self.player = player
        self.is_moving = False

    def track_player(self):
        # overwriting checking keyboard and instead ship makes its own decisions
        # set the speed
        self.speed = 1
        # get the position of the player (lag)
        delta_x = self.player.x + self.x
        delta_y = self.player.y + self.y

        # if delta is too small do nothing!
        if delta_x**2 + delta_y**2 > 5:
            self.theta = degrees(atan2(-delta_y,delta_x))