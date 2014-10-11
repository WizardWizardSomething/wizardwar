from __future__ import division
import os
import cocos
from pyglet import image


class Pellet(cocos.sprite.Sprite):
    def __init__(self, pos, angle):
        super( Pellet, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/Pellet.png')))
        self.initialPosition = pos
        self.position = (pos)
        self.angle = angle
        self.time_alive = 0