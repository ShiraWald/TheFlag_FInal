import screen
import pygame

done = False

screen.draw_game()
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
