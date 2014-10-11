import cocos
from Layers import titleText
from cocos.scenes import FlipX3DTransition
import pyglet
from cocos.audio.pygame.music import *
import os
from Scene import combatScene


class mainMenu(cocos.scene.Scene):
    title = None
    def __init__(self):
        super(mainMenu, self).__init__()
        background = cocos.sprite.Sprite(pyglet.image.load(os.path.normpath(r'../assets/Graphics/background.jpg')))
        self.add(background)
        self.title = titleText.titleText()
        self.add(self.title)
        mixer.init()

    def on_key_press(self,key,modifiers):
        if(key==pyglet.window.key.DOWN):
            self.title.changeCursor(self.title.cursorPosition+1)
        elif(key==pyglet.window.key.UP):
            self.title.changeCursor(self.title.cursorPosition-1)
        elif(key==pyglet.window.key.ENTER):
            if(self.title.cursorPosition==1):
                exit()
            elif(self.title.cursorPosition==0):
                nextScene = combatScene.CombatScene()
                set_volume(0)
                cocos.director.director.replace(FlipX3DTransition(nextScene,duration=1))

    def on_enter(self):
        super(mainMenu,self).on_enter()
        load(os.path.normpath(r'../assets/RoRNewTheme.mp3'))
        play(loops=-1)
        cocos.director.director.window.push_handlers(self)

    def on_exit(self):
        super(mainMenu,self).on_exit()
        cocos.director.director.window.remove_handlers(self)
        stop()

