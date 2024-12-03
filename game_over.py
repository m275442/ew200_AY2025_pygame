import pygame

WIDTH = 1280
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def show_game_over(screen, message):
    # Create a semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(150)  # Set transparency level (0-255)
    overlay.fill((0, 0, 0))  # Fill the overlay with black color

    # Render the message
    pygame.font.init()
    font = pygame.font.Font('assets/Exo2-VariableFont_wght.ttf', 72)  # Large font for the message
    text = font.render(message, True, (255, 0, 0))  # Red color for the message

    # Get the size of the text to center it on the screen
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Draw the overlay and the text to the screen
    screen.blit(overlay, (0, 0))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()
    
    # Wait for a moment before allowing the game to quit or restart
    pygame.time.wait(3000)  # Wait for 3 seconds before exiting or restarting

