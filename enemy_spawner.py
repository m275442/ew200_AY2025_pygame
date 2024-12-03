import pygame
from random import randint
from enemy_astronaut import EnemyAstronaut


def spawn_wave(current_wave, WIDTH, HEIGHT, enemy_group, astronaut1, tower, screen, bullet_group, TILESIZE, enemies_per_wave=5):
    num_enemies = current_wave + 3 # Increase enemies per wave
    for _ in range(num_enemies):
        x = randint(0, WIDTH)
        y = randint(0, TILESIZE)
        # Increase damage with wave (e.g., base damage + 2 per wave)
        damage = 5 + (current_wave * 5)
        health = 50 + (current_wave *2)  # increase health too
        enemy = EnemyAstronaut(astronaut1, tower, screen, x, y, WIDTH, HEIGHT, bullet_group, color='white',health=health, damage=damage)
        enemy_group.add(enemy)



def draw_wave_info(screen, wave, WIDTH,wave_font):
    wave_text = wave_font.render(f"Wave {wave}", True, (255, 255, 255))
    screen.blit(wave_text, (WIDTH // 2 - wave_text.get_width() // 2, 20))  # Centered at the top