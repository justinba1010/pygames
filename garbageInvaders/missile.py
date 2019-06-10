# Copyright 2019 Justin Baum

from PhysicsObject import PhysicsObject
import random

kMaxVel = 4
kColor = (0, 0, 255)


class Missile(PhysicsObject):
    def __init__(self, window, x):
        PhysicsObject.__init__(self, window, (0, 255, 0))
        self.x = x
        self.y = 0
        self.height = 30
        self.width = 10
        self.fall = False
        self.allowOffscreen = False
        self.velocity = (1, 0)
        self.color = kColor

    def handleWall(self):
        PhysicsObject.handleWall(self)
        self.velocity = (-1 * self.velocity[0], self.velocity[1])
        self.y += self.height * 2
