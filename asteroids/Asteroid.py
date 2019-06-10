# Copyright 2019 Justin Baum

from PhysicsObject import PhysicsObject
from random import randint

kDistance = 300**2
screen_width = 1000
screen_height = 800


class Asteroid(PhysicsObject):
    def __init__(self, window, playercoords, speed=75):
        PhysicsObject.__init__(self, window, (100, 100, 100))
        self.generate_coords(playercoords)
        self.height = randint(3, 7) * 7
        self.width = self.height
        self.get_velocity(playercoords, speed)

    def get_velocity(self, playercoords, speed):
        x = playercoords[0] - self.x
        y = playercoords[1] - self.y
        total = x**2 + y**2
        total **= 0.5
        x /= total
        y /= total
        x *= speed
        y *= speed
        self.velocity = (x, y)

    def generate_coords(self, playercoords):
        coords = (randint(0, screen_width), randint(0, screen_height))
        while self.get_dist(playercoords) < kDistance:
            coords = (randint(0, screen_width), randint(0, screen_height))
        self.x = coords[0]
        self.y = coords[1]
