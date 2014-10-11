import cocos
from Layers import titleText
import pyglet
from cocos.audio.pygame.music import *
import os
from Objects import ship


class CombatScene( cocos.scene.Scene ):
    def __init__(self):
        super( CombatScene, self ).__init__()
        self.bookCraft = ship.Ship()
        self.add(self.bookCraft.sprite, )

    def on_mouse_motion(self, x, y, dx, dy):
        print dx, dy

    def on_mouse_press(self, *args):
        print args

    def on_enter(self):
        super(CombatScene,self).on_enter()
        cocos.director.director.window.push_handlers(self)

    def on_exit(self):
        super(CombatScene,self).on_exit()
        cocos.director.director.window.remove_handlers(self)