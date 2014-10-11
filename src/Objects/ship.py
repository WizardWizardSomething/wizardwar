from __future__ import division
import os
import cocos
from cocos.sprite import *
from pyglet import image
from cocos.actions import *
import numpy as np


class Ship(cocos.sprite.Sprite):
    def __init__(self):
        super( Ship, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/BookCraft.png')))
        self.position = (250,250)
        self.centerPoint = self.get_rect().center
        self.midline = (self.centerPoint, self.get_rect().midtop)

        # Constants for craft movement
        self.CRAFT_MAX_VELOCITY = 1000
        self.CRAFT_ACCELERATION = 100
        self.CRAFT_MAX_TURNRATE = 1

        # Keep track of the current move speed of the ship. These are accessed
        # directly by the scene controlling the ship
        self.craftMovingUp = False
        self.craftMovingDown = False
        self.craftMovingRight = False
        self.craftMovingLeft = False
        self.craft_x_velocity = 0
        self.craft_y_velocity = 0

    def move(self, dx, dy):
        move = MoveBy((dx, dy))
        self.do(move)
        self.centerPoint = self.get_rect().center

    # CMB: Does all the velocity math before updating the crafts position
    def updateCraftVelocity(self):
        # Check which directions the ship is moving, then update accordingly
        # Start with up and down movement
        if self.craftMovingUp and not self.craftMovingDown:
            if self.craft_y_velocity < self.CRAFT_MAX_VELOCITY - self.CRAFT_ACCELERATION:
                self.craft_y_velocity = self.craft_y_velocity + self.CRAFT_ACCELERATION
            else:
                self.craft_y_velocity = self.CRAFT_MAX_VELOCITY
        elif self.craftMovingDown and not self.craftMovingUp:
            if self.craft_y_velocity > (self.CRAFT_MAX_VELOCITY * -1) + self.CRAFT_ACCELERATION:
                self.craft_y_velocity = self.craft_y_velocity - self.CRAFT_ACCELERATION
            else:
                self.craft_y_velocity = self.CRAFT_MAX_VELOCITY * -1
        # Degenerate the move speed if craft is not moving
        else:
            if self.craft_y_velocity > self.CRAFT_ACCELERATION:
                self.craft_y_velocity = self.craft_y_velocity - self.CRAFT_ACCELERATION
            elif self.craft_y_velocity < (self.CRAFT_ACCELERATION * -1):
                self.craft_y_velocity = self.craft_y_velocity + self.CRAFT_ACCELERATION
            else:
                self.craft_y_velocity = 0

        # Left and Right Movement
        if self.craftMovingLeft and not self.craftMovingRight:
            if self.craft_x_velocity > (self.CRAFT_MAX_VELOCITY * -1) + self.CRAFT_ACCELERATION:
                self.craft_x_velocity = self.craft_x_velocity - self.CRAFT_ACCELERATION
            else:
                self.craft_x_velocity = self.CRAFT_MAX_VELOCITY * -1
        elif self.craftMovingRight and not self.craftMovingLeft:
            if self.craft_x_velocity < self.CRAFT_MAX_VELOCITY - self.CRAFT_ACCELERATION:
                self.craft_x_velocity = self.craft_x_velocity + self.CRAFT_ACCELERATION
            else:
                self.craft_x_velocity = self.CRAFT_MAX_VELOCITY
        # Degenerate the move speed if the craft is not moving
        else:
            if self.craft_x_velocity > self.CRAFT_ACCELERATION:
                self.craft_x_velocity = self.craft_x_velocity - self.CRAFT_ACCELERATION
            elif self.craft_x_velocity < (self.CRAFT_ACCELERATION * -1):
                self.craft_x_velocity = self.craft_x_velocity + self.CRAFT_ACCELERATION
            else:
                self.craft_x_velocity = 0

        # Physically move the ship
        self.move(self.craft_x_velocity, self.craft_y_velocity)

    def rotate(self, mousePos):
        newLine = (self.getCenter(), mousePos)

        # calculate mouse in relation to sprite
        if newLine[1][1] > self.midline[1][1]:
            if newLine[1][0] > self.midline[1][0]:
                rel = 1
            else:
                rel = -1
        else:
            if newLine[1][0] > self.midline[1][0]:
                rel = -1
            else:
                rel = 1

        centerVector = self.calcVector(self.getMidline())
        newVector = self.calcVector(newLine)
        print centerVector, newVector
        if newVector[1] < 0 and centerVector[1] < 0:
            newVector = (newVector[0], abs(newVector[1]))

        angleOfRot = self.angle_between(centerVector, newVector)
        self.do(RotateBy(angleOfRot*rel, 0))
        self.midline = self.getMidline()

    def getCenter(self):
        return self.get_AABB().center

    def getMidline(self):
        return (self.getCenter(), self.get_AABB().midtop)

    def calcVector(self, tupleOfPts):
        return(tupleOfPts[0][0]-tupleOfPts[0][1], tupleOfPts[0][1]-tupleOfPts[1][1])

    def unit_vector(self, vector):
        """ Returns the unit vector of the vector.  """
        return vector / np.linalg.norm(vector)

    def angle_between(self, v1, v2):
        v1_u = self.unit_vector(v1)
        v2_u = self.unit_vector(v2)
        angle = np.arccos(np.dot(v1_u, v2_u))
        if np.isnan(angle):
            if (v1_u == v2_u).all():
                return 0.0
            else:
                return np.pi
        return angle