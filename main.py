import pygame
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
BACKGROUND_COLOR = (135, 206, 250)
FONT = pygame.font.Font('freesansbold.ttf', 32)

# Initialize screen and clock
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")
CLOCK = pygame.time.Clock()

# Load images
DINO_IMG = pygame.image.load("dino.png")
DINO_IMG = pygame.transform.scale(DINO_IMG, (120, 100))

CACTUS_IMG = pygame.image.load("cactus.png")
CACTUS_IMG = pygame.transform.scale(CACTUS_IMG, (64, 64))

# Class for the Dinosaur
class Dino:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.init_y = y
        self.velocity = 0
        self.jumping = False

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.velocity = -30  # initial velocity for jump

    def move(self):
        if self.jumping:
            self.y += self.velocity
            self.velocity += 1
            if self.y >= self.init_y:
                self.y = self.init_y
                self.jumping = False

    def draw(self):
        SCREEN.blit(DINO_IMG, (self.x, self.y))

# Class for the Cactus
class Cactus:
    def __init__(self, x, y, velocity):
        self.x, self.y = x, y
        self.velocity = velocity

    def move(self):
        self.x -= self.velocity

    def reset_position(self):
        self.x = WIDTH

    def draw(self):
        SCREEN.blit(CACTUS_IMG, (self.x, self.y))

def draw_button(text, x, y, w, h):
    pygame.draw.rect(SCREEN, (0, 128, 0), (x, y, w, h))
    btn_text = FONT.render(text, True, (255, 255, 255))
    text_rect = btn_text.get_rect(center=(x + w // 2, y + h // 2))
    SCREEN.blit(btn_text, text_rect.topleft)

# Main game loop
def game_loop():
    # Initialize game variables
    dino = Dino(50, HEIGHT - 100)
    cactus = Cactus(800, HEIGHT - 64, 7)

    score = 0
    high_score = 0

    # Load high score from file
    try:
        with open('high_score.txt', 'r') as f:
            high_score = int(f.read())
    except FileNotFoundError:
        pass

    game_time = 0
    running = False
    start_ticks = None

    while True:
        SCREEN.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x > WIDTH // 2 - 60 and x < WIDTH // 2 + 60 and y > HEIGHT // 2 - 20 and y < HEIGHT // 2 + 20:
                    if not running:
                        running = True
                        start_ticks = pygame.time.get_ticks()
                        cactus.reset_position()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino.jump()

        if running:
            game_time = (pygame.time.get_ticks() - start_ticks) // 1000
            cactus.move()
            dino.move()

            if cactus.x < -80:
                cactus.reset_position()
                score += 1

            if abs(dino.x - cactus.x) < 70 and abs(dino.y - cactus.y) < 70:
                running = False
                if score > high_score:
                    high_score = score
                    with open('high_score.txt', 'w') as f:
                        f.write(str(high_score))

        # Draw elements
        dino.draw()
        cactus.draw()

        # Draw score and time
        score_text = FONT.render(f'Score: {score} x', True, (255, 255, 255))
        SCREEN.blit(score_text, (10, 10))
        time_text = FONT.render(f'Time: {game_time}s', True, (255, 255, 255))
        SCREEN.blit(time_text, (10, 40))

        # Draw high score
        high_score_text = FONT.render(f'High Score: {high_score}', True, (255, 255, 255))
        SCREEN.blit(high_score_text, (WIDTH - 225, 10))

        # Draw Start button
        if not running:
            draw_button('Start', WIDTH // 2 - 60, HEIGHT // 2 - 20, 120, 40)

        pygame.display.update()
        CLOCK.tick(60)

# Start the game loop
game_loop()