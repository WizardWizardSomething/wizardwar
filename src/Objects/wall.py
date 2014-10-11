import cocos
import os
from pyglet import image


class Wall(cocos.sprite.Sprite):
    def __init__(self,left,right,up,down):
        if(left and not right and not up and not down):
            super( Wall, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/wall_part-1-0.png')))
        if(not left and right and not up and not down):
            super( Wall, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/wall_part-1-2.png')))
        if(not left and not right and up and not down):
            super( Wall, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/wall_part-0-1.png')))
        if(not left and not right and not up and down):
            super( Wall, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/wall_part-2-1.png')))
        if(left and not right and up and not down):
            super( Wall, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/wall_part-0-0.png')))
        if(left and not right and not up and down):
            super( Wall, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/wall_part-2-0.png')))
        if(not left and right and up and not down):
            super( Wall, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/wall_part-0-2.png')))
        if(not left and right and not up and down):
            super( Wall, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/wall_part-2-2.png')))