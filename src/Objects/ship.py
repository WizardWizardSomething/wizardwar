from __future__ import division
from Objects import moduleTest
from cocos.collision_model import CircleShape
import os
import cocos
from cocos.sprite import *
from pyglet import image
from cocos.actions import *
from cocos.euclid import Vector2
import math


class Ship(cocos.sprite.Sprite):
    def __init__(self):
        super( Ship, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/BookCraft.png')))

        self.moduleDebug = moduleTest.TestModule()
        self.add(self.moduleDebug)

        self.position = (250,250)
        self.centerPoint = self.get_rect().center
        self.midline = (self.centerPoint, self.get_rect().midtop)
        self.cshape = CircleShape(Vector2(self.centerPoint[0],self.centerPoint[1]),self.width/2)

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
        self.centerPoint = self.get_AABB().center

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
        angleOfRot = math.atan2(-(mousePos[1] - self.getCenter()[1]), (mousePos[0] - self.getCenter()[0]))
        angleOfRot %= 2 * math.pi
        angleOfRot = math.degrees(angleOfRot)
        self.do(RotateTo(angleOfRot - 90, 0))

    def getCenter(self):
        return self.get_rect().center

    def getMidline(self):
        return (self.getCenter(), self.get_AABB().midtop)

    def calcVector(self, tupleOfPts):
        return(tupleOfPts[0][0]-tupleOfPts[0][1], tupleOfPts[0][1]-tupleOfPts[1][1])

    # Draw the modules on top of the ship based on the ships position and the
    # layout of the modules
    def drawModules(self):
        pass

    def updateCollisionPos(self):
        self.cshape.center = Vector2(self.centerPoint[0],self.centerPoint[1])
        self.cshape.r = self.width/2

    def reverseDirection(self):
        if(self.craftMovingLeft):
            self.craft_x_velocity = 1
        if(self.craftMovingDown):
            self.craft_y_velocity = 1
        if(self.craftMovingRight):
            self.craft_x_velocity = -1
        if(self.craftMovingUp):
            self.craft_y_velocity = -1