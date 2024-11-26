import pygame


class Tower(pygame.sprite.Sprite):
    def __init__(self, screen, x,y, WIDTH, HEIGHT):
        super().__init__()  
        self.screen = screen
        self.x = x
        self.y = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.orig_image = pygame.image.load('assets/tower.png')
        self.image = self.orig_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = 500  # Health starts at 500
        self.max_health = 500  # Maximum health
        self.health_bar_length = 300  # Length of health bar in pixels
        self.health_bar_height = 10  # Height of health bar
        self.health_bar_offset = -30  # Offset from the top of the astronaut sprite

        # Cooldown for taking damage
        self.last_hit_time = 0  # Initialize the last time it was hit
        self.hit_cooldown = 1000  # Cooldown time in milliseconds

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
        print("Tower has been destroyed!")

    def update(self):
        self.draw_health_bar()