import cocos
import os
import pyglet
from cocos.audio.pygame.music import *

class gameOver(cocos.scene.Scene):
    def __init__(self):
        super(gameOver, self).__init__()
        bg = cocos.sprite.Sprite(pyglet.image.load(os.path.normpath(r'../assets/Graphics/gameover.png')))
        bg.position = (cocos.director.director.get_window_size()[0]/2,cocos.director.director.get_window_size()[1]/2)
        self.add(bg)

    def on_enter(self):
        super(gameOver,self).on_enter()
        if(not get_busy()):
            load(os.path.normpath(r'../assets/VEC3 FX Impact 50.wav'))
            set_volume(1)
            play(loops=0)

    def on_exit(self):
        super(gameOver,self).on_exit()
        stop()