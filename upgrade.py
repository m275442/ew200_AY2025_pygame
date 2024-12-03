import pygame

def show_upgrade_menu(screen, width, height, player, tower, player_health_upgrade, player_damage_upgrade, tower_health_upgrade):
    print("Upgrade menu triggered!")  # This will help confirm it's being called
    upgrade_active = True
    font = pygame.font.Font('assets/Exo2-VariableFont_wght.ttf', 36)
    options = [
        f"1. Increase Player Health (+{player_health_upgrade})",
        f"2. Increase Player Damage (+{player_damage_upgrade})",
        f"3. Increase Tower Health (+{tower_health_upgrade})"
    ]
    selected_option = 0

    while upgrade_active:
        # Render the upgrade menu
        screen.fill((0, 0, 0))  # Black background
        title_text = font.render("Choose an Upgrade:", True, (255, 255, 255))
        screen.blit(title_text, (width // 2 - title_text.get_width() // 2, 100))

        for i, option in enumerate(options):
            color = (255, 255, 0) if i == selected_option else (255, 255, 255)
            option_text = font.render(option, True, color)
            screen.blit(option_text, (width // 2 - option_text.get_width() // 2, 200 + i * 50))

        pygame.display.flip()

        # Handle user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    # Apply the selected upgrade
                    if selected_option == 0:
                        player.health += player_health_upgrade
                    elif selected_option == 1:
                        player.damage += player_damage_upgrade
                    elif selected_option == 2:
                        tower.health += tower_health_upgrade
                    upgrade_active = False
