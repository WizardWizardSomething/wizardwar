from __future__ import division
import os
import cocos
from cocos.sprite import *
from pyglet import image
from cocos.actions import *


class PropulsionModule(cocos.sprite.Sprite):
    def __init__(self):
        super( PropulsionModule, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/PropulsionModule.png')))
        pass