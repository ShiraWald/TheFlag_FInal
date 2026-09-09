import consts
import game_field
import screen
import pygame

# solider_in_board=[]
# def create_clear_board():
#     for row in range(consts.BOARD_ROWS):
#         current_row=[]
#         for col in range(consts.BOARD_COLS):
#             current_row.append(consts.GRASS_SIGN)
#         solider_in_board.append(current_row)



def soldier_legs(solider_current):
    soldier = game_field.solider_location(solider_current)
    # print(f"solider = {soldier}")
    legs= soldier[len(soldier) - 1]
    # print(f" legs {legs}")
    return legs



def soldier_body(solider_current):
    soldier = game_field.solider_location(solider_current)
    body=[]
    for part in range(consts.SOLDIER_BODY_ROWS):
        body.append(soldier[part])
    print(f"body =={body}")
    return body

def soldier_check_location(solider_current):
    print(f"sol current{solider_current}")
    if solider_current[1]> consts.BOARD_COLS-consts.SOLDIER_COLS:
        return False
    if solider_current[1]<0:
        return False
    if solider_current[0]> consts.BOARD_ROWS-consts.SOLDIER_ROWS:
        return False
    if solider_current[0]<0:
        return False
    return True
#a
def soldier_check_mine(soldier_current):
    solider_cur_legs=soldier_legs(soldier_current)
    for leg in solider_cur_legs:
        if game_field.board[leg[1]][leg[0]]==consts.MINE_SIGN:
            return True
    return False
def soldier_check_flag(soldier_current):
    soldier_cur_body=soldier_body(soldier_current)
    for body_row in soldier_cur_body:
        for body_col in body_row :
            if game_field.board[body_col[1]][body_col[0]]==consts.FLAG_SIGN:
                return True
    return False

















