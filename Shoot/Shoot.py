#Credits: Hamster Republic for sounds.
#V 1.4 Added ALL Power-up (gives everything plus 30 points)

#Input libaries and intilize pygame
import pygame, sys, random, math
from pygame.locals import *
pygame.init()

#Declare global vars
ENEMY_PUSH_BACK = 40
BULLET_COUNT = 25
ENEMY_COUNT=0
WIDTH = 950
HEIGHT = 600
enemy_speed = 1
score = 0 # score = kills*3 + time
kills = -2
ENEMY_ARRAY=[]# 3[starting] elements
BULLET_ARRAY=[]# 25 elements
timer = 0
AllSprites = pygame.sprite.OrderedUpdates() # empty assignment for class use.
FPS = 30
lose = False
STOP= False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.MasterImage = pygame.image.load("Player.gif")
        self.MasterImage = self.MasterImage.convert()
        self.rect = self.MasterImage.get_rect()
        transparent = self.MasterImage.get_at((80,1))
        self.MasterImage.set_colorkey(transparent)
        self.Angle = 0 #Since the image and movement angles are the same
        self.RotSpeed = 8
        self.speed = 0
        self.acceleration = 0.5
        self.friction = 0.95;
        self.count = 0 #Bullet counter
        self.delay = 1000 #Delay counter
        self.fireRate = 800 # 1000= 1 second, smaller the faster it is.
        self.damage = 1.0
        #It's very important NOT to use rect.centerx and rect.centery as points since they are ints they will not work well with cos and sin since a float will return most the time. In which will only give 1 or -1 when angles are exactly North,East,South, or West.
        #This is why X and Y posititon must be floats and not ints.
        self.x = 320.0
        self.y = 240.0
        self.rect.centerx, self.rect.centery = (self.x, self.y)
    def update(self):
        self.Keys()
        self.Rotate()
        self.Move()
        self.Bounds()
        self.rect.center = (self.x, self.y)
    def Keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.Angle += self.RotSpeed
        if keys[pygame.K_RIGHT]:
            self.Angle -= self.RotSpeed
        if keys[pygame.K_UP]:
            self.speed += self.acceleration
        if keys[pygame.K_SPACE]:
            self.Shoot()
    def Rotate(self):
        lastCenter = self.rect.center
        self.image = pygame.transform.rotate(self.MasterImage, self.Angle)
        self.rect = self.image.get_rect()
        self.rect.center = lastCenter
    def Move(self):
        self.delay += 30
        self.speed *= self.friction
        if self.speed < 0.1: #Bounds
            self.speed = 0
        self.x += self.speed*math.cos((self.Angle)*(math.pi/180))
        self.y += self.speed*math.sin((self.Angle)*(math.pi/180))*(-1)
    def Bounds(self):
        global lose
        if STOP==False:
            if self.x>WIDTH:
                self.x = 1
            if self.x<0:
                self.x = WIDTH-1
            if self.y>HEIGHT:
                self.y = 1
            if self.y<0:
                self.y = HEIGHT-1
    def Shoot(self):
        global STOP
        if(self.delay>self.fireRate) and STOP==False:
            if(self.count<24):
                self.count+=1
                BULLET_ARRAY[self.count].x = self.x+38*math.cos((self.Angle)*(math.pi/180))
                BULLET_ARRAY[self.count].y = self.y+38*math.sin((self.Angle)*(math.pi/180))*(-1)
                BULLET_ARRAY[self.count].Angle = self.Angle
                BULLET_ARRAY[self.count].speed = 15
            else:
                self.count = 0
            self.delay = 0

