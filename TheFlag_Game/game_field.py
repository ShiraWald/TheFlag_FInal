
import pygame
import consts
import random

board=[]
#a
def create_clear_board():
    for row in range(consts.BOARD_ROWS):
        current_row=[]
        for col in range(consts.BOARD_COLS):
            current_row.append(consts.GRASS_SIGN)
        board.append(current_row)

def solider_location(current_location):
    r = consts.SOLDIER_ROWS
    c = consts.SOLDIER_COLS
    sign = consts.SOLIDER_SIGN
    solider_in_lst=[]
    for row in range(r):
        y = current_location[0]+row
        current=[]
        for col in range(c):
            x = current_location[1]+col
            # board[y][x]=sign
            current.append((x,y))
        solider_in_lst.append(current)
    return solider_in_lst


def check_near_mines(row,col):
    if board[row][col]!=consts.GRASS_SIGN:
        return False
    if board[row][col+1]!=consts.GRASS_SIGN:
        return False
    if board[row][col+2] != consts.GRASS_SIGN:
        return False
    else:
        return True


def mines_locations():
    mines_x = random.sample(range(1,consts.BOARD_COLS-consts.MINE_COLS), consts.MINES_COUNT)
    mines_y = random.sample(range(consts.SOLDIER_ROWS,consts.BOARD_ROWS), consts.MINES_COUNT)
    mines=[]
    for i in range(consts.MINES_COUNT):
        row=mines_y[i]
        col=mines_x[i]
        while not check_near_mines(row,col):
            col=random.randint(1,consts.BOARD_COLS-consts.MINE_COLS-1)
            row=random.randint(1,consts.BOARD_ROWS-1)
        board[row][col]=consts.MINE_SIGN
        board[row][col+1] = consts.MINE_SIGN
        board[row][col+2] = consts.MINE_SIGN
        mines.append((row,col))
    return mines





def flag_location():

    r=consts.FLAG_ROWS
    c=consts.FLAG_COLS
    sign=consts.FLAG_SIGN
    for row in range(r):
        y=consts.BOARD_ROWS-1-row
        for col in range(c):
            x=consts.BOARD_COLS-1
            board[y][x - col] = sign


def locate_in_board():
    create_clear_board()
    flag_location()
    mines_locations()

    # # corners=[(0,0),(0,consts.BOARD_COLS-1),(consts.BOARD_ROWS-1,0),(consts.BOARD_ROWS-1,consts.BOARD_COLS-1)]
    # flag_corner=(consts.BOARD_ROWS-1,consts.BOARD_COLS-1)
    # solider_corner=(0,0)




locate_in_board()

























