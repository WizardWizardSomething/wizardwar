import cocos
from Layers import titleText

class mainMenu(cocos.scene.Scene):
    def __init__(self):
        super(mainMenu, self).__init__()
        titleText1 = titleText.titleText()
        self.add(titleText1)
