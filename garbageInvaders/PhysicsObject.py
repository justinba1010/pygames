# Copyright 2019 Justin Baum

import pygame
import constants

kHeight = 60
kWidth = 40
kColor = (255, 0, 0)
kGravity = 0.03
kJump = -3

class PhysicsObject:
    def __init__(self, window, color = kColor):
        self.x = 50
        self.y = 50
        self.height = kHeight
        self.width = kWidth
        self.window = window
        self.velocity = (0,0)
        self.ground = False
        self.color = color
        self.fall = False
        self.offScreen = False
        self.allowOffScreen = False
        self.lastTime = pygame.time.get_ticks()
    def show(self):
        pygame.draw.rect(
            self.window,
            self.color,
            (
                int(self.x),
                int(self.y),
                self.width,
                self.height
            )
        )
    def jump(self):
        if self.ground:
            self.velocity = (self.velocity[0], kJump)
    def left(self):
        self.x -= 3
    def right(self):
        self.x += 3
    def collision(self, other):
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        cross1 = x1 >= (other.x) and x1 <= (other.x + other.width) and y1 >= (other.y) and y1 <= (other.y + other.height)
        cross2 = x2 >= (other.x) and x2 <= (other.x + other.width) and y2 >= (other.y) and y2 <= (other.y + other.height)
        return cross1 or cross2
    def handleWall(self):
        self.x = 0 if self.x < 0 else constants.screen_width - self.width if self.x > constants.screen_width - self.width else self.x
        self.y = 0 if self.y < 0 else constants.screen_width - self.height if self.y > constants.screen_width - self.height else self.y
        
    def update(self):
        # Check Jump state
        ticks = (pygame.time.get_ticks() - self.lastTime)
        if self.fall:
            if self.y < (constants.screen_width - self.height):
                self.velocity = (self.velocity[0], self.velocity[1] + kGravity*ticks)
                self.ground = False
            if self.y >= (constants.screen_width - self.height):
                self.y = constants.screen_width - self.height
                self.ground = True
                self.velocity = (self.velocity[0], 0 if self.velocity[1] > 0 else self.velocity[1])
        self.lastTime = pygame.time.get_ticks()
        self.x += self.velocity[0]*ticks
        self.y += self.velocity[1]*ticks
        self.offScreen = (self.x > constants.screen_width - self.width or self.x < 0)
        self.offScreen = self.offScreen or (self.y > constants.screen_width - self.width or self.y < 0)
        if self.offScreen and not self.allowOffScreen:
            self.handleWall()
        

        