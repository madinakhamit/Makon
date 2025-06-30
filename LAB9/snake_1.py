# Import necessary libraries
import pygame
import sys
import random
import time

# Initialize pygame
pygame.init()

# Set the width and height of the game window
width, height = 500, 500
cell_size = 10  # Each cell the snake moves in is 10x10 pixels

# Create the game window
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKE")

# Define some colors using RGB format
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

# Initialize the snake's starting position and body
snake_pos = [100, 100]
snake_body = [[100, 100], [90, 100], [80, 100]]

# Load and scale the image for the snake's head
snake = pygame.image.load('snake.jpg').convert_alpha()
snake = pygame.transform.scale(snake, (cell_size, cell_size))

# Class for handling food (apple) properties and behavior
class Food:
    def __init__(self, image_path):
        self.rect = self.generate_food_rect()
        self.weight = random.randint(1, 5)
        self.creation_time = time.time()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (cell_size, cell_size))

    def generate_food_rect(self):
        while True:
            x = random.randint(0, (width - cell_size) // cell_size) * cell_size
            y = random.randint(0, (height - cell_size) // cell_size) * cell_size
            if [x, y] not in snake_body:
                return pygame.Rect(x, y, cell_size, cell_size)

    def is_expired(self, expiration_time=5):
        return time.time() - self.creation_time > expiration_time

# Create the apples
gold_apple = Food("apple.png")
silver_apple = Food("green.jpg")  # Changed green.png to green.jpg

# Font to display score and level
font = pygame.font.SysFont("Verdana", 20)

# Set initial direction and game control variables
direction = 'RIGHT'
change_to = direction
clock = pygame.time.Clock()
score = 0
level = 1
speed = 10
Running = True

# Main game loop
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'

    direction = change_to

    if direction == 'UP':
        snake_pos[1] -= cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size

    snake_pos[0] %= width
    snake_pos[1] %= height

    snake_body.insert(0, list(snake_pos))

    # Check collision with apples
    ate_gold = pygame.Rect(snake_pos[0], snake_pos[1], cell_size, cell_size).colliderect(gold_apple.rect)
    ate_silver = pygame.Rect(snake_pos[0], snake_pos[1], cell_size, cell_size).colliderect(silver_apple.rect)

    if ate_gold:
        score += gold_apple.weight
        if score // 4 + 1 > level:
            level += 1
            speed += 2
        gold_apple = Food("apple.png")
    elif ate_silver:
        score += silver_apple.weight * 2  # Silver apple gives double points
        if score // 4 + 1 > level:
            level += 1
            speed += 2
        silver_apple = Food("green.jpg")  # Changed green.g to green.jpg
    else:
        snake_body.pop()

    # Expire apples if too old
    if gold_apple.is_expired():
        gold_apple = Food("apple.png")
    if silver_apple.is_expired():
        silver_apple = Food("green.jpg")  # Changed green.png to green.jpg

    screen.fill(black)
    screen.blit(gold_apple.image, gold_apple.rect.topleft)
    screen.blit(silver_apple.image, silver_apple.rect.topleft)

    for block in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))

    score_text = font.render(f"Score: {score}", True, white)
    level_text = font.render(f"Level: {level}", True, white)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (400, 10))

    pygame.display.flip()
    clock.tick(speed)
