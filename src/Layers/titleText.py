import cocos
from Objects import label

class titleText(cocos.layer.Layer):
    cursorPosition = 0
    title = None
    startText = None
    exitText = None
    def __init__(self):
        super(titleText, self).__init__()
        self.title = label.labelClass('Room of Runes',False,32)
        self.title.position = cocos.director.director.get_window_size()[0]/2,(cocos.director.director.get_window_size()[1]+100)/2
        self.startText = label.labelClass('Start',self.shouldBeHighlighted(0),24)
        self.startText.position = cocos.director.director.get_window_size()[0]/2,(cocos.director.director.get_window_size()[1]-40)/2
        self.exitText = label.labelClass('Exit',self.shouldBeHighlighted(1),24)
        self.exitText.position = cocos.director.director.get_window_size()[0]/2,(cocos.director.director.get_window_size()[1]-100)/2
        self.add(self.title)
        self.add(self.startText)
        self.add(self.exitText)

    def shouldBeHighlighted(self,position):
        if(position == self.cursorPosition):
            return True
        else:
            return False

    def changeCursor(self,position):
        if(position>1):
            position=0
        if(position<0):
            position=1
        self.cursorPosition = position
        if(position == 0):
            self.startText.changeHighlighted(True)
            self.exitText.changeHighlighted(False)
        else:
            self.startText.changeHighlighted(False)
            self.exitText.changeHighlighted(True)