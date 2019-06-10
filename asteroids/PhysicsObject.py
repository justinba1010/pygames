# Copyright 2019 Justin Baum

import pygame
from math import sin, cos, radians

screen_width = 1000
screen_height = 800
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
        self.color = color
        self.off_screen = False
        self.allow_off_screen = False
        self.last_time = pygame.time.get_ticks()
    def display(self):
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
    def collision(self, other):
        x1 = self.x
        y1 = self.y
        x2 = self.x + self.width
        y2 = self.y + self.height
        cross1 = x1 >= (other.x) and x1 <= (other.x + other.width) and y1 >= (other.y) and y1 <= (other.y + other.height)
        cross2 = x2 >= (other.x) and x2 <= (other.x + other.width) and y2 >= (other.y) and y2 <= (other.y + other.height)
        return cross1 or cross2
    def handle_wall(self):
        self.x = 0 if self.x < 0 else screen_width - self.width if self.x > screen_width - self.width else self.x
        self.y = 0 if self.y < 0 else screen_height - self.height if self.y > screen_height - self.height else self.y
    def handle_wall_torus(self):
        self.x %= screen_width
        self.y %= screen_height
    def update(self):
        # Check Jump state
        ticks = (pygame.time.get_ticks() - self.last_time)/1000.0
        self.last_time = pygame.time.get_ticks()
        self.x += self.velocity[0]*ticks
        self.y += self.velocity[1]*ticks
        self.off_screen = (self.x > screen_width - self.width or self.x < 0)
        self.off_screen = self.off_screen or (self.y > screen_height - self.height or self.y < 0)
        if self.off_screen and not self.allow_off_screen:
            self.handle_wall_torus()
    def get_vector(self, angle = None):
        if angle == None:
            angle = self.angle
        return (sin(radians(angle)),cos(radians(angle)))
    def get_dist(self, coords):
        return (self.x - coords[0])**2 + (self.y - coords[1])**2
