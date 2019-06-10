# Copyright 2019 Justin Baum

from PhysicsObject import PhysicsObject
import random

kMaxVel = 4
kColor = (0, 0, 255)
class Missile(PhysicsObject):
    def __init__(self, window, x, y):
        PhysicsObject.__init__(self, window, (0, 255, 0))
        self.x = x
        self.y = y
        self.height = 30
        self.width = 10
        self.fall = False
        self.allowOffscreen = False
        self.velocity = (0,-1)
        self.color = kColor
    def handleWall(self):
        pass
        


