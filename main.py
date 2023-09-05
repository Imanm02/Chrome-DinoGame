import pygame
import random
import time

import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 400
background_color = (135, 206, 250)
score = 0
game_time = 0

# Initialize screen and clock
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino Game")
clock = pygame.time.Clock()

# Load images and fonts
dino_img = pygame.image.load("dino.png")
dino_img = pygame.transform.scale(dino_img, (120, 100))

cactus_img = pygame.image.load("cactus.png")
cactus_img = pygame.transform.scale(cactus_img, (64, 64))  # 80% of the original size

font = pygame.font.Font('freesansbold.ttf', 32)

# Initialize variables
dino_x, dino_y, dino_init_y = 50, height - 100, height - 100
dino_velocity = 0

cactus_x, cactus_y = 800, height - 64  # Adjusted for the new cactus size
cactus_velocity = 7

start_ticks = None
running = False
jumping = False
button_show = True

# Button dimensions
button_width, button_height = 120, 40

while True:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            if button_show:
                # Start Button
                if x > width // 2 - button_width // 2 and x < width // 2 + button_width // 2 and y > height // 2 - button_height and y < height // 2:
                    running = True
                    start_ticks = pygame.time.get_ticks()
                    button_show = False

                # Finish Button
                if x > width // 2 - button_width // 2 and x < width // 2 + button_width // 2 and y > height // 2 + button_height and y < height // 2 + 2 * button_height:
                    running = False
                    button_show = True
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                dino_velocity = -15  # Increased initial velocity for higher jump

    if running:
        if start_ticks is None:
            start_ticks = pygame.time.get_ticks()

        game_time = (pygame.time.get_ticks() - start_ticks) // 1000

        # Update positions
        cactus_x -= cactus_velocity

        if jumping:
            dino_y += dino_velocity
            dino_velocity += 1

            if dino_y >= dino_init_y:
                dino_y = dino_init_y
                jumping = False

        if cactus_x < -80:
            cactus_x = width
            score += 1

        if abs(dino_x - cactus_x) < 70 and abs(dino_y - cactus_y) < 70:
            running = False
            button_show = True
            dino_y = dino_init_y  # Reset dino position

    # Draw
    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(cactus_img, (cactus_x, cactus_y))

    if running:
        score_text = font.render(f'Score: {score} x', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        time_text = font.render(f'Time: {game_time}s', True, (255, 255, 255))
        screen.blit(time_text, (10, 40))

    if button_show:
        pygame.draw.rect(screen, (0, 128, 0), (width // 2 - button_width // 2, height // 2 - button_height, button_width, button_height))
        pygame.draw.rect(screen, (128, 0, 0), (width // 2 - button_width // 2, height // 2 + button_height, button_width, button_height))

        start_text = font.render('Start', True, (255, 255, 255))
        screen.blit(start_text, (width // 2 - 30, height // 2 - button_height + 5))

        finish_text = font.render('Finish', True, (255, 255, 255))
        screen.blit(finish_text, (width // 2 - 30, height // 2 + button_height + 5))

    pygame.display.update()
    clock.tick(60)