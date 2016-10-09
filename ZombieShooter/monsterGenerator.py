import bge
import random

def main():

    # This code is for generating monsters
    # if will wait for 'delay' amount of seconds
    # and then place the 'monsterController' object
    # into a random position and add a Monster to 
    # the game.
    
    cont = bge.logic.getCurrentController()
    own = cont.owner

    sens = cont.sensors['Keyboard']
    actu = cont.actuators['makeMonster']
    
    scene = bge.logic.getCurrentScene()
    objList = scene.objects            
    
    bounds = 90 # The monster is only made within a 40x40 bounds in X and Y.
    playerBounds = 5 # How far a monster is created next to a player
    monsterLimit = 2 # The total amount of monsters in the game at once
    
    # Change spawn rate based on score
    own["spawnRate"] = 5 - (0.1*objList["Player"]["score"])
    if own["spawnRate"] < 3:
        own["spawnRate"] = 5 - (0.05*objList["Player"]["score"])
    if own["spawnRate"] < 1.5:
        own["spawnRate"] = 5 - (0.025*objList["Player"]["score"])        
    if own["spawnRate"] < 0:    
        own["spawnRate"] = 0.1
        
    # Make the object and set health to 100
    if own["spawnTimer"] > own["spawnRate"]:
        own["spawnTimer"] = 0.0
        
        # Only make a monster if we have less than the limit
        monsterCount = 0
        for obj in objList:
            if(str(obj) == "Monster"):
                monsterCount += 1
        # When we have too many we return, no new monster is made
        if(monsterCount > monsterLimit):
            return
        
        # Setup the monster and get player coords
        newMonster = actu.object
        newMonster["health"] = 100
        playerX = objList["Player"].worldPosition[0]
        playerY = objList["Player"].worldPosition[1]

        # Get for possible locations, ensure the monster will not be made too close 
        # to the player
        monsterX_Neg = random.randrange(-bounds,int(playerX-playerBounds-1))
        monsterX_Pos = random.randrange(int(playerX+playerBounds),bounds+1)
        
        monsterY_Neg = random.randrange(-bounds,int(playerY-playerBounds-1))
        monsterY_Pos = random.randrange(int(playerY+playerBounds),bounds+1)  
        
        # Either spawn: (-X,-Y) (X, Y) (X, -Y) (-X, Y)
        if(random.randrange(0,1+1) == 0):
            own.worldPosition[0] = monsterX_Pos
        else:
            own.worldPosition[0] = monsterX_Neg
            
        if(random.randrange(0,1+1) == 0):
            own.worldPosition[1] = monsterY_Pos
        else:
            own.worldPosition[1] = monsterY_Neg
        
        # This will create the monster and place it in the scene
        cont.activate(actu)
    else:
        cont.deactivate(actu)

main()
