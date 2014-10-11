import cocos
from Layers import titleText
import pyglet


class mainMenu(cocos.scene.Scene):
    title = None
    def __init__(self):
        super(mainMenu, self).__init__()
        self.enable_handlers()
        self.title = titleText.titleText()
        self.add(self.title)

    def on_key_press(self,key,modifiers):
        if(key==pyglet.window.key.DOWN):
            self.title.changeCursor(self.title.cursorPosition+1)
        elif(key==pyglet.window.key.UP):
            self.title.changeCursor(self.title.cursorPosition-1)
        elif(key==pyglet.window.key.ENTER):
            if(self.title.cursorPosition==1):
                exit()

    def on_enter(self):
        super(mainMenu,self).on_enter()
        cocos.director.director.window.push_handlers(self)

    def on_exit(self):
        super(mainMenu,self).on_exit()
        cocos.director.director.window.remove_handlers(self)

