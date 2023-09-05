# Python Chrome Dino Game

Dino Game is a simple but fun game developed in Python using the Pygame library. It is inspired by the famous Chrome Dino game that you can play when you're offline. Your aim is to control a dinosaur and dodge an incoming cactus to earn points.

## Code Walkthrough

The Dino Game is built in Python using the Pygame library. The source code is structured in a simple and straightforward manner to make it easy to understand and extend.

### File Structure

```plaintext
Dino-Game/
|-- main.py
|-- dino.png
|-- cactus.png
|-- high_score.txt (generated at runtime)
```

### Imports and Initialization

We begin by importing the necessary modules and initializing Pygame. The screen and clock are set up, and images are loaded into memory.

```python
import pygame
import time

pygame.init()

WIDTH, HEIGHT = 800, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

DINO_IMG = pygame.image.load("dino.png")
CACTUS_IMG = pygame.image.load("cactus.png")
```

### Dino Class

The Dino class is responsible for all dinosaur-related logic. It handles the dinosaur's position, drawing it on the screen, and the jump action.

```python
class Dino:
    def __init__(self, x, y):
        # constructor code
    def jump(self):
        # jump code
    def move(self):
        # move code
    def draw(self):
        # draw code
```

### Cactus Class

Similarly, the Cactus class deals with the cactus' logic. It takes care of the position, velocity, and drawing of the cactus.

```python
class Cactus:
    def __init__(self, x, y, velocity):
        # constructor code
    def move(self):
        # move code
    def reset_position(self):
        # reset position code
    def draw(self):
        # draw code
```

### Main Game Loop

The game loop is where all the magic happens. We handle events, update game states, and redraw elements in this loop.

```python
def game_loop():
    dino = Dino(50, HEIGHT - 100)
    cactus = Cactus(800, HEIGHT - 64, 7)
    # ... more initialization code
    while True:
        # ... event handling
        # ... game logic
        # ... drawing elements
```

### Utilities

Utility functions are also defined for reusable operations like drawing buttons and displaying text.

```python
def draw_button(text, x, y, w, h):
    # ... draw button code
```

### High Score

The game also includes a high score feature that saves and loads the highest score from a text file.

```python
with open('high_score.txt', 'r') as f:
    high_score = int(f.read())
```

## Maintainer

- [Iman Mohammadi](https://github.com/Imanm02)
