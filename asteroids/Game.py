# Copyright 2019 Justin Baum
import pygame
from Player import Player
from Asteroid import Asteroid
from Missile import Missile

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

screen_width = 1000
screen_height = 800


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((screen_width, screen_height))
        self.player = Player(self.window, screen_width // 2,
                             screen_height // 2)
        self.asteroids = []
        self.missiles = []
        self.max_asteroids = 10
        self.max_missiles = 10
        self.asteroid_time = 600
        self.missile_time = 200
        self.score = 0
        self.lives = 4
        self.play = True
        self.last_asteroid = pygame.time.get_ticks()
        self.last_missile = pygame.time.get_ticks()

    def display(self):
        self.window.fill((0, 0, 0))
        # Scroll through objects
        self.player.display()
        for asteroid in self.asteroids:
            asteroid.display()
        for missile in self.missiles:
            missile.display()
        self.display_score()
        pygame.display.update()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.left()
        if keys[pygame.K_RIGHT]:
            self.player.right()
        if keys[pygame.K_UP]:
            self.player.up()
        if keys[pygame.K_DOWN]:
            self.player.down()
        if keys[pygame.K_SPACE]:
            self.shoot()
        # Update game objects
        self.player.update()
        for asteroid in self.asteroids:
            asteroid.update()
        for missile in self.missiles:
            missile.update()
        self.generate_asteroids()
        self.collision_detection()

    def shoot(self):
        if pygame.time.get_ticks() - self.last_missile > self.missile_time:
            self.missiles.append(
                Missile(self.window, (self.player.x, self.player.y),
                        self.player.angle))
            self.last_missile = pygame.time.get_ticks()
            if len(self.missiles) > self.max_missiles:
                self.missiles = self.missiles[1:]
            self.score -= 1

    def display_score(self):
        textsurface = myfont.render("Score: " + str(self.score), False,
                                    (255, 255, 255))
        self.window.blit(textsurface, (400, 600))

    def collision_detection(self):
        for asteroid in self.asteroids:
            if self.player.collision(asteroid):
                self.reset()
                self.lives -= 1
                break
            for missile in self.missiles:
                if missile.collision(asteroid):
                    self.missiles.remove(missile)
                    self.asteroids.remove(asteroid)
                    print("Its working")
                    self.score += 50

    def reset(self):
        if self.lives == 0:
            print("Game Over")
            self.play = False
        self.missiles = []
        self.asteroids = []

    def generate_asteroids(self):
        if pygame.time.get_ticks() - self.last_asteroid > self.asteroid_time:
            self.asteroids.append(
                Asteroid(self.window, (self.player.x, self.player.y)))
            self.last_asteroid = pygame.time.get_ticks()
            if len(self.asteroids) > self.max_asteroids:
                self.asteroids = self.asteroids[1:]
