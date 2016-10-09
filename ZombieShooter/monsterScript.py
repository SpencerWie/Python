import bge
import GameLogic
import math

def main():

    cont = bge.logic.getCurrentController()
    monster = cont.owner
    
    scene = GameLogic.getCurrentScene()
    player = scene.objects['Player']    

    # Get a normal vector between monster and play and move monster towards that vector
    # This will make the monster move towards the player
    
    # It turns out blender has this built-in
    """
    vecTo = monster.getVectTo(player)[2]
    distVector = math.sqrt((vecTo[0])**2 + (vecTo[1])**2 + (vecTo[2])**2)*10
    normalToPlayer = [ vecTo[0]/distVector, vecTo[1]/distVector, vecTo[2]/distVector ]
    
    monster.applyMovement( normalToPlayer, True)
    monster.alignAxisToVect(normalToPlayer, 2, 1.0)
    """
    
main()
