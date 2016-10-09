import bge
from random import randint

def main():

    # When the player clicks the left mouse button cast a ray
    # from the camera to the crosshair and check if that ray
    # hits a Monster, if it does the monster is hit and loses
    # health

    cont = bge.logic.getCurrentController()
    own = cont.owner
    scene = bge.logic.getCurrentScene()
    objList = scene.objects

    mouseSens = cont.sensors['Mouse']

    # If the left mouse button was clicked
    if mouseSens.positive and objList["gunFire"].visible == 0 and objList["gun"]["delay"] > 0.1:
        # Show gun fire
        objList["gunFire"].setVisible(True)
        objList["gun"].applyRotation([-0.1,0,0], True)
        # Get the object hit from crosshair
        hitObj = objList["Camera"].rayCastTo(objList["crossHair"],300, "")
        # If the object hit was a Monster, kill the one that was hit
        if "Monster" in objList:
            if(str(hitObj) == str(objList["Monster"])):
                hitObj.applyMovement( [-1, 0, 0] , True)
                # Kill the monster when health drops below 1
                if(hitObj["health"] < 1):
                    hitObj.endObject()
                    objList["Player"]["score"] += 1
                    objList["gameText"]["Text"] = objList["Player"]["score"]
                # Otherwise damage monster and update heath bar    
                else:
                    hitObj["health"] -= 10
                    healthBar = hitObj.children[0]
                    # c = currentTransformations
                    c = healthBar.localTransform
                    # set the scale base on remaining health
                    dropHP = ((hitObj["health"])/100)
                    # apply matrix transform (change Y-scale only)
                    healthBar.localTransform = [
                        [ c[0][0], c[0][1], c[0][2], c[0][3]],
                        [ c[1][0], dropHP , c[2][1], c[1][3]],
                        [ c[2][0], c[2][1], c[2][2], c[2][3]],
                        [ 0.0,     0.0,     0.0,     1.0    ] 
                    ]
    
    if objList["gunFire"].visible == 1:
        if(objList["gun"]["delay"] > 0.2):
            objList["gunFire"].setVisible(False)       
            objList["gun"]["delay"] = 0.0 
            objList["gun"].applyRotation([0.1,0,0], True)
main()
