from Layers.roomBorder import roomBorder
from Layers import combatText
from Scene.gameOver import gameOver
import cocos
from Layers import titleText
from cocos.collision_model import CollisionManagerBruteForce
from cocos.scenes import FlipX3DTransition
import pyglet
from cocos.audio.pygame.music import *
import os
from Objects import ship, enemyships, explosion, pellet
from cocos.audio.pygame.music import *
from cocos.audio.pygame.mixer import *
import random

#test imports
from pyglet.window import key

class CombatScene( cocos.scene.Scene ):
    collisionManager = None
    title = None
    def __init__(self):
        super( CombatScene, self ).__init__()

        # Render da text
        self.title = combatText.CombatText()
        self.add(self.title)

        # Initialize the ship
        self.bookCraft = ship.Ship()

        self.collisionManager = CollisionManagerBruteForce()
        # Initialize the enemies
        self.enemyList = []
        self.enemyTimer = 0
        self.enemycounter = 0
        self.explosionList = []

        self.roomBorder = roomBorder()
        self.collisionManager.add(self.bookCraft)
        self.roomBorder.addTilesToCollision(self.collisionManager)
        self.add(self.roomBorder)
        self.add(self.bookCraft )
        self.mouserel = (0, 0)

        self.schedule_interval(self.mainCombatTimer, 0.05)
        #self.mainCombatTimer(10)

    def on_mouse_motion(self, x, y, dx, dy):
        self.mouserel = (dx, dy)
        self.bookCraft.rotate((x, y))

    def on_mouse_press(self, *args):
        self.bookCraft.shoot(self)

    def on_key_press(self, key, modifiers):
        # Determine what direction the ship is moving
        if key==pyglet.window.key.W:
            self.bookCraft.craftMovingUp = True
        if key==pyglet.window.key.S:
            self.bookCraft.craftMovingDown = True
        if key==pyglet.window.key.A:
            self.bookCraft.craftMovingLeft = True
        if key==pyglet.window.key.D:
            self.bookCraft.craftMovingRight = True

    def on_key_release(self, key, modifiers):
        if key == pyglet.window.key.W:
            self.bookCraft.craftMovingUp = False
        if key == pyglet.window.key.S:
            self.bookCraft.craftMovingDown = False
        if key == pyglet.window.key.A:
            self.bookCraft.craftMovingLeft = False
        if key == pyglet.window.key.D:
            self.bookCraft.craftMovingRight = False

    def on_enter(self):
        super(CombatScene,self).on_enter()
        if(not get_busy()):
            load(os.path.normpath(r'../assets/RoRFight2.mp3'))
            set_volume(1)
            play(loops=-1)
        cocos.director.director.window.push_handlers(self)

    def on_exit(self):
        super(CombatScene,self).on_exit()
        cocos.director.director.window.remove_handlers(self)
        stop()

    # The update loop for the combat scene
    def mainCombatTimer(self, test):
        self.bookCraft.updateCraftVelocity()
        self.bookCraft.updateBulletPosition()
        self.updateEnemies()
        self.bookCraft.updateCollisionPos()
        self.roomBorder.updateCollisionPos()
        self.updateExplosions()
        if(len(self.collisionManager.objs_colliding(self.bookCraft))>0):
            self.bookCraft.reverseDirection()

    def updateEnemies(self):
        self.enemyTimer += 1
        if self.enemyTimer % 100 == 0:
            for x in xrange(random.randint(0, 10)):
                newEnemy = enemyships.Enemy((0, random.randint(0, 768)), random.randint(200, 340), random.randint(50, 1000))
                self.collisionManager.add(newEnemy)
                self.add(newEnemy)
                self.enemyList.append(newEnemy)

        if not self.enemyList: return
        for ship in self.enemyList:
            for item in map(str, self.collisionManager.objs_colliding(ship)):
                if 'Pellet'.upper() in item.upper():
                    ship.health -= 50
                for bullet in self.bookCraft.bulletList:
                    if bullet in self.collisionManager.objs_colliding(ship):
                        self.collisionManager.remove_tricky(bullet)
                        self.remove(bullet)
                        self.bookCraft.bulletList.remove(bullet)
                if 'ship.Ship' in item:
                    self.bookCraft.heath -= 15
                    if self.bookCraft.heath <= 0:
                        cocos.director.director.replace(FlipX3DTransition(gameOver(),duration=1))

            # check if this should be dead
            if ship.health <= 0:
                self.enemycounter += 1
                huh = Sound(os.path.normpath(r'../assets/VEC3 FX Impact 35.wav'))
                huh.play()
                splosion = explosion.Explosion(ship.get_rect().center)
                self.add(splosion)
                self.explosionList.append(splosion)
                self.collisionManager.remove_tricky(ship)
                self.remove(ship)
                self.enemyList.remove(ship)

            ship.fly()
            if ship.time_alive >= 500:
                self.collisionManager.remove_tricky(ship)
                self.remove(ship)
                self.enemyList.remove(ship)
            else:
                ship.updateCollisionPos()
                ship.time_alive += 1

    def updateExplosions(self):
        if not self.explosionList: return
        for splosion in self.explosionList:
            if splosion.time_alive > 5:
                self.remove(splosion)
                self.explosionList.remove(splosion)
                continue
            splosion.time_alive += 1