window = pygame.display.set_mode((WIDTH, HEIGHT)) #Create window here so display is availble.
player = Player() #Create player here so bullet class can use.

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x=-100,y=-100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bullet.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        transparent = self.image.get_at((1,1))
        self.image.set_colorkey(transparent)
        self.x = x
        self.y = y
        self.speed = 0
        self.Angle = player.Angle
        self.rect.centerx, self.rect.centery = (self.x, self.y)
    def update(self):
        self.x += self.speed*math.cos((self.Angle)*(math.pi/180))
        self.y += self.speed*math.sin((self.Angle)*(math.pi/180))*(-1)
        self.rect.center = (self.x, self.y)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x=0,y=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        transparent = self.image.get_at((1,1))
        self.image.set_colorkey(transparent)
        self.x = x
        self.y = y
        self.speed = enemy_speed
        self.Angle = 0
        self.Speed=1
        self.isHit = False
        self.health = 6
        self.pushBack = 30
        self.rect.centerx, self.rect.centery = (self.x, self.y)
        self.Reset()
    def update(self):
        #More Stuff Here
        self.Move()
        self.Hit()
        self.rect.center = (self.x, self.y)
    def Reset(self):
        global kills
        kills+=1
        self.image = pygame.image.load("enemy.gif")
        self.health=6.0
        self.isHit=False
        radEdge = random.random()
        if radEdge <= 0.25:
            self.x = random.random()*WIDTH
            self.y = 0
        elif radEdge <= 0.5:
            self.x = 0
            self.y = random.random()*HEIGHT
        elif radEdge <= 0.75:
            self.x = random.random()*WIDTH
            self.y = HEIGHT
        else:
            self.x = WIDTH
            self.y = random.random()*HEIGHT
    def Move(self):
        global timer
        global ENEMY_COUNT
        #Adjust speed based on time
        if int(timer/1000)>=20:
            self.Speed=2
        if int(timer/1000)>=40:
            self.Speed=3
        if int(timer/1000)>=60:
            self.Speed=4
        if int(timer/1000)>=80:
            self.Speed=5
        if int(timer/1000)>=100:
            self.Speed=6
        if int(timer/1000)>=150:
            self.Speed=7
        if int(timer/1000)>=200:
            self.Speed=8
        if int(timer/1000)>=250:
            self.Speed=9
        if int(timer/1000)>=300:
            self.Speed=10
        if int(timer/1000)>=400:
            self.Speed=12
        if int(timer/1000)>=500:
            self.Speed=15
        if int(timer/1000)>=600:
            self.Speed=20
        if int(timer/1000)>=750:
            self.Speed=30

        #Move towards player
        self.dx = math.fabs(player.x - self.x)
        self.dy = math.fabs(player.y - self.y)
        angle = math.atan2(self.dy, self.dx)
        self.dx = self.Speed*math.cos(angle)
        self.dy = self.Speed*math.sin(angle)
        if self.x > player.x:
            self.dx = self.dx*(-1)
        if self.y > player.y:
            self.dy = self.dy*(-1)
        self.x += self.dx
        self.y += self.dy
    def Hit(self):
        global AllSprites, ENEMY_ARRAY, enemy_speed
        distancePlayer = math.sqrt(math.pow((self.x-player.x),2)+math.pow((self.y-player.y),2))
        if distancePlayer < 50:
            print "Game Over" #This works
            menu = Menu()
            AllSprites.add(menu)
            player.speed=0
            player.acceleration=0
            enemy_speed = 0
            for enemy in ENEMY_ARRAY:
                enemy.Speed=0
            #Have a function to restart the game and one to make a small menu interface.
        for bullet in BULLET_ARRAY:
            distanceBullet = math.sqrt(math.pow((self.x-bullet.x),2)+math.pow((self.y-bullet.y),2))
            if distanceBullet < 50:
                self.image = pygame.image.load("enemyHit.gif")
                if self.health > 5: #Only on first hit will the enemy slow down
                    self.Speed *= 0.75
                self.health -= player.damage
                #Hide and move bullet
                bullet.speed=0
                bullet.x = -100
                bullet.y = -100
                #Push back enemy or kill(reset)
                DX = math.fabs(player.x - self.x)
                DY = math.fabs(player.y - self.y)
                if self.x > player.x:
                    DX = DX*(-1)
                if self.y > player.y:
                    DY = DY*(-1)
                angle = math.atan2(DY,DX)+ math.pi
                self.x += math.cos(angle)*self.pushBack
                self.y += math.sin(angle)*self.pushBack
                if self.health < 1:
                    self.Reset()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("DAMAGE.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        transparent = self.image.get_at((1,1))
        self.image.set_colorkey(transparent)
        self.x = -100
        self.y = -100
        self.item = "damage"
        self.Timer = 0
    def update(self):
        global HEIGHT, WIDTH, FPS
        self.Timer += FPS #Make Timer act like a timer.
        if(self.Timer>15000):# 15 seconds
            self.Timer=0
            selector = random.random()
            if selector <= 0.3:
                self.image = pygame.image.load("FIRERATE.gif")
                self.item = "firerate"
                transparent = self.image.get_at((1,1))
                self.image.set_colorkey(transparent)
            elif selector <= 0.6:
                self.image = pygame.image.load("SPEED.gif")
                self.item = "speed"
                transparent = self.image.get_at((1,1))
                self.image.set_colorkey(transparent)
            elif selector <= 0.9:
                self.image = pygame.image.load("DAMAGE.gif")
                self.item = "damage"
                transparent = self.image.get_at((1,1))
                self.image.set_colorkey(transparent)
            else:
                self.image = pygame.image.load("ALL.gif")
                self.item = "all"
                transparent = self.image.get_at((1,1))
                self.image.set_colorkey(transparent)
            self.x = random.random()*WIDTH
            self.y = random.random()*HEIGHT
        distancePlayer = math.sqrt(math.pow((self.x-player.x),2)+math.pow((self.y-player.y),2))
        if distancePlayer < 50:
            self.HitPlayer()
        self.rect.centerx, self.rect.centery = (self.x, self.y)
            #Play sound here
    def HitPlayer(self):
        global kills
        if self.item=="firerate":
            player.fireRate *= 0.75
        elif self.item=="speed":
            player.acceleration += 0.10
        elif self.item=="damage":
            player.damage += 0.25
        else:
            #ALL gives everything as one plus 10 kills
            player.fireRate *= 0.75
            player.acceleration += 0.10
            player.damage += 0.25
            kills+=10
        self.x = -100
        self.y = -100

class Menu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Menu.png")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = (WIDTH/2, HEIGHT/2)
    def update(self):
        global timer, STOP, ENEMY_ARRAY
        STOP=True
        timer-=30 #since time is +30 evey frame, this wil canncel that to make it stop.
        #Place player and all enemies out of site constantly while menu is up.
        player.x=1000
        player.y=-100
        for enemy in ENEMY_ARRAY:
            enemy.x,enemy.y = (1000,1000)
        self.Keys()
    def Keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.Reset()
            self.kill()
    def Reset(self):
        #This will reset the game.
        global lose
        lose=True

#Create Screen and starting conditions
def main():
    global timer, FPS, ENEMY_COUNT, kills, player, lose, STOP
    fpsClock = pygame.time.Clock()

    #window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Shoot')

    #Setup
    fontObj = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = 'Time: '+ str(pygame.time.get_ticks())
    textTimerObj = fontObj.render(text, True, (30,30,30))
    textRectObj = textTimerObj.get_rect()
    textRectObj.center = (70,20)
    textScore = fontObj.render("Score: "+str(kills+(timer/1000)),True,(100,100,100))
    textRectScore = textScore.get_rect()
    textRectScore.center = (70,300)
    background = pygame.Surface(window.get_size())
    background.fill((255,255,255))

    #Object Setup
    #Put 25 bullets in AllSprites
    for i in range(BULLET_COUNT):
        newBullet = Bullet()
        BULLET_ARRAY.append(newBullet)

    #Put Enemy in AllSprites
    menu = Menu()
    enemy = Enemy()
    enemy2 = Enemy()
    powerUp = PowerUp()
    ENEMY_ARRAY.append(enemy)
    ENEMY_ARRAY.append(enemy2)
    AllSprites = pygame.sprite.OrderedUpdates(player,BULLET_ARRAY, powerUp, menu)
    AllSprites.add(enemy, enemy2)

    while True: #main game loop

        #Update Timer and cast into int
        #timer = int(timer/1000)
        text = 'Time: '+ str(timer/1000)


        #Adjust enemies based on time
        if (timer/1000)>50 and ENEMY_COUNT==0:
            nEnemy = Enemy()
            AllSprites.add(nEnemy)
            ENEMY_ARRAY.append(nEnemy)
            ENEMY_COUNT+=1
        if (timer/1000)>150 and ENEMY_COUNT==1:
            nEnemy = Enemy()
            AllSprites.add(nEnemy)
            ENEMY_ARRAY.append(nEnemy)
            ENEMY_COUNT+=1
        if (timer/1000)>200 and ENEMY_COUNT==2:
            nEnemy = Enemy()
            AllSprites.add(nEnemy)
            ENEMY_ARRAY.append(nEnemy)
            ENEMY_COUNT+=1
        if (timer/1000)>300 and ENEMY_COUNT==3:
            nEnemy1 = Enemy()
            nEnemy2 = Enemy()
            AllSprites.add(nEnemy1)
            AllSprites.add(nEnemy2)
            ENEMY_ARRAY.append(nEnemy1)
            ENEMY_ARRAY.append(nEnemy2)
            ENEMY_COUNT+=1
        if (timer/1000)>500 and ENEMY_COUNT==4:
            nEnemy1 = Enemy()
            nEnemy2 = Enemy()
            AllSprites.add(nEnemy1)
            AllSprites.add(nEnemy2)
            ENEMY_ARRAY.append(nEnemy1)
            ENEMY_ARRAY.append(nEnemy2)
            ENEMY_COUNT+=1

        #Reset
        if(lose==True):
            for items in AllSprites:
                items.kill()
            for i in range(BULLET_COUNT):
                newBullet = Bullet()
                BULLET_ARRAY.append(newBullet)
            player = Player()
            enemy = Enemy()
            enemy2 = Enemy()
            powerUp = PowerUp()
            AllSprites.add(player,enemy,enemy2, powerUp, BULLET_ARRAY)
            ENEMY_ARRAY.append(enemy)
            ENEMY_ARRAY.append(enemy2)
            ENEMY_COUNT=0
            kills=0
            timer=0
            STOP=False
            lose=False
        #Check if enemy hit player
        for enemy in ENEMY_ARRAY:
            distancePlayer = math.sqrt(math.pow((enemy.x-player.x),2)+math.pow((enemy.y-player.y),2))
            if distancePlayer < 50:
                print "Game Over" #This works
                menu = Menu()
                AllSprites.add(menu)
                player.speed=0
                player.acceleration=0
                player.x=0
                player.y=0
                enemy_speed = 0
                for enemy in ENEMY_ARRAY:
                    enemy.Speed=0
                    enemy.x, enemy.y = (500,500)

        #Draw Timer
        textTimerObj = fontObj.render(text, True, (30,30,30)) #textsetup
        textScore = fontObj.render("Score: "+str((kills*5)+(timer/1000)),True,(100,100,100))
        AllSprites.clear(window, background)
        AllSprites.update()
        window.blit(background, (0, 0))
        window.blit(textTimerObj, (20, 20))
        window.blit(textScore, (20,560))
        AllSprites.draw(window)

        pygame.display.flip()#Double Buffering

        #Event Handler
        for event in pygame.event.get():
            if event.type == QUIT:
              pygame.quit()
              sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)
        timer += FPS

if __name__ == '__main__':
    main()

