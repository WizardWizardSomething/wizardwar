import cocos
from Layers import titleText
import pyglet
from cocos.audio.pygame.music import *
import os
from Objects import ship

#test imports
from pyglet.window import key

class CombatScene( cocos.scene.Scene ):
    def __init__(self):
        super( CombatScene, self ).__init__()

        # Initialize the ship
        self.bookCraft = ship.Ship()
        self.add(self.bookCraft )

        self.schedule_interval(self.mainCombatTimer, 0.05)
        #self.mainCombatTimer(10)

    def on_mouse_motion(self, x, y, dx, dy):
        print dx, dy

    def on_mouse_press(self, *args):
        print args

    def on_key_press(self, key, modifiers):
        # Determine what direction the ship is moving
        if key==pyglet.window.key.W:
            self.bookCraft.craftMovingUp = True
        if key==pyglet.window.key.S:
            self.bookCraft.craftMovingDown = True
        if key==pyglet.window.key.A:
            self.bookCraft.craftMovingLeft = True
        if key==pyglet.window.key.D:
            self.bookCraft.craftMovingRight = True

    def on_key_release(self, key, modifiers):
        if key == pyglet.window.key.W:
            self.bookCraft.craftMovingUp = False
        if key == pyglet.window.key.S:
            self.bookCraft.craftMovingDown = False
        if key == pyglet.window.key.A:
            self.bookCraft.craftMovingLeft = False
        if key == pyglet.window.key.D:
            self.bookCraft.craftMovingRight = False


    def on_key_release(self,key,modifiers):
        pass

    def on_enter(self):
        super(CombatScene,self).on_enter()
        cocos.director.director.window.push_handlers(self)

    def on_exit(self):
        super(CombatScene,self).on_exit()
        cocos.director.director.window.remove_handlers(self)

    # The update loop for the combat scene
    def mainCombatTimer(self, test):
        self.bookCraft.updateCraftVelocity()
