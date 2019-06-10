# Copyright 2019 Justin Baum

from PhysicsObject import PhysicsObject


class Player(PhysicsObject):
    def __init__(self, window):
        PhysicsObject.__init__(self, window)
        self.y = 500
        self.velocity = (0, 0)
        self.fall = True
