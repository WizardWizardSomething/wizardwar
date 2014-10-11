import cocos

class labelClass(cocos.text.Label):
    def __init__(self, text,highlighted,size):
        super( labelClass, self).__init__(text,
                                 font_name='Times New Roman',
                                 font_size=size,
                                 anchor_x='center', anchor_y='center')
        self.changeHighlighted(highlighted)

    def changeHighlighted(self,highlighted):
        if(highlighted):
            self.element.color = (255,255,55,255)
        else:
            self.element.color = (255,255,255,255)