from __future__ import division
import os
import cocos
from cocos.sprite import *
from pyglet import image
from cocos.actions import *


class CockpitModule(cocos.sprite.Sprite):
    def __init__(self):
        super( CockpitModule, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/CockpitModule.png')))
        pass