import pygame, sys, random, time

from pygame.locals import *

pygame.init()
WIDTH = 640
HEIGHT = 480
FPSCLOCK = pygame.time.Clock()
BLOCK_SIZE = 10

DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))

class Colors:
    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREY = pygame.Color(150, 150, 150)
    BLUE = pygame.Color(100, 150, 255)
    YELLOW = pygame.Color(255, 255, 0)


def draw_circle(location, color, size=BLOCK_SIZE):
    pygame.draw.circle(DISPLAY, color, (location[0], location[1]), size)


def random_color():
    color = lambda: random.randint(50, 255)
    return pygame.Color(color(), color(), color())


BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)
def draw_text(text):
    score_Surf = BASICFONT.render(text, True, Colors.GREY)
    score_Rect = score_Surf.get_rect()
    score_Rect.midtop = (WIDTH/2, HEIGHT/2)
    DISPLAY.blit(score_Surf, score_Rect)


def check_quit():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_q:
            return True
    return False

size = BLOCK_SIZE
location = [size, size]
move = [1, 1]
pygame.init()
color = random_color()
bounced = 0
fps = 500

bounce_map = {0: WIDTH, 1: HEIGHT}
stop = False


while not stop:
    stop = check_quit()
    DISPLAY.fill(Colors.BLACK)
    draw_circle(location, color)
    draw_text(str(bounced))
    pygame.display.flip()

    for k, v in bounce_map.items():
        location[k] += move[k]
        if location[k] < size or location[k] > v - size:
            move[k] *= -1
            color = random_color()
            bounced += 1

    FPSCLOCK.tick(fps)
