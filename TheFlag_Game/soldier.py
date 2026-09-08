import consts
import game_field
import screen
import pygame

solider_in_board=[]
def create_clear_board():
    for row in range(consts.BOARD_ROWS):
        current_row=[]
        for col in range(consts.BOARD_COLS):
            current_row.append(consts.GRASS_SIGN)
        solider_in_board.append(current_row)

def solider_location(current_location):
    r = consts.SOLDIER_ROWS
    c = consts.SOLDIER_COLS
    sign = consts.SOLIDER_SIGN
    solider_in_lst=[]
    for row in range(r):
        y = current_location[0]+row
        for col in range(c):
            x = current_location[1]+col
            solider_in_board[y][x]=sign
            solider_in_lst.append((y,x))
    return solider_in_lst

def locate_solider_pic(location):
    screen1=screen.screen
    #2





