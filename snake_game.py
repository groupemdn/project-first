# snake_game.py

import pygame
import os
import pandas 

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake settings
snake_block = 10
snake_speed = 15

# Set up the clock
clock = pygame.time.Clock()

# Font style
font_style = pygame.font.SysFont(None, 35)

# Display score
def display_score(score):
    value = font_style.render(f"Score: {score}", True, white)
    screen.blit(value, [0, 0])

# Draw the snake
def draw_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, green, [segment[0], segment[1], snake_block, snake_block])

# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting position of the snake
    x, y = width // 2, height // 2
    x_change, y_change = 0, 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, width - snake_block) / 10) * 10
    food_y = round(random.randrange(0, height - snake_block) / 10) * 10

    while not game_over:

        while game_close:
            screen.fill(black)
            msg = font_style.render("Game Over! Press C-Continue or Q-Quit", True, red)
            screen.blit(msg, [width // 6, height // 3])
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Move the snake
        x += x_change
        y += y_change

        # Check for collision with boundaries
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Draw the game
        screen.fill(blue)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
        
        # Update the snake position
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collision with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Check for eating food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10) * 10
            food_y = round(random.randrange(0, height - snake_block) / 10) * 10
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
if __name__ == "__main__":
    game_loop()

        # Draw the game
        # screen.fill(blue)
        # pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])
