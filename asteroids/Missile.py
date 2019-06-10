# Copyright 2019
from PhysicsObject import PhysicsObject


class Missile(PhysicsObject):
    def __init__(self, window, playercoords, playerangle, speed=400):
        PhysicsObject.__init__(self, window, (0, 100, 255))
        self.velocity = self.get_vector(playerangle)
        self.x = playercoords[0]
        self.y = playercoords[1]
        self.height = 12
        self.width = 12
        self.velocity = (self.velocity[0] * speed, self.velocity[1] * speed)
