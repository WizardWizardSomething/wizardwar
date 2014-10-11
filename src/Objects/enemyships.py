from __future__ import division
import os
import cocos
from pyglet import image
from cocos.actions import *
import math


class Enemy(cocos.sprite.Sprite):
    def __init__(self, pos, angle, speed):
        super( Enemy, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/IAmABall.png')))
        self.position = pos
        self.health = 100
        self.angle = angle
        self.speed = speed

    def fly(self):
        newPoint = self.point_pos(self.position[0], self.position[1], -self.speed, self.angle)
        self.do(MoveTo(newPoint))

    def point_pos(self, x0, y0, d, theta):
        theta_rad = math.pi/2 - math.radians(theta)
        return x0 + d*math.cos(theta_rad), y0 + d*math.sin(theta_rad)