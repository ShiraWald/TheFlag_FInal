import pygame
import consts
import random


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
        grass_img = pygame.transform.scale(grass_img,
                                          (consts.FLAG_ROWS * consts.CELL_SIZE, consts.FLAG_COLS * consts.CELL_SIZE))
        grass_list = random_grass_pos()

        for pos in grass_list:
                screen.blit(grass_img, pos)




def draw_flag():
        flag_img = pygame.image.load(consts.FLAG_IMG)
        flag_img = pygame.transform.smoothscale(flag_img,
                                          (consts.FLAG_ROWS * consts.CELL_SIZE, consts.FLAG_COLS * consts.CELL_SIZE))
        flag_rect = flag_img.get_rect()
        screen.blit(flag_img, flag_rect)

def draw_game():
        screen.fill(consts.BACKGROUND_COLOR)
        draw_flag()
        draw_grass()
        pygame.display.flip()


