import random
import os
import time

# Game settings
width = 20
height = 10
snake = [(5, 5)]
direction = 'RIGHT'
food = ()
score = 0

# Generate food
def place_food():
    while True:
        f = (random.randint(1, height - 2), random.randint(1, width - 2))
        if f not in snake:
            return f

food = place_food()

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the game board
def display():
    clear()
    print(f"Score: {score}")
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                print("#", end='')
            elif (i, j) == food:
                print("@", end='')
            elif (i, j) in snake:
                print("O", end='')
            else:
                print(" ", end='')
        print()

# Move the snake
def move():
    head = snake[0]
    if direction == 'UP':
        new_head = (head[0] - 1, head[1])
    elif direction == 'DOWN':
        new_head = (head[0] + 1, head[1])
    elif direction == 'LEFT':
        new_head = (head[0], head[1] - 1)
    elif direction == 'RIGHT':
        new_head = (head[0], head[1] + 1)

    if (
        new_head in snake or
        new_head[0] == 0 or new_head[0] == height - 1 or
        new_head[1] == 0 or new_head[1] == width - 1
    ):
        return False

    snake.insert(0, new_head)
    if new_head == food:
        global food, score
        food = place_food()
        score += 1
    else:
        snake.pop()

    return True

# Main game loop
def game():
    global direction
    display()
    while True:
        time.sleep(0.3)
        if not move():
            print("Game Over! Final Score:", score)
            break
        display()
        # Read input without blocking
        if os.name == 'nt':
            import msvcrt
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                if key == 'w' and direction != 'DOWN':
                    direction = 'UP'
                elif key == 's' and direction != 'UP':
                    direction = 'DOWN'
                elif key == 'a' and direction != 'RIGHT':
                    direction = 'LEFT'
                elif key == 'd' and direction != 'LEFT':
                    direction = 'RIGHT'
        else:
            import sys, select
            if select.select([sys.stdin], [], [], 0.0)[0]:
                key = sys.stdin.read(1).lower()
                if key == 'w' and direction != 'DOWN':
                    direction = 'UP'
                elif key == 's' and direction != 'UP':
                    direction = 'DOWN'
                elif key == 'a' and direction != 'RIGHT':
                    direction = 'LEFT'
                elif key == 'd' and direction != 'LEFT':
                    direction = 'RIGHT'

game()
