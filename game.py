import pygame
import random
import sys
import os

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 40)

def draw_pipes(win, pipes):
    for pipe in pipes:
        pygame.draw.rect(win, GREEN, pipe)

def create_pipe():
    height = random.randint(100, 400)
    top = pygame.Rect(WIDTH, 0, 70, height)
    bottom = pygame.Rect(WIDTH, height + 150, 70, HEIGHT)
    return top, bottom

def game_loop():
    # Game variables
    gravity = 0.5
    bird_movement = 0
    bird = pygame.Rect(100, 300, 30, 30)

    pipe_velocity = 3
    pipes = []
    pipes.extend(create_pipe())

    clock = pygame.time.Clock()
    score = 0
    running = True

    while running:
        win.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = -8

        bird_movement += gravity
        bird.y += int(bird_movement)

        # Draw bird
        pygame.draw.rect(win, WHITE, bird)

        # Move pipes
        for pipe in pipes:
            pipe.x -= pipe_velocity
        if pipes[0].x < -70:
            pipes.pop(0)
            pipes.pop(0)
            pipes.extend(create_pipe())
            score += 1

        draw_pipes(win, pipes)

        # Collision
        for pipe in pipes:
            if bird.colliderect(pipe):
                running = False
        if bird.top <= 0 or bird.bottom >= HEIGHT:
            running = False

        # Score
        score_text = font.render(f"Score: {score}", True, BLACK)
        win.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

    game_over_screen(score)

def game_over_screen(score):
    while True:
        win.fill(BLACK)
        over_text = font.render("Game Over!", True, WHITE)
        score_text = font.render(f"Final Score: {score}", True, WHITE)
        restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)

        win.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 60))
        win.blit(score_text, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
        win.blit(restart_text, (WIDTH // 2 - 180, HEIGHT // 2 + 20))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    os.execv(sys.executable, ['python'] + sys.argv)
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# Start the game
game_loop()
   
