# Copyright 2019

import pygame
from Missile import Missile

def alwaysRun():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:             
            pygame.quit()
            quit()

def collisions(player, enemies, missiles, score):
    for enemy in enemies:
        if player.collision(enemy):
            print("Collision")             
            pygame.quit()
            quit()
        for missile in missiles:
            if missile.collision(enemy):
                enemies.remove(enemy)
                missiles.remove(missile)
                score[0] += 3
                break
            elif missile.offScreen:
                score[0] -= 1
                missiles.remove(missile)
lastshot = 0
def shoot(window, player, missiles):
    global lastshot
    if pygame.time.get_ticks() - lastshot > 100:
        lastshot = pygame.time.get_ticks()
        missiles.append(Missile(window, player.x + player.width//2, player.y))

def handleEvents(window, player, enemies, missiles, score):
    keys = pygame.key.get_pressed()
    alwaysRun()
    if keys[pygame.K_UP]:
        player.jump()
    if keys[pygame.K_RIGHT]:
        player.right()
    if keys[pygame.K_LEFT]:
        player.left()
    if keys[pygame.K_SPACE]:
        shoot(window, player, missiles)
    collisions(player, enemies, missiles, score)
    for enemy in enemies:
        enemy.update()
        enemy.show()
    for missile in missiles:
        missile.update()
        missile.show()
    player.update()
    player.show()



    