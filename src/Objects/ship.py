from __future__ import division
from cocos.collision_model import CircleShape
from Objects import cauldronModule, cockpitModule, crateModule, propulsionModule, wandModule
import os
import cocos
from pyglet import image
from cocos.actions import *
from cocos.euclid import Vector2
import math
import pellet


class Ship(cocos.sprite.Sprite):
    def __init__(self):
        super( Ship, self ).__init__(image.load(os.path.normpath(r'../assets/Graphics/BookCraft.png')))

        self.drawModules()

        self.position = (250,250)
        self.bulletList = []
        self.centerPoint = self.get_rect().center
        self.midline = (self.centerPoint, self.get_rect().midtop)
        self.cshape = CircleShape(Vector2(self.centerPoint[0],self.centerPoint[1]),self.width/2)

        # Constants for craft movement
        self.CRAFT_MAX_VELOCITY = 1000
        self.CRAFT_ACCELERATION = 100
        self.CRAFT_MAX_TURNRATE = 1

        # Keep track of the current move speed of the ship. These are accessed
        # directly by the scene controlling the ship
        self.craftMovingUp = False
        self.craftMovingDown = False
        self.craftMovingRight = False
        self.craftMovingLeft = False
        self.craft_x_velocity = 0
        self.craft_y_velocity = 0

    def move(self, dx, dy):
        self.point = (self.point_pos(self.getCenter()[0], self.getCenter()[1], -100, self.rotation))
        move = MoveBy((dx, dy))
        self.do(move)
        self.centerPoint = self.get_AABB().center

    # CMB: Does all the velocity math before updating the crafts position
    def updateCraftVelocity(self):
        # Check which directions the ship is moving, then update accordingly
        # Start with up and down movement
        if self.craftMovingUp and not self.craftMovingDown:
            if self.craft_y_velocity < self.CRAFT_MAX_VELOCITY - self.CRAFT_ACCELERATION:
                self.craft_y_velocity = self.craft_y_velocity + self.CRAFT_ACCELERATION
            else:
                self.craft_y_velocity = self.CRAFT_MAX_VELOCITY
        elif self.craftMovingDown and not self.craftMovingUp:
            if self.craft_y_velocity > (self.CRAFT_MAX_VELOCITY * -1) + self.CRAFT_ACCELERATION:
                self.craft_y_velocity = self.craft_y_velocity - self.CRAFT_ACCELERATION
            else:
                self.craft_y_velocity = self.CRAFT_MAX_VELOCITY * -1
        # Degenerate the move speed if craft is not moving
        else:
            if self.craft_y_velocity > self.CRAFT_ACCELERATION:
                self.craft_y_velocity = self.craft_y_velocity - self.CRAFT_ACCELERATION
            elif self.craft_y_velocity < (self.CRAFT_ACCELERATION * -1):
                self.craft_y_velocity = self.craft_y_velocity + self.CRAFT_ACCELERATION
            else:
                self.craft_y_velocity = 0

        # Left and Right Movement
        if self.craftMovingLeft and not self.craftMovingRight:
            if self.craft_x_velocity > (self.CRAFT_MAX_VELOCITY * -1) + self.CRAFT_ACCELERATION:
                self.craft_x_velocity = self.craft_x_velocity - self.CRAFT_ACCELERATION
            else:
                self.craft_x_velocity = self.CRAFT_MAX_VELOCITY * -1
        elif self.craftMovingRight and not self.craftMovingLeft:
            if self.craft_x_velocity < self.CRAFT_MAX_VELOCITY - self.CRAFT_ACCELERATION:
                self.craft_x_velocity = self.craft_x_velocity + self.CRAFT_ACCELERATION
            else:
                self.craft_x_velocity = self.CRAFT_MAX_VELOCITY
        # Degenerate the move speed if the craft is not moving
        else:
            if self.craft_x_velocity > self.CRAFT_ACCELERATION:
                self.craft_x_velocity = self.craft_x_velocity - self.CRAFT_ACCELERATION
            elif self.craft_x_velocity < (self.CRAFT_ACCELERATION * -1):
                self.craft_x_velocity = self.craft_x_velocity + self.CRAFT_ACCELERATION
            else:
                self.craft_x_velocity = 0

        # Physically move the ship
        self.move(self.craft_x_velocity, self.craft_y_velocity)

    def rotate(self, mousePos):
        self.point = (self.point_pos(self.getCenter()[0], self.getCenter()[1], -100, self.rotation))

        angleOfRot = math.atan2(-(mousePos[1] - self.getCenter()[1]), (mousePos[0] - self.getCenter()[0]))
        angleOfRot %= 2 * math.pi
        angleOfRot = math.degrees(angleOfRot)
        self.do(RotateTo(angleOfRot - 90, 0))

    def getCenter(self):
        return self.get_rect().center

    def getMidline(self):
        return (self.getCenter(), self.get_AABB().midtop)

    def calcVector(self, tupleOfPts):
        return(tupleOfPts[0][0]-tupleOfPts[0][1], tupleOfPts[0][1]-tupleOfPts[1][1])

    # Draw the modules on top of the ship based on the ships position and the
    # layout of the modules
    def drawModules(self):
        MODULE_WIDTH = 20
        MODULE_HEIGHT = 20
        CRAFT_SIZE = self.get_rect().size

        # Create an empty Matrix, which will be iterated through for rendering later
        X_LENGTH = 9
        Y_LENGTH = 6
        ModuleGrid = [["EMPTY" for x in range(Y_LENGTH)] for x in range(X_LENGTH)]

        # Hardcoded values for the module render values.
        # 'EMPTY' means there is no module there, and nothing should be rendered
        # 'RESERVED' means another module is overlapping that space (could probably be implemented better)
        # Reserved value exists mainly to keep the player from overlapping modules during module placement
        # in crafting.
        ModuleGrid[0][0] = "RESERVED"
        ModuleGrid[0][1] = "PROPULSION"
        ModuleGrid[1][1] = "POWER"
        ModuleGrid[1][2] = "CRATE"
        #ModuleGrid[2][4] = "WAND"
        ModuleGrid[3][3] = "POWER"
        ModuleGrid[4][1] = "CRATE"
        ModuleGrid[4][2] = "COCKPIT"
        ModuleGrid[4][3] = "CRATE"

        ModuleGrid[5][3] = "POWER"
        ModuleGrid[7][1] = "POWER"
        ModuleGrid[7][2] = "CRATE"
        ModuleGrid[8][0] = "RESERVED"
        ModuleGrid[8][1] = "PROPULSION"

        # Render the module grid
        for x in range(X_LENGTH):
            for y in range(Y_LENGTH):
                # Render crate modules
                if ModuleGrid[x][y] == "CRATE":
                    self.moduleDebug = crateModule.CrateModule()
                    moduleGridStartingPosition = ((CRAFT_SIZE[0] / 2) - (MODULE_WIDTH / 2),
                                                  (CRAFT_SIZE[1] / 2) - (MODULE_WIDTH / 2))
                    self.moduleDebug.position = (moduleGridStartingPosition[0] * -1 + (x * MODULE_WIDTH),
                                                 moduleGridStartingPosition[1] - (y * MODULE_WIDTH))
                    self.add(self.moduleDebug)

                # Render Propulsion Module
                elif ModuleGrid[x][y] == "PROPULSION":
                    self.moduleDebug = propulsionModule.PropulsionModule()
                    moduleGridStartingPosition = ((CRAFT_SIZE[0] / 2) - (MODULE_WIDTH / 2),
                                                  (CRAFT_SIZE[1] / 2) - (MODULE_WIDTH / 2))
                    self.moduleDebug.position = (moduleGridStartingPosition[0] * -1 + (x * MODULE_WIDTH),
                                                 moduleGridStartingPosition[1] - (y * MODULE_WIDTH))
                    self.add(self.moduleDebug)

                # Render Cockpit Module
                elif ModuleGrid[x][y] == "COCKPIT":
                    self.moduleDebug = cockpitModule.CockpitModule()
                    moduleGridStartingPosition = ((CRAFT_SIZE[0] / 2) - (MODULE_WIDTH / 2),
                                                  (CRAFT_SIZE[1] / 2) - (MODULE_WIDTH / 2))
                    self.moduleDebug.position = (moduleGridStartingPosition[0] * -1 + (x * MODULE_WIDTH),
                                                 moduleGridStartingPosition[1] - (y * MODULE_WIDTH))
                    self.add(self.moduleDebug)

                # Render Power Module
                elif ModuleGrid[x][y] == "POWER":
                    self.moduleDebug = cauldronModule.CauldronModule()
                    moduleGridStartingPosition = ((CRAFT_SIZE[0] / 2) - (MODULE_WIDTH / 2),
                                                  (CRAFT_SIZE[1] / 2) - (MODULE_WIDTH / 2))
                    self.moduleDebug.position = (moduleGridStartingPosition[0] * -1 + (x * MODULE_WIDTH),
                                                 moduleGridStartingPosition[1] - (y * MODULE_WIDTH))
                    self.add(self.moduleDebug)

                # Render Wand Module
                elif ModuleGrid[x][y] == "WAND":
                    self.moduleDebug = wandModule.WandModule()
                    moduleGridStartingPosition = ((CRAFT_SIZE[0] / 2) - (MODULE_WIDTH / 2),
                                                  (CRAFT_SIZE[1] / 2) - (MODULE_WIDTH / 2))
                    self.moduleDebug.position = (moduleGridStartingPosition[0] * -1 + (x * MODULE_WIDTH),
                                                 moduleGridStartingPosition[1] - (y * MODULE_WIDTH))
                    self.add(self.moduleDebug)

    def shoot(self, canvas):
        self.canvas = canvas
        bullet = pellet.Pellet(self.point, self.rotation)
        canvas.collisionManager.add(bullet)
        canvas.add(bullet)
        self.bulletList.append(bullet)

    def updateBulletPosition(self):
        for bullet in self.bulletList:
            newPoint = self.point_pos(bullet.position[0], bullet.position[1], -50, bullet.angle)
            dx = newPoint[0] - bullet.position[0]
            dy = newPoint[1] - bullet.position[1]
            bullet.do(MoveBy((dx, dy), 0))

            if bullet.time_alive > 10:
                self.canvas.collisionManager.remove_tricky(bullet)
                self.canvas.remove(bullet)
                self.bulletList.remove(bullet)
            else:
                bullet.time_alive += 1
                bullet.updateCollisionPos()

    def point_pos(self, x0, y0, d, theta):
        theta_rad = math.pi/2 - math.radians(theta)
        return x0 + d*math.cos(theta_rad), y0 + d*math.sin(theta_rad)

    def updateCollisionPos(self):
        self.cshape.center = Vector2(self.centerPoint[0],self.centerPoint[1])
        self.cshape.r = self.width/2

    def reverseDirection(self):
        if(self.craftMovingLeft):
            self.craft_x_velocity = 1
        if(self.craftMovingDown):
            self.craft_y_velocity = 1
        if(self.craftMovingRight):
            self.craft_x_velocity = -1
        if(self.craftMovingUp):
            self.craft_y_velocity = -1