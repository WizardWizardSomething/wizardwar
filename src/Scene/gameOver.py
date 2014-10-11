import cocos
import os
import pyglet


class gameOver(cocos.scene.Scene):
    def __init__(self):
        super(gameOver, self).__init__()
        bg = cocos.sprite.Sprite(pyglet.image.load(os.path.normpath(r'../assets/Graphics/gameover.png')))
        bg.position = (cocos.director.director.get_window_size()[0]/2,cocos.director.director.get_window_size()[1]/2)
        self.add(bg)