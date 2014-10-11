import os
import cocos
from cocos.sprite import *
from pyglet import image
from cocos.actions import *


class Ship(cocos.sprite.Sprite):
    def __init__(self):
        super( Ship, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/BookCraft.png')))
        self.position = (250,250)

    def move(self, dx, dy):
        move = MoveBy((dx, dy))
        self.do(move)

    def rotate(self, ):
        pass