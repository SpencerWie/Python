"""
V 1.0.1
BlockRun.py
A basic platform scrolling game.
-By Spencer Wieczorek
"""
#-------------------------------------------------------------------------------

### Coding Setup #### - (1000 lines)

# Variables

# pygame Setup

# All Objects

# All Functions

# Game Setup (BlockRun)

# Main Game Loop

# Event Handler

#-------------------------------------------------------------------------------
#[]Variables
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 300

LEFT=False
RIGHT=False
UP=False
DOWN=False

COINS = 0
JUMP=False
JUMP_SPEED=0
JUMP_MAX = 50
xSPEED = 4
ySPEED = 0
walkSPEED = 4
sprintSPEED = 6
SPRINT=False
COLLIDE_L = False
COLLIDE_R = False
onGROUND = False
GRAVITY = 1
DIED=False
WIN=False

LIVES = 3
LEVEL = 0

WHITE = (255,255,255)
BLACK = (30,30,30)
GREY = (40,40,40)
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#[]Setup pygame
import pygame, sys, random
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

pygame.display.set_icon(pygame.image.load('icon.bmp'))
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Block Run')

mousex=0
mousey = 0
fontObj = pygame.font.Font('freesansbold.ttf', 15)
textPos = 'Coins:'+str(COINS)
textSurfaceObj = fontObj.render(textPos, True, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (40,20)
textPos2 = 'Hearts:'+str(LIVES)
textSurfaceObj2 = fontObj.render(textPos, True, WHITE)
textRectObj2 = textSurfaceObj.get_rect()
textRectObj2.center = (42,40)
textPos3 = 'Level:'+str(LEVEL)
textSurfaceObj3 = fontObj.render(textPos, True, WHITE)
textRectObj3 = textSurfaceObj.get_rect()
textRectObj3.center = (420,15)
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#[]All Objects
class Player(pygame.sprite.Sprite):
    global DOWN
    global LEFT
    global RIGHT
    global SPRINT
    global LEVEL
    def __init__(self, turn=False, down=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH/2
        self.rect.centery = WINDOW_HEIGHT/4
        self.turn = turn
        self.down = down

    def update(self):
        if LEFT==True and DIED==False and WIN==False: #normal
            self.image = pygame.image.load("playerTurn.gif")
            self.image = self.image.convert()
            newRect = self.image.get_rect()
            newRect.centerx = self.rect.centerx
            newRect.centery = self.rect.centery
            self.rect = newRect
            self.turn = True
            self.down=False
        elif RIGHT==True and DIED==False and WIN==False:
            self.image = pygame.image.load("player.gif")
            self.image = self.image.convert()
            newRect = self.image.get_rect()
            newRect.centerx = self.rect.centerx
            newRect.centery = self.rect.centery
            self.rect = newRect
            self.turn = False
            self.down=False

        if self.turn==True and DIED==False and WIN==False and SPRINT==False: #duck
            if DOWN==True:
                self.image = pygame.image.load("playerDownTurn.gif")
                self.image = self.image.convert()
                newRect = self.image.get_rect()
                newRect.centerx = self.rect.centerx
                newRect.centery = self.rect.centery+2
                self.rect = newRect
                self.down=True
                self.turn = True

        if DOWN==True and self.turn==False and DIED==False and WIN==False and SPRINT==False:
            self.image = pygame.image.load("playerDown.gif")
            self.image = self.image.convert()
            newRect = self.image.get_rect()
            newRect.centerx = self.rect.centerx
            newRect.centery = self.rect.centery+2
            self.rect = newRect
            self.down=True
            self.turn = False

        if DOWN==False and self.down==True: #Unduck when let go of down and you are ducking
            if self.turn==True:
                self.image = pygame.image.load("playerTurn.gif")
                self.image = self.image.convert()
                newRect = self.image.get_rect()
                newRect.centerx = self.rect.centerx
                newRect.centery = self.rect.centery
                self.rect = newRect
                self.turn = False
                self.down=False
            elif self.turn==False:
                self.image = pygame.image.load("player.gif")
                self.image = self.image.convert()
                newRect = self.image.get_rect()
                newRect.centerx = self.rect.centerx
                newRect.centery = self.rect.centery
                self.rect = newRect
                self.turn = False
                self.down=False

    def Die(self):
        global LIVES
        LEFT=False
        RIGHT=False
        DIED=True
        LIVES -= 1
        self.image = pygame.image.load("playerDie.gif")
        self.rect.centery +=0
        self.rect.centerx +=0
    def Win(self):
        self.image = pygame.image.load("playerWin.gif")
        self.rect.centery +=0
        self.rect.centerx +=0
        self.rect.centery = goalArray.sprite.rect.centery
        self.rect.centerx = goalArray.sprite.rect.centerx
    def reset(self):
        self.rect.centerx = WINDOW_WIDTH/2
        self.rect.centery = WINDOW_HEIGHT/4
        self.image = pygame.image.load("player.gif")
        if LEVEL==2:
            for items in stage:
                items.kill()
            CreateLevel2()
            for hearts in heartArray:
                hearts.kill()
        elif LEVEL==3:
            for items in stage:
                items.kill()
            CreateLevel3()
            for hearts in heartArray:
                hearts.kill()
        elif LEVEL==4:
            for items in stage:
                items.kill()
            CreateTitle()
            LIVES=99

class Sprint(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("EffectRight.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centery = playerArray.sprite.rect.centery
    def update(self):
        if SPRINT==True and DOWN==False and DIED==False and WIN==False:
            if RIGHT==True:
                self.rect.centerx = playerArray.sprite.rect.centerx-17
                self.rect.centery = playerArray.sprite.rect.centery-15
                self.image = pygame.image.load("EffectRight.gif")
            elif LEFT==True:
                self.rect.centerx = playerArray.sprite.rect.centerx+14
                self.rect.centery = playerArray.sprite.rect.centery-15
                self.image = pygame.image.load("EffectLeft.gif")
            else:
                self.rect.centerx = -50
                self.rect.centery = -50

class Enemy(pygame.sprite.Sprite):
    def __init__(self, X=0, Y=0, SPEED = 2, Area=50, Hits=0, direct='right', xS=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.gif")

        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
        self.X = X #New restart var must be made because X&Y change
        self.xS = self.rect.centerx #restart var
        self.Y = Y
        self.direct = direct
        self.Area = Area
        self.SPEED = SPEED
        self.Hits = Hits
    def reset(self):
        self.rect.centerx = self.xS
        self.X = self.xS
        self.rect.centery = self.Y
        self.Hits=0
    def move(self):
        if self.direct=='right':
            if self.rect.centerx < self.X+self.Area:
                self.rect.centerx += self.SPEED
                if self.Hits==1:
                    self.image = pygame.image.load("enemyHit.gif")
                    self.image = self.image.convert()
                else:
                    self.image = pygame.image.load("enemy.gif")
                    self.image = self.image.convert()
            elif self.rect.centerx >= self.X+self.Area:
                self.direct='left'
        if self.direct=='left':
            if self.rect.centerx > self.X-self.Area:
                self.rect.centerx -= self.SPEED
                if self.Hits==1:
                    self.image = pygame.image.load("enemyHitTurn.gif")
                    self.image = self.image.convert()
                else:
                    self.image = pygame.image.load("enemyTurn.gif")
                    self.image = self.image.convert()
            elif self.rect.centerx <= self.X-self.Area:
                self.direct='right'
    def Kill(self):
        self.Hits+=1
        if self.Hits==1:
            self.rect.centery+=19
        else:
            r = random.randint(1, 100) # There is a 60% of dropping a coin.
            if r>40:
                coinEx = Coin(self.rect.centerx,self.rect.centerx-10)
                AllSprites2.add(coinEx)
                stage.add(coinEx)
                coinArray.add(coinEx)
            elif r<6: # There is a 5% of dropping a heart
                heartEx = Heart(self.rect.centerx,self.rect.centerx-10)
                AllSprites2.add(heartEx)
                stage.add(heartEx)
                heartArray.add(heartEx)
            self.kill()

class SpikeEnemy(Enemy):
    def __init__(self, X=0, Y=0, SPEED = 2, Area=40, xS=0,direct='right',angle=30):
        Enemy.__init__(self)
        self.image = pygame.image.load("EnemyRoller.gif")
        #self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
        self.X = X #New restart var must be made because X&Y change
        self.xS = self.rect.centerx #restart var
        self.Y = Y
        self.Area = Area
        self.SPEED = SPEED
        self.angle = angle
    def move(self):
        if self.direct=='right':
            if self.rect.centerx < self.X+self.Area:
                self.rect.centerx += self.SPEED
            elif self.rect.centerx >= self.X+self.Area:
                self.direct='left'
        if self.direct=='left':
            if self.rect.centerx > self.X-self.Area:
                self.rect.centerx -= self.SPEED
            elif self.rect.centerx <= self.X-self.Area:
                self.direct='right'
    def Kill(self):
        self.SPEED+=0
        deathCode()


class EnemyUfo(Enemy):
    def __init__(self, X=0, Y=0, SPEED = 3, Area=40, Hits=0, direct='up', xS=0):
        Enemy.__init__(self)
        self.image = pygame.image.load("ufo.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
        self.X = X #New restart var must be made because X&Y change
        self.xS = self.rect.centerx #restart var
        self.Y = Y
        self.direct = direct
        self.Area = Area
        self.SPEED = SPEED
    def move(self):
        if self.direct=='up':
            if self.rect.centery < self.Y+self.Area:
                self.rect.centery += self.SPEED
                if self.Hits==1:
                    self.image = pygame.image.load("ufo-hit.gif")
                else:
                    self.image = pygame.image.load("ufo.gif")
            elif self.rect.centery >= self.Y+self.Area:
                self.direct='down'
        if self.direct=='down':
            if self.rect.centery > self.Y-self.Area:
                self.rect.centery -= self.SPEED
                if self.Hits==1:
                    self.image = pygame.image.load("ufo-hit.gif")
                else:
                    self.image = pygame.image.load("ufo.gif")
            elif self.rect.centery <= self.Y-self.Area:
                self.direct='up'
    def Kill(self):
        self.Hits+=1
        if self.Hits==1:
            self.rect.centery+=19
        else:
            self.kill()

class Block(pygame.sprite.Sprite):
    def __init__(self, X=0, Y=0, WIDTH=20, HEIGHT=20, COLOR=(5,5,5)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH,HEIGHT))
        self.image.fill(COLOR)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, COLOR, self.rect, 0)
        self.rect.centerx = X
        self.rect.centery = Y
        self.X = X
        self.Y = Y
    def reset(self):
        self.rect.centerx = self.X
        self.rect.centery = self.Y

#Clouds is a in-place background animation sprite (for now an single in-ant obj)
class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("clouds.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()

class Spike(pygame.sprite.Sprite):
    def __init__(self, X=0, Y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spikes.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
        self.X = X #New restart var must be made because X&Y change
        self.Y = Y #
    def reset(self):
        self.rect.centerx = self.X
        self.rect.centery = self.Y

class Coin(pygame.sprite.Sprite):
    def __init__(self, X=0, Y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
        self.X = X
        self.Y = Y
    def reset(self):
        self.rect.centerx = self.X
        self.rect.centery = self.Y
    def Kill(self):
        self.kill()

class Heart(Coin):
    def __init__(self, X=0, Y=0):
        Coin.__init__(self)
        self.image = pygame.image.load("heart.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
        self.X = X
        self.Y = Y


class Goal(pygame.sprite.Sprite):
    def __init__(self, X=0, Y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("goal.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y
        self.X = X
        self.Y = Y
    def reset(self):
        self.rect.centerx = self.X
        self.rect.centery = self.Y

class Title(pygame.sprite.Sprite):
    def __init__(self, X=0, Y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Title.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = X
        self.rect.centery = Y

class Instructions(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("HowToPlay.jpg")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#[]All functions
def loadLevel():
    global LEVEL
    #reset starting vars
    LEFT=False
    RIGHT=False
    UP=False
    JUMP=False
    JUMP_SPEED = 0
    COLLIDE_L = False
    COLLIDE_R = False
    onGROUND = False
    GRAVITY = 1
    DIED=False
    WIN=False
    LEVEL+=1
    #First remove all the items in the stage
    playerArray.sprite.reset()
    for items in stage:
        items.kill()
    if LEVEL==2:
        CreateLevel2()
    elif LEVEL==3:
        CreateLevel3()
    elif LEVEL==1:
        for items in titleArray:
            items.kill()
        CreateLevel1()

def CreateTitle():
    global LEVEL
    LEVEL=0
    for items in stage:
        items.kill()
    global COINS
    global LIVES
    COINS=0
    LIVES=3
    playerArray.sprite.centerx = 0
    block1 = Block(0,300,10000,20)
    goal = Goal(-300,-300)
    goalArray.add(goal)
    title = Title(WINDOW_WIDTH/2 , WINDOW_HEIGHT/2)
    AllSprites2.add(title,block1)
    blockArray.add(block1)
    titleArray.add(title,block1)

def CreateLevel1():
    player = Player()
    goal = Goal(1340,220)
    #Blocks       (x,y,w,h)
    block1 = Block(0,300,150,150)
    block2 = Block(200,300,400,30)
    block3 = Block(400,280,100,40)
    block4 = Block(660,270,300,60)
    block5 = Block(960,270,100,60)
    block6 = Block(1260,280,200,60)
    block7 = Block(200,180,100,30)
    #Enemys        (x, y, spd,dis)
    enemy1 = Enemy(670,215,2,70)
    enemy2u = EnemyUfo(1080,200,3,150)
    #Coins        (x,y)
    coin1 = Coin(5,170)
    coin2 = Coin(405,240)
    coin3 = Coin(605,150)
    coin4 = Coin(755,150)
    coin5 = Coin(1080,160)
    #Hearts
    heart1 = Heart(1080,30)
    #Spikes       (x,y)
    spike1 = Spike(310,280)
    # Game Arrays (level 1 items)
    AllSprites2.add(block1, block2, block3,block4,block5,block6,block7,spike1,coin1,coin2,coin3,coin4,coin5,heart1,enemy1,enemy2u,goal)
    stage.add(block1,block2,block3,block4,block5,block6,block7,spike1,coin1,coin2,coin3,coin4,coin5,heart1,enemy1,enemy2u,goal)
    blockArray.add(block1,block2,block3,block4,block5,block6,block7)
    spikeArray.add(spike1)
    coinArray.add(coin1,coin2,coin3,coin4,coin5)
    heartArray.add(heart1)
    enemyArray.add(enemy1,enemy2u)
    goalArray.add(goal)

def CreateLevel2():
    enemy1 = Enemy(395,220,2,80)
    enemy2u = EnemyUfo(900,200,4,150)
    enemy3s = SpikeEnemy(1900,80,2,250)
    enemy4 = Enemy(2970,240,3,120)
    enemy5 = Enemy(3450,240,2,120)
    block1 = Block(300,265,400,40)
    block2 = Block(225,200,30,100)
    block3 = Block(225,240,140,70)
    block4 = Block(700,280,30,170)
    block5 = Block(700,210,140,30)
    block6 = Block(1100,280,30,170)
    block7 = Block(1100,210,30,130)
    block8 = Block(1200,210,30,200)
    block9 = Block(1300,210,30,270)
    block10 = Block(1400,210,30,200)
    block11 = Block(1820,280,180,210)#mid
    block12 = Block(1660,260,150,200)
    block13 = Block(1900,260,100,200)
    block14 = Block(2080,260,260,200)
    block15 = Block(2400,280,200,150)
    block16 = Block(2440,280,40,200)
    block17 = Block(2480,240,40,200)
    block18 = Block(2520,250,40,300)
    block19 = Block(2560,190,40,300)
    block20 = Block(2610,190,60,300)
    block21 = Block(3140,290,1040,50)
    block22 = Block(3190,50,1000,30)
    block23 = Block(3670,180,50,280)
    block24 = Block(3140,210,40,220)#
    block25= Block(3140,200,460,20)
    block26= Block(3140,110,400,20)
    goal = Goal(3620,235)
    coin1 = Coin(180,170)
    coin2 = Coin(280,170)
    coin3 = Coin(900,100)
    coin4 = Coin(900,40)
    coin5 = Coin(700,140)
    coin6 = Coin(3000,140)
    coin7 = Coin(3570,20)
    coin8 = Coin(3320,140)
    heart1 = Heart(3670,20)
    spike1 = Spike(180,200)
    spike2 = Spike(270,200)
    spike3 = Spike(3550,260)
    spike4 = Spike(3520,260)
    spike5 = Spike(3490,260)
    spike6 = Spike(3460,260)
    spike7 = Spike(3430,260)
    spike8 = Spike(3400,260)
    stage.add(block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20,block21,block22,block23,block24,block25,block26,coin1,coin2,coin3,coin4,coin5,coin6,coin7,coin8,heart1,spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8,enemy1,enemy2u,enemy3s,enemy4,enemy5,goal)
    AllSprites2.add(block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20,block21,block22,block23,block24,block25,block26,enemy1,coin1,coin2,coin3,coin4,coin5,coin6,coin7,coin8,heart1,spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8,enemy2u,enemy3s,enemy4,enemy5,goal)
    coinArray.add(coin1,coin2,coin3,coin4,coin5,coin6,coin7,coin8)
    heartArray.add(heart1)
    blockArray.add(block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20,block21,block22,block23,block24,block25,block26)
    enemyArray.add(enemy1,enemy2u,enemy3s,enemy4,enemy5)
    spikeArray.add(spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8)
    goalArray.add(goal)

def CreateLevel3():
    enemy1 = Enemy(850,235,2,50)
    enemy2 = Enemy(990,215,3,35)
    enemyS = SpikeEnemy(2500,165,4,1000)
    enemy4 = Enemy(1800,235,3,160)
    enemy5 = Enemy(2500,165,2,250)
    enemy6 = Enemy(2500,115,2,180,1)
    enemy7 = Enemy(3180,200,3,100)
    enemy8 = Enemy(4500,160,3,55)
    block1 = Block(2500,280,5000,40)
    block2 = Block(225,280,300,80)
    block3 = Block(500,280,100,80)
    block4 = Block(700,280,150,80)
    block5 = Block(1000,280,150,80)
    block6 = Block(1150,245,200,100)
    block7 = Block(225,280,250,120)
    block8 = Block(225,280,250,160)
    block9 = Block(1400,160,50,250)
    block10 = Block(3600,160,50,250)
    block11 = Block(1350,180,50,250)
    block11 = Block(1300,200,50,250)
    block12 = Block(1250,220,50,250)
    block13 = Block(1200,240,50,250)
    block14 = Block(2500,280,800,80)
    block15 = Block(1800,190,200,30)
    block16 = Block(1800,120,200,30)#
    block16 = Block(2500,200,600,20)
    block17 = Block(2500,130,400,20)
    block18 = Block(2500,70,300,20)
    block19 = Block(2500,20,200,20)
    block20 = Block(2700,20,30,20)
    block21 = Block(2800,20,50,20)
    block22 = Block(3000,260,25,150)#
    block23 = Block(3200,240,400,30)
    block24 = Block(3390,260,25,150)
    block25 = Block(3450,220,20,250)
    block26 = Block(3600,170,20,250)
    block27 = Block(3750,260,150,200)
    block28 = Block(3950,260,150,200)
    block29 = Block(4250,260,150,200)
    block30 = Block(4500,260,150,150)
    block31 = Block(4375,269,25,300)
    block32 = Block(4725,260,150,200)
    goal = Goal(4725,130)
    coin1 = Coin(850,170)
    coin2 = Coin(500,190)
    coin3 = Coin(1800,60)
    coin4 = Coin(2400,165)
    coin5 = Coin(2600,165)
    coin6 = Coin(2500,105)
    coin7 = Coin(4100,245)
    heart1 = Heart(2800,2)
    spike1 = Spike(1350,255)
    spike2 = Spike(400,255)
    spike3 = Spike(430,255)
    spike4 = Spike(500,235)
    spike5 = Spike(570,255)
    spike6 = Spike(600,255)
    spike7 = Spike(1095,190)
    spike8 = Spike(1065,190)
    spike9 = Spike(3420,255)
    spike10 = Spike(3505,255)
    spike11 = Spike(3535,255)
    spike12 = Spike(3655,255)
    spike13 = Spike(3855,255)
    spike14 = Spike(4055,255)
    spike15 = Spike(4155,255)
    spike16 = Spike(4375,115)
    stage.add(block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20,block21,block22,block23,block24,block25,block26,block27,block28,block29,block28,block29,block30,block31,block32,coin1,coin2,coin3,coin4,coin5,coin6,coin7,heart1,enemy1,enemy2,enemy4,enemy5,enemy6,enemy7,enemy8,enemyS,spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8,spike9,spike10,spike11,spike12,spike13,spike14,spike15,spike16,goal)
    AllSprites2.add(block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20,block21,block22,block23,block24,block25,block26,block27,block28,block29,block29,block30,block31,block32,coin1,coin2,coin3,coin4,coin5,coin6,coin7,heart1,spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8,spike9,spike10,spike11,spike12,spike13,spike14,spike15,spike16,enemy1,enemy2,enemy4,enemy5,enemy6,enemy7,enemy8,enemyS,goal)
    coinArray.add(coin1,coin2,coin3,coin4,coin5,coin6,coin7)
    heartArray.add(heart1)
    blockArray.add(block1,block2,block3,block4,block5,block6,block7,block8,block9,block10,block11,block12,block13,block14,block15,block16,block17,block18,block19,block20,block21,block22,block23,block24,block25,block26,block27,block28,block29,block30,block31,block32)
    enemyArray.add(enemy1,enemy2,enemy4,enemy5,enemy6,enemy7,enemy8,enemyS)
    spikeArray.add(spike1,spike2,spike3,spike4,spike5,spike6,spike7,spike8,spike9,spike10,spike11,spike12,spike13,spike14,spike15,spike16)
    goalArray.add(goal)

def inGroundCheck():
    #If the player is below the ground push the player to the top.
    for blocks in blockArray: # If you are below the top of a block
        if blocks.rect.collidepoint(playerArray.sprite.rect.centerx, playerArray.sprite.rect.bottom-2) or blocks.rect.collidepoint(playerArray.sprite.rect.centerx-10, playerArray.sprite.rect.bottom-2) or blocks.rect.collidepoint(playerArray.sprite.rect.centerx+10, playerArray.sprite.rect.bottom-2):
            playerArray.sprite.rect.centery-=2
            JUMP=False
            JUMP_SPEED=0

def Gravity():
    #Makes the gravity.
    global GRAVITY
    global JUMP
    global JUMP_SPEED
    for blocks in blockArray:
        if blocks.rect.collidepoint(playerArray.sprite.rect.centerx, playerArray.sprite.rect.bottom) or blocks.rect.collidepoint(playerArray.sprite.rect.centerx-11, playerArray.sprite.rect.bottom) or blocks.rect.collidepoint(playerArray.sprite.rect.centerx+11, playerArray.sprite.rect.bottom):
            GRAVITY=0 #When player hits the ground
            JUMP=True
            break #Once a collision is found don't test others
        elif blocks.rect.collidepoint(playerArray.sprite.rect.centerx, playerArray.sprite.rect.top) or blocks.rect.collidepoint(playerArray.sprite.rect.centerx-11, playerArray.sprite.rect.top) or blocks.rect.collidepoint(playerArray.sprite.rect.centerx+11, playerArray.sprite.rect.top):
            JUMP_SPEED = 0 #When player hits the ceiling
            JUMP=False
            DOWN=True
            break
        else:
            if GRAVITY<7:
                GRAVITY+=1
            JUMP=False
            #break X Breaking here will cause to only check first block in turple

    playerArray.sprite.rect.centery += GRAVITY

def jumpCheck():
    #See if the player can jump, jump if the player can.
    global JUMP
    global COLLIDE_R
    global COLLIDE_L
    global JUMP_SPEED
    if JUMP==True:
        if UP==True:
            if JUMP_SPEED==0:
                if JUMP_SPEED<JUMP_MAX:
                    JUMP_SPEED+=20
    else:
        if JUMP_SPEED>0:
            JUMP_SPEED-=1
            JUMP=False
            COLLIDE_R = False
            COLLIDE_L = False

    playerArray.sprite.rect.centery -= JUMP_SPEED

def mainDraw():
    #Draw all objects
    AllSprites2.clear(window, background)
    playerArray.sprite.update()
    AllSprites2.draw(window)
    howToArray.draw(window)

def collisionCheck():
    #Set vars if the players hits the block from its left or right.
    global COLLIDE_R
    global COLLIDE_L

    for blocks in blockArray:

        if (blocks.rect.collidepoint(playerArray.sprite.rect.right, playerArray.sprite.rect.centery) and COLLIDE_R==False):
            COLLIDE_R = True
            COLLIDE_L = False
        elif (blocks.rect.collidepoint(playerArray.sprite.rect.left-1, playerArray.sprite.rect.centery) and COLLIDE_L==False):
            COLLIDE_L = True
            COLLIDE_R = False

def playerMovement():
    #Player can move only when not touching a block to their left or right.
    global COLLIDE_R
    global COLLIDE_L
    global xSPEED
    if LEFT==True and COLLIDE_L==False and DIED==False:
        for items in stage:
            COLLIDE_R=False
            items.rect.centerx += xSPEED
        for monsters in enemyArray: #adjust monsters X so they don't move with the screen
            monsters.X += xSPEED
    if RIGHT==True and COLLIDE_R==False and DIED==False:
        for items in stage:
            COLLIDE_L=False
            items.rect.centerx -= xSPEED
        for monsters in enemyArray:
            monsters.X -= xSPEED

def deathCode():
    #Reset the level when player dies
    global DIED
    playerArray.sprite.image = pygame.image.load("playerDie.gif")
    #This will be set into an UpdateAll() Function # Draw everything then update.
    AllSprites2.clear(window, background)
    AllSprites2.draw(window)
    playerArray.sprite.Die()
    pygame.display.update()
    #END UpdateALL
    DIED=True
    pygame.display.update()
    pygame.display.update()
    fpsClock.tick(FPS)
    pygame.time.wait(2000)
    #Reset positions
    for items in stage:
        items.reset()
        DIED=False
    playerArray.sprite.reset()

def deathCheck():
    global JUMP_SPEED
    global WINDOW_HEIGHT
    #Hit by monster
    for monsters in enemyArray:
        if playerArray.sprite.rect.colliderect(monsters.rect):
            if playerArray.sprite.rect.bottom < monsters.rect.centery - (monsters.rect.h/4): # Top of enemys head
                monsters.Kill()
                JUMP_SPEED+=20 #Make player jump
            else:
                deathCode()
    #Hit by spikes
    for spikes in spikeArray:
        if playerArray.sprite.rect.colliderect(spikes.rect):
            deathCode()
    #Falls of edge
    if playerArray.sprite.rect.centery > WINDOW_HEIGHT+100:
        deathCode()

def getCoin():
    global COINS
    global LIVES
    for coins in coinArray:
        if playerArray.sprite.rect.colliderect(coins.rect):
            coins.Kill()#remove coin
            COINS+=1
            if(COINS>=10):
                COINS-= 10
                LIVES+=1

    for hearts in heartArray:
        if playerArray.sprite.rect.colliderect(hearts.rect):
            hearts.Kill()#remove heart
            LIVES+=1

def moveEnemies():
    for monster in enemyArray:
        monster.move()

def LifeCheck():
    #Reset the game when you lose all lives.
    global LIVES
    global LEVEL
    if LIVES<=0:
        LEVEL=0
        CreateTitle()

def sprintControl():
    #Only can sprint when the player is not ducked.
    if SPRINT==True and DOWN==False and DIED==False and WIN==False:
        sprint = Sprint()
        sprint.update()
        window.blit(sprint.image, (sprint.rect.centerx, sprint.rect.centery))

def onWin():
    #Move to the next level when player hits the goal.
    global JUMP
    global LEFT
    global RIGHT
    global COLLIDE_R
    global COLLIDE_L
    global WIN
    global DIED
    global LEVEL
    if playerArray.sprite.rect.colliderect(goalArray.sprite.rect):
        #Create a array of loadlevels then make a levelWin(LEVEL) function. *Note*
        #Stop player movement and show Win sprite. Set properites.
        playerArray.sprite.Win()
        AllSprites2.clear(window, background)
        AllSprites2.draw(window)
        playerArray.draw(window)
        pygame.display.update()
        fpsClock.tick(FPS)
        JUMP=False
        LEFT=False
        RIGHT=False
        COLLIDE_R=True
        COLLIDE_L=True
        WIN=True
        pygame.time.wait(2000)
            #Reset positions
        for items in stage:
            items.reset()
        DIED=False
        WIN=False
        COLLIDE_R=False
        COLLIDE_L=False
        loadLevel()

#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#[]GameSetup
clouds = Clouds()
player = Player()
goal = Goal(-100,-100)

background = pygame.Surface(window.get_size())
window.blit(background, (0, 0))

titleArray = pygame.sprite.OrderedUpdates()
AllSprites2 = pygame.sprite.OrderedUpdates(clouds,player)
stage = pygame.sprite.OrderedUpdates()
blockArray = pygame.sprite.OrderedUpdates()
spikeArray = pygame.sprite.OrderedUpdates()
coinArray = pygame.sprite.Group()
heartArray = pygame.sprite.Group()
enemyArray= pygame.sprite.Group()
goalArray = pygame.sprite.GroupSingle(goal)
playerArray = pygame.sprite.GroupSingle(player)
howToArray = pygame.sprite.GroupSingle()
#---Level 1 Items/Placement---#
#CreateLevel1()
CreateTitle()
#-------------------#

#-------------------------------------------------------------------------------

##############################################################################[]
while True: #main game loop

    #Draw text
    if LEVEL>0: #Only show text in-game.
        textPos = 'Coins:'+str(COINS)#textsetup
        textPos2 = 'Lives:'+str(LIVES)#textsetup
        textPos3 = 'Level:'+str(LEVEL)
    else:
        textPos = ''
        textPos2 = ''
        textPos3 = ''

    textSurfaceObj = fontObj.render(textPos, True, WHITE) #textsetup
    textSurfaceObj2 = fontObj.render(textPos2, True, WHITE) #textsetup
    textSurfaceObj3 = fontObj.render(textPos3, True, GREY) #textsetup

    mainDraw() #Draw all objects

    sprintControl()

    window.blit(textSurfaceObj, textRectObj) #draw Text objects
    window.blit(textSurfaceObj2, textRectObj2) #draw Text objects
    window.blit(textSurfaceObj3, textRectObj3) #draw Text objects

    Gravity()#Gravity Control

    inGroundCheck() #Check if Playeris inside a block. Move player up if he is.

    jumpCheck() #If the Player is on the ground then jump.

    collisionCheck()#Check collisions.

    playerMovement()#Left and Right Player Movements.

    getCoin()#Get a Coin if a player hits one.

    LifeCheck()#Check if you hit a heart

    deathCheck()#Check if player died.

    moveEnemies()#Move Enemys.

    onWin()#On level win move to the next level.


##############################################################################[]

    #Event Handler
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            #On Key Press
            if event.key == K_LEFT or event.key == K_a:
                LEFT=True
            elif event.key == K_RIGHT or event.key == K_d:
                RIGHT=True
            elif event.key == K_UP or event.key == K_w:
                UP=True
            elif event.key == K_DOWN or event.key == K_s:
                DOWN=True
                xSPEED=walkSPEED-2
            elif (event.key ==  K_LSHIFT or  event.key == K_RSHIFT) and (DOWN==False):
                xSPEED=sprintSPEED
                SPRINT=True
            elif event.key == K_ESCAPE: #ESC is an exit
                pygame.quit()
                sys.exit()

        elif event.type == KEYUP:
            #On Key Release
            if event.key == K_LEFT or event.key == K_a:
                LEFT=False
            elif event.key == K_RIGHT or event.key == K_d:
                RIGHT=False
            elif event.key == K_UP or event.key == K_w:
                UP=False
            elif event.key == K_DOWN or event.key == K_s:
                DOWN=False
                xSPEED=walkSPEED
            elif event.key ==  K_LSHIFT or  event.key == K_RSHIFT:
                xSPEED=walkSPEED
                SPRINT=False
            elif event.key == K_n:
                loadLevel()
            elif event.key == K_SPACE:
                if LEVEL==0:
                    loadLevel()
            elif event.key == K_i:
                if LEVEL==0:
                    howTo = Instructions()
                    howToArray.add(howTo)
                    howToArray.draw(window)
                    LEVEL = -1
                    #Open Insructions
                elif LEVEL == -1:
                    howTo.kill()
                    LEVEL = 0
                    #Close Insructions

    pygame.display.update()
    fpsClock.tick(FPS)

if __name__ == '__main__':
    main()