import cocos
from Layers import titleText
import pyglet
from cocos.audio.pygame.music import *
import os


class CombatScene( cocos.scene.Scene ):
    def __init__(self):
        super( CombatScene, self ).__init__()
        # self.enable_handlers()

    def on_enter(self):
        super(CombatScene,self).on_enter()
        cocos.director.director.window.push_handlers(self)

    def on_exit(self):
        super(CombatScene,self).on_exit()
        cocos.director.director.window.remove_handlers(self)