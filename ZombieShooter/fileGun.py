import bge

def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    scene = bge.logic.getCurrentScene()
    objList = scene.objects

    mouseSens = cont.sensors['Mouse']

    # If the left mouse button was clicked
    if mouseSens.positive:
        # Show gun fire
        objList["gunFire"].setVisible(True)
    else:
        # Hide gun fire
        if(objList["gunFire"].visible == 1):
            objList["gunFire"].setVisible(False)
        
main()
