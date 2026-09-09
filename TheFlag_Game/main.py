import screen
import pygame
import soldier
import game_field
import consts

mine_locations = game_field.mines_locations()
def main():
    done = False


    current_solider_location = (0, 0)
    screen.draw_game(current_solider_location)
    screen.draw_soldier(current_solider_location)
    screen.start_message()
    pygame.time.wait(1000)
    screen.draw_game(current_solider_location)
    screen.draw_soldier(current_solider_location)
    finish = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if not finish:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        solider_new_location = (current_solider_location[0] - 1, current_solider_location[1])
                        if soldier.soldier_check_location(solider_new_location):
                            current_solider_location = solider_new_location
                            screen.draw_soldier(current_solider_location)
                            screen.draw_normal(current_solider_location)

                    elif event.key == pygame.K_DOWN:
                        solider_new_location = (current_solider_location[0] + 1, current_solider_location[1])
                        if soldier.soldier_check_location(solider_new_location):
                            current_solider_location = solider_new_location
                            screen.draw_soldier(current_solider_location)
                            screen.draw_normal(current_solider_location)


                    elif event.key == pygame.K_LEFT:
                        solider_new_location = (current_solider_location[0], current_solider_location[1] - 1)
                        if soldier.soldier_check_location(solider_new_location):

                            current_solider_location = solider_new_location
                            screen.draw_soldier(current_solider_location)
                            screen.draw_normal(current_solider_location)


                    elif event.key == pygame.K_RIGHT:
                        solider_new_location = (current_solider_location[0], current_solider_location[1] + 1)
                        if soldier.soldier_check_location(solider_new_location):
                            current_solider_location = solider_new_location
                            screen.draw_soldier(current_solider_location)
                            screen.draw_normal(current_solider_location)


                    elif event.key == pygame.K_KP_ENTER:
                        screen.night_vision(current_solider_location , mine_locations)
                        pygame.time.wait(1000)
                        screen.draw_soldier(current_solider_location)
                        screen.draw_normal(current_solider_location)

                    if soldier.soldier_check_mine(current_solider_location):
                        screen.draw_explosion(current_solider_location)
                        print(f"boom in {current_solider_location}")
                        screen.draw_message(consts.MESSAGE_LOSE)
                        finish = True


                    if soldier.soldier_check_flag(current_solider_location):
                        print("flaggg")
                        screen.draw_message(consts.MESSAGE_WIN)
                        finish = True



main()
