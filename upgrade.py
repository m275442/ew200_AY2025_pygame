import pygame

def show_upgrade_menu(screen, WIDTH, HEIGHT, astronaut, tower, player_health_upgrade, player_damage_upgrade, tower_health_upgrade):
    # Create upgrade menu (you can adjust this based on your UI design)
    menu_font = pygame.font.Font('assets/Exo2-VariableFont_wght.ttf', 36)
    menu_bg = pygame.Surface((WIDTH, HEIGHT))
    menu_bg.fill((0, 0, 0))  # Black background
    menu_bg.set_alpha(150)  # Make it semi-transparent
    screen.blit(menu_bg, (0, 0))

    # Render instruction text at the top
    instruction_text = menu_font.render("Please click an upgrade with your mouse", True, (255, 255, 255))
    screen.blit(instruction_text, (WIDTH//2 - instruction_text.get_width()//2, 50))  # Top center of the screen
    
    # Draw menu text
    health_text = menu_font.render(f"Heal Yourself (+{player_health_upgrade})", True, (255, 255, 255))
    damage_text = menu_font.render(f"Upgrade Damage (+{player_damage_upgrade})", True, (255, 255, 255))
    tower_health_text = menu_font.render(f"Heal the Tower (+{tower_health_upgrade})", True, (255, 255, 255))
    
    screen.blit(health_text, (WIDTH//2 - health_text.get_width()//2, HEIGHT//2 - 100))
    screen.blit(damage_text, (WIDTH//2 - damage_text.get_width()//2, HEIGHT//2))
    screen.blit(tower_health_text, (WIDTH//2 - tower_health_text.get_width()//2, HEIGHT//2 + 100))
    
    pygame.display.flip()

    # Wait for player input to close the menu (like pressing a key or clicking)
    menu_active = True
    while menu_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check if player clicks on one of the buttons to upgrade
                if (WIDTH//2 - health_text.get_width()//2 <= mouse_x <= WIDTH//2 + health_text.get_width()//2 and
                    HEIGHT//2 - 100 <= mouse_y <= HEIGHT//2 - 100 + health_text.get_height()):
                    astronaut.health += player_health_upgrade
                elif (WIDTH//2 - damage_text.get_width()//2 <= mouse_x <= WIDTH//2 + damage_text.get_width()//2 and
                    HEIGHT//2 - 100 <= mouse_y <= HEIGHT//2 - 100 + damage_text.get_height()):
                    astronaut.damage += player_damage_upgrade
                elif (WIDTH//2 - tower_health_text.get_width()//2 <= mouse_x <= WIDTH//2 + tower_health_text.get_width()//2 and
                    HEIGHT//2 - 100 <= mouse_y <= HEIGHT//2 - 100 + tower_health_text.get_height()):
                    tower.health += tower_health_upgrade
                menu_active = False  # Close the menu after upgrading
                
                # Similar checks can be done for the other upgrade buttons
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press Escape to close the menu
                    menu_active = False  # Close the menu when Escape is pressed
