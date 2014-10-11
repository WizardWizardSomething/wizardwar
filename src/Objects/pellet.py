from __future__ import division
import os
import cocos
from cocos.collision_model import CircleShape
from cocos.euclid import Vector2
from pyglet import image


class Pellet(cocos.sprite.Sprite):
    def __init__(self, pos, angle):
        super( Pellet, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/Pellet.png')))
        self.initialPosition = pos
        self.position = (pos)
        self.angle = angle
        self.time_alive = 0
        self.cshape = CircleShape(Vector2(self.get_rect().center[0], self.get_rect().center[1]), self.width/2)

    def updateCollisionPos(self):
        self.cshape.center = Vector2(self.get_rect().center[0], self.get_rect().center[1])
        self.cshape.r = self.width/2