from Objects.wall import Wall
import cocos
from cocos.euclid import Vector2


class roomBorder(cocos.layer.Layer):
    objectList = None

    def __init__(self):
        super(roomBorder,self).__init__()
        self.tileList = []
        for x in xrange(0,cocos.director.director.get_window_size()[0],32):
            for y in range(0,cocos.director.director.get_window_size()[1],32):
                if(x==0 and y==0):
                    item = Wall(True,False,False,True)
                    item.position = (x+16,y+16)
                    self.add(item)
                    self.tileList.append(item)
                elif(x==0 and y==cocos.director.director.get_window_size()[1]-32):
                    item = Wall(True,False,True,False)
                    item.position = (x+16,y+16)
                    self.add(item)
                    self.tileList.append(item)
                elif(x==cocos.director.director.get_window_size()[0]-32 and y==0):
                    item = Wall(False,True,False,True)
                    item.position = (x+16,y+16)
                    self.add(item)
                    self.tileList.append(item)
                elif(x==cocos.director.director.get_window_size()[0]-32 and y==cocos.director.director.get_window_size()[1]-32):
                    item = Wall(False,True,True,False)
                    item.position = (x+16,y+16)
                    self.add(item)
                    self.tileList.append(item)
                #Now we got the corners, place any remaining sides
                elif(x==0):
                    item = Wall(True,False,False,False)
                    item.position = (x+16,y+16)
                    self.add(item)
                    self.tileList.append(item)
                elif(y==0):
                    item = Wall(False,False,False,True)
                    item.position = (x+16,y+16)
                    self.add(item)
                    self.tileList.append(item)
                elif(x==cocos.director.director.get_window_size()[0]-32):
                    item = Wall(False,True,False,False)
                    item.position = (x+16,y+16)
                    self.add(item)
                    self.tileList.append(item)
                elif(y==cocos.director.director.get_window_size()[1]-32):
                    item = Wall(False,False,True,False)
                    item.position = (x+16,y+16)
                    self.add(item)
                    self.tileList.append(item)

    def addTilesToCollision(self,cm):
        for tile in self.tileList:
            cm.add(tile)

    def updateCollisionPos(self):
        for tile in self.tileList:
            tile.cshape.center = Vector2(tile.get_rect().center[0],tile.get_rect().center[1])
            tile.cshape.r = tile.width/2