import pygame
import eventhandler
import constants
from Enemy import Enemy
from Player import Player
from Missile import Missile
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

pygame.init()


window = pygame.display.set_mode((constants.screen_width, constants.screen_width))

pygame.display.set_caption("Garbage Invaders")

player = Player(window)

enemies = []

missiles = []

for i in range(0,800,80):
    enemies.append(Enemy(window, i))
lastEnemy = pygame.time.get_ticks()
score = [0]
while True:
    pygame.time.delay(10)
    
    # Event loop
    flytime = 500/(pow(pygame.time.get_ticks(), 0.125))
    level = min(1, 1 + score[0]/100)
    if pygame.time.get_ticks() - lastEnemy > (flytime):
        enemies.append(Enemy(window, 0, level))
        lastEnemy = pygame.time.get_ticks()
    window.fill((0,0,0))
    eventhandler.handleEvents(window, player, enemies, missiles, score)
    textsurface = myfont.render("Score: "+ str(score[0]), False, (255,255,255))
    window.blit(textsurface,(400,600))
    pygame.display.update()

