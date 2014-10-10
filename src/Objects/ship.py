import os
import cocos
from cocos.sprite import *
from pyglet import image
from cocos.actions import *


class Ship( ):
    def __init__(self):
        # super( Ship, self ).__init()

        pic = image.load(os.path.normpath(r'../assets/Graphics/BookCraft.png'))
        self.sprite = Sprite(pic, (250, 250))

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
        self.sprite.do(move)

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

    def draw(self):
        self.sprite.draw()

    def rotate(self, ):
        pass