import os
import cocos
from cocos.sprite import *
from pyglet import image
from cocos.actions import *


class Ship( ):
    def __init__(self):
        # super( Ship, self ).__init()

        pic = image.load(os.path.normpath(r'..\assets/Graphics/BookCraft.png'))
        self.sprite = Sprite(pic, (250, 250))

    def move(self, dx, dy):
        move = MoveBy((dx, dy))
        self.sprite.do(move)

    def draw(self):
        self.sprite.draw()