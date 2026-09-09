import screen
import pygame
import soldier
import game_field

def main():

    done = False

    screen.draw_game()
    current_solider_location = (0, 0)
    screen.draw_soldier(current_solider_location)
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    solider_new_location = (current_solider_location[0] , current_solider_location[1]-1)
                    if soldier.soldier_check_location(solider_new_location):
                        current_solider_location = solider_new_location
                        screen.draw_soldier(current_solider_location)

                elif event.key == pygame.K_DOWN:
                    solider_new_location = (current_solider_location[0], current_solider_location[1]+1)
                    if soldier.soldier_check_location(solider_new_location):
                        current_solider_location = solider_new_location
                        screen.draw_soldier(current_solider_location)
                elif event.key == pygame.K_LEFT:
                    solider_new_location = (current_solider_location[0]-1, current_solider_location[1] )
                    if soldier.soldier_check_location(solider_new_location):
                        current_solider_location = solider_new_location
                        screen.draw_soldier(current_solider_location)
                elif event.key == pygame.K_RIGHT:
                    solider_new_location = (current_solider_location[0]+1, current_solider_location[1] )
                    if soldier.soldier_check_location(solider_new_location):
                        current_solider_location = solider_new_location
                        screen.draw_soldier(current_solider_location)
                if soldier.soldier_check_mine(current_solider_location):
                    print("boom")



main()


