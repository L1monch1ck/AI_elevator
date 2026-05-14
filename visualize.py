import pygame
import time

from environment import MazeEnv
from agent import QLearningAgent

pygame.init()

env = MazeEnv()
agent = QLearningAgent()

CELL = 100

WIDTH = env.size * CELL
HEIGHT = env.size * CELL + 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Maze AI")

font = pygame.font.SysFont("Arial", 28)

clock = pygame.time.Clock()

# COLORS
BG = (15, 18, 28)
PATH = (35, 40, 60)
WALL = (120, 90, 255)
TRAP = (255, 90, 90)
GOAL = (0, 255, 170)
AI = (0, 200, 255)

try:
    agent.load()
except:
    pass

state = env.reset()

episodes = 0
steps = 0
episode_reward = 0

speed = 0.1

running = True

while running:

    screen.fill(BG)

    # EVENTS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_s:
                agent.save()

            if event.key == pygame.K_UP:
                speed = max(0.02, speed - 0.02)

            if event.key == pygame.K_DOWN:
                speed += 0.02

    # DRAW MAP
    for r in range(env.size):

        for c in range(env.size):

            color = PATH

            if (r, c) in env.walls:
                color = WALL

            if (r, c) in env.traps:
                color = TRAP

            if (r, c) == env.goal:
                color = GOAL

            rect = pygame.Rect(
                c * CELL + 5,
                r * CELL + 5,
                CELL - 10,
                CELL - 10
            )

            pygame.draw.rect(
                screen,
                color,
                rect,
                border_radius=18
            )

    # AI MOVE
    action = agent.choose_action(state)

    next_state, reward, done = env.step(action)

    agent.update(state, action, reward, next_state)

    state = next_state

    steps += 1
    episode_reward += reward

    # RESET
    if done:

        episodes += 1

        steps = 0
        episode_reward = 0

        state = env.reset()

    # DRAW AI
    x, y = env.agent_pos

    cx = y * CELL + CELL // 2
    cy = x * CELL + CELL // 2

    pygame.draw.circle(screen, AI, (cx, cy), 24)

    # INFO
    info = (
        f"Episodes: {episodes}    "
        f"Steps: {steps}    "
        f"Reward: {episode_reward}"
    )

    text = font.render(info, True, (255, 255, 255))

    screen.blit(text, (20, HEIGHT - 55))

    pygame.display.update()

    time.sleep(speed)

    clock.tick(60)

pygame.quit()