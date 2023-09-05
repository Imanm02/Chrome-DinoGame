# Install the "pygame" library first
# pip install pygame

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 400
score = 0

# Initialize screen and clock
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dino Game")
clock = pygame.time.Clock()

# Load images and fonts
dino_img = pygame.image.load("dino.png")
dino_img = pygame.transform.scale(dino_img, (50, 50))

cactus_img = pygame.image.load("cactus.png")
cactus_img = pygame.transform.scale(cactus_img, (50, 50))

font = pygame.font.Font('freesansbold.ttf', 32)

# Initialize variables
dino_x, dino_y = 50, height - 50
dino_velocity = 0

cactus_x, cactus_y = 800, height - 50
cactus_velocity = 10

running = False
jumping = False

def draw_button(text, x, y, w, h, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, w, h), border_radius=15)

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, w, h), border_radius=15)

    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surface = small_text.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (x + (w / 2), y + (h / 2))
    screen.blit(text_surface, text_rect)

def start_game():
    global running, score
    running = True
    score = 0

def stop_game():
    global running
    running = False

# Main game loop
while True:
    # Blue background
    screen.fill((0, 128, 255))
    clock.tick(30)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    # Draw buttons
    draw_button("Start", width // 3, height // 2, 100, 50, (0, 128, 0), (0, 255, 0), start_game)
    draw_button("Finish", 2 * width // 3, height // 2, 100, 50, (128, 0, 0), (255, 0, 0), stop_game)

    if running:
        # Gameplay and logic
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not jumping:
            jumping = True
            dino_velocity = -15

        if jumping:
            dino_y += dino_velocity
            dino_velocity += 1

        if dino_y >= height - 50:
            dino_y = height - 50
            jumping = False

        cactus_x -= cactus_velocity

        if cactus_x < -50:
            cactus_x = 800
            cactus_velocity = random.randint(5, 10)
            score += 1  # Increase score when successfully dodging a cactus

        # Collision detection
        dino_rect = pygame.Rect(dino_x, dino_y, 50, 50)
        cactus_rect = pygame.Rect(cactus_x, cactus_y, 50, 50)

        if dino_rect.colliderect(cactus_rect):
            running = False

        # Drawing images
        screen.blit(dino_img, (dino_x, dino_y))
        screen.blit(cactus_img, (cactus_x, cactus_y))

        # Draw score
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    pygame.display.update()