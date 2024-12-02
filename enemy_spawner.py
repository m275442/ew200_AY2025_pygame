import pygame
from random import randint
from enemy_astronaut import EnemyAstronaut


def spawn_wave(current_wave, WIDTH, HEIGHT, enemy_group, astronaut1, tower, screen, bullet_group, TILESIZE, enemies_per_wave=5):
    num_enemies = current_wave * enemies_per_wave  # Increase enemies per wave
    for _ in range(num_enemies):
        x = randint(0, WIDTH)
        y = randint(0, TILESIZE)
        speed = randint(1, 2 + current_wave)  # Increase speed with wave
        enemy = EnemyAstronaut(astronaut1, tower, screen, x, y, WIDTH, HEIGHT, bullet_group, color='white',health=50)
        enemy_group.add(enemy)



def draw_wave_info(screen, wave, WIDTH,wave_font):
    wave_text = wave_font.render(f"Wave {wave}", True, (255, 255, 255))
    screen.blit(wave_text, (WIDTH // 2 - wave_text.get_width() // 2, 20))  # Centered at the top