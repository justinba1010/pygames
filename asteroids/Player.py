# Copyright 2019 Justin Baum

from PhysicsObject import PhysicsObject

kSpeed = 2

class Player(PhysicsObject):
    def __init__(self, window, x, y):
        PhysicsObject.__init__(self, window)
        self.x = 500
        self.y = 400
        self.velocity = (0,0)
        self.angle = 0
    def left(self):
        self.angle += 3
        self.angle %= 360
    def right(self):
        self.angle -= 3
        self.angle %= 360
    def up(self):
        vector = self.get_vector()
        self.x += vector[0]*kSpeed
        self.y += vector[1]*kSpeed
    def down(self):
        vector = self.get_vector()
        self.x -= vector[0]*kSpeed
        self.y -= vector[1]*kSpeed