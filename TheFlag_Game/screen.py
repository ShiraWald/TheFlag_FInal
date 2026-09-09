import time
import pygame
import consts
import random

import game_field


screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
mine_locations = game_field.mines_locations()


def random_grass_pos():
        grass_list = []

        for j in range(consts.GRASS_AMOUNT):
                x = random.randrange(0, consts.WINDOW_WIDTH - consts.FLAG_ROWS * consts.CELL_SIZE )
                y = random.randrange(0, consts.WINDOW_HEIGHT - consts.FLAG_COLS * consts.CELL_SIZE)
                grass_list.append((x, y))
        return grass_list

grass_locations = random_grass_pos()

def draw_grass():

        grass_img = pygame.image.load(consts.GRASS_IMG)
        grass_img = pygame.transform.smoothscale(grass_img,
                                          (consts.GRASS_HEIGHT , consts.GRASS_WIDTH))
        grass_list = grass_locations

        for pos in grass_list:
                screen.blit(grass_img, pos)
        pygame.display.flip()


def draw_soldier(location):
        soldier_img = pygame.image.load(consts.SOLDIER_IMG)
        soldier_img = pygame.transform.smoothscale(soldier_img,
                                                (consts.SOLDIER_COLS * consts.CELL_SIZE,
                                                 consts.SOLDIER_ROWS * consts.CELL_SIZE))
        screen.blit(soldier_img, (location[1]*consts.CELL_SIZE,location[0]*consts.CELL_SIZE))
        pygame.display.flip()




def draw_grid():
        for x in range(0, consts.WINDOW_WIDTH , consts.CELL_SIZE):
                for y in range(0, consts.WINDOW_HEIGHT , consts.CELL_SIZE):
                        rect = pygame.Rect(x , y , consts.CELL_SIZE , consts.CELL_SIZE)
                        pygame.draw.rect(screen , consts.GRID_COLOR , rect , 1 )


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
        screen.blit(flag_img, (consts.WINDOW_WIDTH  - consts.FLAG_ROWS * consts.CELL_SIZE , consts.WINDOW_HEIGHT - consts.FLAG_COLS * consts.CELL_SIZE ))

def draw_night_soldier(location):
        soldier_night_img = pygame.image.load(consts.SOLDIER_NIGHT_IMG)
        soldier_night_img = pygame.transform.smoothscale(soldier_night_img,
                                                   (consts.SOLDIER_COLS * consts.CELL_SIZE,
                                                    consts.SOLDIER_ROWS * consts.CELL_SIZE))
        screen.blit(soldier_night_img, (location[1] * consts.CELL_SIZE, location[0] * consts.CELL_SIZE))



def start_message():
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text = my_font.render(consts.MESSAGE_TEXT , False , consts.MESSAGE_COLOR)
        screen.blit(text , (0,1))
#lo

def draw_message(message):
    pygame.font.init()
    win_location = \
        (0.2 * consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT / 2 - (65 // 2))
    my_font = pygame.font.SysFont('Comic Sans MS', 50)
    text = my_font.render(message, False, consts.MESSAGE_COLOR)
    screen.blit(text, win_location)
    pygame.display.flip()


#1

def draw_explosion(location):
        explosion_img = pygame.image.load(consts.EXPLOTION_IMG)
        explosion_img = pygame.transform.smoothscale(explosion_img,
                                                         (consts.GRASS_HEIGHT , consts.GRASS_WIDTH))
        screen.blit(explosion_img, (location[1] * consts.CELL_SIZE, (location[0] + 2) * consts.CELL_SIZE))
        pygame.display.flip()


def night_vision(location):
        screen.fill(consts.NIGHT_BACKGROUND_COLOR)
        draw_grid()
        draw_mine(mine_locations)
        draw_night_soldier(location)
        pygame.display.flip()


def draw_normal(location):
        screen.fill(consts.BACKGROUND_COLOR)
        draw_grass()
        draw_flag()
        draw_soldier(location)
        pygame.display.flip()



def draw_game(location):
        draw_normal(location)
        pygame.display.flip()


