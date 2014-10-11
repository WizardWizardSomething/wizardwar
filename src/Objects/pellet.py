from __future__ import division
from Objects import moduleTest
import os
import cocos
from cocos.sprite import *
from pyglet import image
from cocos.actions import *
import math


class Pellet(cocos.sprite.Sprite):
    def __init__(self, pos, angle):
        super( Pellet, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/Pellet.png')))
        self.initialPosition = pos
        self.position = (pos)
        self.angle = angle
        self.time_alive = 0