from __future__ import division
import os
import cocos
from cocos.collision_model import CircleShape
from pyglet import image
from cocos.actions import *
from cocos.euclid import Vector2
import math


class Explosion(cocos.sprite.Sprite):
    def __init__(self, pos):
        super( Explosion, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/explodingGIF.gif')))
        self.position = pos
        self.scale = 3
        self.time_alive = 0