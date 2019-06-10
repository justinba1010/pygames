# Copyright 2019 Justin Baum

from PhysicsObject import PhysicsObject
import random

kMaxVel = 4

class Enemy(PhysicsObject):
    def __init__(self, window, x = 40, vel = 1):
        PhysicsObject.__init__(self, window, (0, 255, 0))
        self.x = x
        self.y = 0
        self.height = 30
        self.width = 30
        self.fall = False
        self.allowOffscreen = False
        self.velocity = (1*vel,0)
    def handleWall(self):
        self.velocity = (-1*self.velocity[0], self.velocity[1])
        self.y += self.height*2
        self.x += self.velocity[0]*3
        

