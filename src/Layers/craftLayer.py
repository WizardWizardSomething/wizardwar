from Objects.ship import Ship
import cocos

class bookCraft(cocos.layer.Layer):
    def __init__(self):
        super(bookCraft, self).__init__()

        # Declare the starting render position
        self.position = (250, 250)