import pygame
import consts
import random
import game_field


screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def random_grass_pos():
        grass_list = []

        for j in range(consts.GRASS_AMOUNT):
                x = random.randrange(0, consts.WINDOW_WIDTH - consts.FLAG_ROWS * consts.CELL_SIZE )
                y = random.randrange(0, consts.WINDOW_HEIGHT - consts.FLAG_COLS * consts.CELL_SIZE)
                grass_list.append((x, y))
        return grass_list


def draw_grass():

        grass_img = pygame.image.load(consts.GRASS_IMG)
        grass_img = pygame.transform.smoothscale(grass_img,
                                          (consts.GRASS_HEIGHT , consts.GRASS_WIDTH))
        grass_list = random_grass_pos()

        for pos in grass_list:
                screen.blit(grass_img, pos)

def draw_grid():
        BLACK = (0,0,0)
        for x in range(0, consts.WINDOW_WIDTH , consts.CELL_SIZE):
                for y in range(0, consts.WINDOW_HEIGHT , consts.CELL_SIZE):
                        rect = pygame.Rect(x , y , consts.CELL_SIZE , consts.CELL_SIZE)
                        pygame.draw.rect(screen , BLACK , rect , 1)


def draw_mine(location):
        mine_img = pygame.image.load(consts.MINE_IMG)
        mine_img = pygame.transform.smoothscale(mine_img,
                                                 (consts.MINE_COLS * consts.CELL_SIZE, consts.MINE_ROWS * consts.CELL_SIZE))
        for mine in location:
                screen.blit(mine_img, (  mine[1] * consts.CELL_SIZE , mine[0] * consts.CELL_SIZE))




def draw_flag():
        flag_img = pygame.image.load(consts.FLAG_IMG)
        flag_img = pygame.transform.smoothscale(flag_img,
                                          (consts.FLAG_ROWS * consts.CELL_SIZE, consts.FLAG_COLS * consts.CELL_SIZE))
        flag_rect = flag_img.get_rect()
        screen.blit(flag_img, (consts.WINDOW_WIDTH  - consts.FLAG_ROWS * consts.CELL_SIZE , consts.WINDOW_HEIGHT - consts.FLAG_COLS * consts.CELL_SIZE ))


# def solider(): #not sure
#         solider_img = pygame.image.load(consts.SOLDIER_IMG)


def draw_game():
        screen.fill(consts.BACKGROUND_COLOR)
        draw_flag()
        draw_grass()
        draw_mine(game_field.mines_locations())
        draw_grid()
        pygame.display.flip()


