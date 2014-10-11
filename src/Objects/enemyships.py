from __future__ import division
import os
import cocos
from cocos.collision_model import CircleShape
from pyglet import image
from cocos.actions import *
from cocos.euclid import Vector2
import math


class Enemy(cocos.sprite.Sprite):
    def __init__(self, pos, angle, speed):
        super( Enemy, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/IAmABall.png')))
        self.position = pos
        self.health = 100
        self.angle = angle
        self.speed = speed
        self.time_alive = 0
        self.cshape = CircleShape(Vector2(self.get_rect().center[0], self.get_rect().center[1]), self.width/1.5)

    def fly(self):
        newPoint = self.point_pos(self.position[0], self.position[1], -self.speed, self.angle)
        self.do(MoveTo(newPoint))

    def point_pos(self, x0, y0, d, theta):
        theta_rad = math.pi/2 - math.radians(theta)
        return x0 + d*math.cos(theta_rad), y0 + d*math.sin(theta_rad)

    def updateCollisionPos(self):
        self.cshape.center = Vector2(self.get_rect().center[0], self.get_rect().center[1])
        self.cshape.r = self.width/2