import pygame, sys, random, time

from pygame.locals import *


def main():
    global FPSCLOCK, DISPLAY, BASICFONT, BLACK, WHITE, RED, GREY, GREEN, pause

    pygame.init()
    DISPLAY = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Snake')
    FPSCLOCK = pygame.time.Clock()
    BASICFONT = pygame.font.SysFont("SIMYOU.TTF", 80)

    BLACK = pygame.Color(0, 0, 0)
    WHITE = pygame.Color(255, 255, 255)
    RED = pygame.Color(255, 0, 0)
    GREY = pygame.Color(150, 150, 150)
    GREEN = pygame.Color(30, 255, 30)

    play_game()


def play_game():
    pause = 1
    snake_Head = [100, 100]
    snake_Body = [[80, 100], [60, 100], [40, 100]]
    direction = "right"

    food_Position = [300, 300]
    food_flag = 1

    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'

    '''游戏的主循环'''
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                if (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                if (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                if event.key == K_p:
                    pause *= -1

        if pause == 1:
            if direction == LEFT:
                snake_Head[0] -= 20
            if direction == RIGHT:
                snake_Head[0] += 20
            if direction == UP:
                snake_Head[1] -= 20
            if direction == DOWN:
                snake_Head[1] += 20

            snake_Body.insert(0, list(snake_Head))

            if snake_Head[0] == food_Position[0] and snake_Head[1] == food_Position[1]:
                food_flag = 0
            else:
                snake_Body.pop()

        if food_flag == 0:
            x = random.randrange(1, 32)
            y = random.randrange(1, 24)
            food_Position = [int(x * 20), int(y * 20)]
            food_flag = 1

        DISPLAY.fill(BLACK)
        draw_snake(snake_Body)
        draw_food(food_Position)
        draw_score(len(snake_Body) - 3)
        pygame.display.flip()
        FPSCLOCK.tick(7)
        if pause == -1:
            draw_pause()

        if snake_Head[0] < 0 or snake_Head[0] > 620:
           game_over()
        if snake_Head[1] < 0 or snake_Head[1] > 460:
            game_over()
        for i in snake_Body[1:]:
            if snake_Head[0] == i[0] and snake_Head[1] == i[1]:
                game_over()


def draw_snake(snake_Body):
    for i in snake_Body:
        pygame.draw.rect(DISPLAY, WHITE, Rect(i[0], i[1], 20, 20))


def draw_food(food_Position):
    pygame.draw.rect(DISPLAY, RED, Rect(food_Position[0], food_Position[1], 20, 20))


def draw_score(score):
    score_Surf = BASICFONT.render('%s' % (score), True, GREY)
    score_Rect = score_Surf.get_rect()
    score_Rect.midtop = (320, 240)
    DISPLAY.blit(score_Surf, score_Rect)


def draw_pause():
    score_Surf = BASICFONT.render('PAUSED', True, GREY)
    score_Rect = score_Surf.get_rect()
    score_Rect.midtop = (320, 60)
    DISPLAY.blit(score_Surf, score_Rect)


def game_over():
    GameOver_Surf = BASICFONT.render('Game Over!', True, GREY)
    GameOver_Rect = GameOver_Surf.get_rect()
    GameOver_Rect.midtop = (320, 10)
    DISPLAY.blit(GameOver_Surf, GameOver_Rect)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()