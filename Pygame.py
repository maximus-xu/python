import math
import pygame
import random
import sys
import time
from pygame.locals import *

pygame.init()
WIDTH = 1500
HEIGHT = 900
FPSCLOCK = pygame.time.Clock()
BLOCK_SIZE = 20
BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))


class Colors:
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREY = pygame.Color(150, 150, 150)
    GREY2 = pygame.Color(50, 50, 50)
    BLUE = pygame.Color(100, 150, 255)
    YELLOW = pygame.Color(255, 255, 0)


class Directions:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'


class Distances:
    VERY_FAR = 'very far'
    FAR = 'far'
    MEDIUM = 'medium'
    CLOSE = 'close'
    VERY_CLOSE = 'very close'

    speed_map = {
        VERY_FAR: 25,
        FAR: 25,
        MEDIUM: 20,
        CLOSE: 15,
        VERY_CLOSE: 10,
    }


def draw_rect(coordinates, color, size=BLOCK_SIZE):
    pygame.draw.rect(DISPLAY, color, Rect(coordinates[0], coordinates[1], size, size))


def draw_circle(coordinates, color, size=BLOCK_SIZE):
    pygame.draw.circle(DISPLAY, color, (coordinates[0], coordinates[1]), size)


def random_color():
    color = lambda: random.randint(50, 255)
    return pygame.Color(color(), color(), color())


def draw_text(text, x, y):
    score_Surf = BASICFONT.render(text, True, Colors.GREY)
    score_Rect = score_Surf.get_rect()
    score_Rect.midtop = (x, y)
    DISPLAY.blit(score_Surf, score_Rect)


def game_over():
    GameOver_Surf = BASICFONT.render('Game Over!', True, Colors.GREY)
    GameOver_Rect = GameOver_Surf.get_rect()
    GameOver_Rect.midtop = (WIDTH/2, 10)
    DISPLAY.blit(GameOver_Surf, GameOver_Rect)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()


def new_coin():
    global size
    return [(random.randrange(1, math.floor(WIDTH/size))) * size, (random.randrange(1, math.floor(HEIGHT/size))) * size]


size = BLOCK_SIZE
body = [[0, 0], [20, 0], [40, 0]]
coin_location = new_coin()
score = 0
pygame.init()
event = pygame.event
fps = 10
direction = Directions.RIGHT
coin_color = Colors.BLACK
distance = None

while True:
    head = body[-1].copy()

    FPSCLOCK.tick(fps)

    DISPLAY.fill(Colors.BLACK)

    for item in body:
        draw_rect(item, Colors.WHITE)

    draw_rect(coin_location, Colors.YELLOW)
    draw_text(str(score), WIDTH/2, HEIGHT/2)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            direction_map = {
                K_w: Directions.UP,
                K_UP: Directions.UP,
                K_a: Directions.LEFT,
                K_LEFT: Directions.LEFT,
                K_s: Directions.DOWN,
                K_DOWN: Directions.DOWN,
                K_d: Directions.RIGHT,
                K_RIGHT: Directions.RIGHT
            }
            direction = direction_map.get(event.key, direction)

    if direction == Directions.UP:
        head[1] -= size
    elif direction == Directions.LEFT:
        head[0] -= size
    elif direction == Directions.DOWN:
        head[1] += size
    elif direction == Directions.RIGHT:
        head[0] += size

    body = body[1:]
    body += [head]

    if head[0] > WIDTH - size or head[0] < 0:
        game_over()
        break
    if head[1] > HEIGHT - size or head[1] < 0:
        game_over()
        break

    if head == coin_location:
        coin_location = new_coin()
        score += 1



'''
size = BLOCK_SIZE
head = [size, size]
move = [1, 1]
pygame.init()
color = random_color()
bounced = 0
fps = 5000

bounce_map = {0: WIDTH, 1: HEIGHT}
stop = False


while not stop:
    stop = check_quit()
    DISPLAY.fill(Colors.BLACK)
    draw_circle(head, color)
    draw_text(str(bounced))
    pygame.display.flip()

    for k, v in bounce_map.items():
        head[k] += move[k]
        if head[k] < size or head[k] > v - size:
            move[k] *= -1
            color = random_color()
            bounced += 1
            
            
            
            
            
            
    
    FPSCLOCK.tick(fps)
    DISPLAY.fill(Colors.BLACK)
    draw_rect(head, Colors.WHITE)
    draw_rect(coin_location, coin_color)
    draw_text(str(score), WIDTH/2, HEIGHT/2)
    draw_text(distance, WIDTH/2, HEIGHT/4)
    coin_color = Colors.BLACK
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit()
            break
        elif event.type == KEYDOWN:
            direction_map = {
                K_w: Directions.UP,
                K_UP: Directions.UP,
                K_a: Directions.LEFT,
                K_LEFT: Directions.LEFT,
                K_s: Directions.DOWN,
                K_DOWN: Directions.DOWN,
                K_d: Directions.RIGHT,
                K_RIGHT: Directions.RIGHT
            }
            direction = direction_map.get(event.key, direction)

    if direction == Directions.UP:
        head[1] -= size
    elif direction == Directions.LEFT:
        head[0] -= size
    elif direction == Directions.DOWN:
        head[1] += size
    elif direction == Directions.RIGHT:
        head[0] += size

    x_distance = abs(head[0] - coin_location[0])/size
    y_distance = abs(head[1] - coin_location[1])/size
    total_distance = (x_distance ** 2 + y_distance ** 2)**1/2
    fps = total_distance/25 + 5

    if total_distance >= 200:
        distance = Distances.VERY_FAR
    elif 200 > total_distance >= 100:
        distance = Distances.FAR
    elif 100 > total_distance >= 30:
        distance = Distances.MEDIUM
    elif 30 > total_distance >= 10:
        distance = Distances.CLOSE
    elif 10 > total_distance >= 2:
        distance = Distances.VERY_CLOSE
    else:
        coin_color = Colors.YELLOW

    if head == coin_location:
        score += 1
        coin_location = new_coin()
        coin_color = Colors.BLACK

    FPSCLOCK.tick(fps)
'''