# Install the "pygame" library first
# pip install pygame

import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
width, height = 800, 400
screen = pygame.display.set_mode((width, height))

# Title and icon
pygame.display.set_caption("Dino Game")
icon = pygame.Surface((10, 10))  # Create a dummy surface for the icon
pygame.display.set_icon(icon)

# Dino
dino_img = pygame.Surface((50, 50))
dino_img.fill((0, 128, 0))
dino_x, dino_y = 50, height - 50
dino_velocity = 0

# Cactus
cactus_img = pygame.Surface((50, 50))
cactus_img.fill((128, 0, 0))
cactus_x, cactus_y = 800, height - 50
cactus_velocity = 10

# Main loop
running = True
jumping = False
clock = pygame.time.Clock()
while running:
    screen.fill((255, 255, 255))  # Fill the screen with white
    clock.tick(30)  # Cap the frame rate at 30 FPS
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        dino_velocity = -15
    
    # Update Dino position
    if jumping:
        dino_y += dino_velocity
        dino_velocity += 1
    
    if dino_y >= height - 50:
        dino_y = height - 50
        jumping = False
    
    # Update cactus position
    cactus_x -= cactus_velocity
    if cactus_x < -50:
        cactus_x = 800
        cactus_y = height - 50
        cactus_velocity = random.randint(5, 10)
    
    # Collision detection
    dino_rect = pygame.Rect(dino_x, dino_y, 50, 50)
    cactus_rect = pygame.Rect(cactus_x, cactus_y, 50, 50)
    if dino_rect.colliderect(cactus_rect):
        running = False  # Game Over
    
    # Draw everything
    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(cactus_img, (cactus_x, cactus_y))
    
    pygame.display.update()  # Update the display

pygame.quit()