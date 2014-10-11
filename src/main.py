from __future__ import division, print_function, unicode_literals

# This code is so you can run the samples without installing the package
import sys
import os
from Scene import mainMenu

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

import cocos

if __name__ == "__main__":
    cocos.director.director.init(resizable=True)

    # And now, start the application, starting with main_scene
    #cocos.director.push_handlers(pyglet.window.key.KeyStateHandler())
    menu = mainMenu.mainMenu()
    cocos.director.director.run(menu)

