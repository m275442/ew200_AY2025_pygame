import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH = 1280
HEIGHT = 768
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game Instructions')

# Fonts
font = pygame.font.Font('assets/Exo2-VariableFont_wght.ttf', 36)  # Smaller font for the instructions
button_font = pygame.font.Font('assets/Exo2-VariableFont_wght.ttf', 72)

# Function to draw instructions
def draw_instructions():
    screen.fill((0, 0, 0))  # Black background

    # Instruction text in multiple lines
    lines = [
        "Welcome to the game! You are an astronaut stranded on a planet Earth.",
        "You and your crew were trying to escape but an infection spread.",
        "You are the sole survivor and your only way off the planet is with your ship,",
        "which is hidden in a tower. The infected are trying to destroy it and infect you...",
        "Use the arrow keys to move around and the space key to defend yourself!"
    ]
    
    # Render each line of text and display it
    y_position = HEIGHT // 4  # Starting position for text
    
    for line in lines:
        rendered_text = font.render(line, True, (255, 255, 255))  # White text
        screen.blit(rendered_text, (WIDTH // 2 - rendered_text.get_width() // 2, y_position))
        y_position += 50  # Move the next line down

    # Display "Start Game" text
    start_text = button_font.render("Start Game", True, (0, 255, 0))  # Green color
    start_text_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))  # Positioning "Start Game"
    screen.blit(start_text, start_text_rect)

    pygame.display.flip()  # Update the screen

    return start_text_rect  # Return the rectangle for "Start Game" button

# Function to handle the instruction screen
def instruction_screen():
    # Main loop for the instruction screen
    running = True
    start_button_rect = draw_instructions()  # Get the rectangle for the "Start Game" button

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Exit the game if the close button is clicked

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):  # If the player clicks "Start Game"
                    running = False  # Exit the instruction screen loop
                    return True  # Indicate to start the game

        pygame.time.Clock().tick(60)  # Limit the frame rate to 60 FPS

    return False  # If the player doesn't click "Start Game" or closes the window


