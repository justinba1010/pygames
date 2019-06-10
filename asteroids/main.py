import pygame
from Game import Game

pygame.display.set_caption("Garbagaroids")
pygame.init()

game = Game()

while game.play:
    pygame.time.wait(20)
    game.display()
    game.update()
    