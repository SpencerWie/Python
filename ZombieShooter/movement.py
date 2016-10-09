# Handle all the keyboard input for movement

import bge

speed = 0.15 # forward speed
sideStep = 0.1 # left/right speed
backStep = 0.08 # backwards speed
sprint = 0.1 # additional speed when sprinting
jump = 4000.0 # Jump power

cont = bge.logic.getCurrentController()
block = cont.owner
groundCollision = cont.sensors["groundCollision"]

keyboard = bge.logic.keyboard
isPressed = bge.logic.KX_INPUT_ACTIVE
onKeyDown = bge.logic.KX_INPUT_JUST_ACTIVATED

# More foward on W key, apply sprint when left shift is also pressed
if keyboard.events[bge.events.WKEY] == isPressed:
    block.applyMovement((0, speed, 0), True)
    if keyboard.events[bge.events.LEFTSHIFTKEY] == isPressed:
        block.applyMovement((0, sprint, 0), True)
        
# Side step to the left on A key        
if keyboard.events[bge.events.AKEY] == isPressed:
    block.applyMovement((-sideStep, 0, 0), True)
        
# Side step to the right on D key         
if keyboard.events[bge.events.DKEY] == isPressed:
    block.applyMovement((sideStep, 0, 0), True)
    
# Step back on S key       
if keyboard.events[bge.events.SKEY] == isPressed:
    block.applyMovement((0, -backStep, 0), True)    
        
# Jump on SPACE, only allow jump when player is on the ground.        
if keyboard.events[bge.events.SPACEKEY] == onKeyDown:
    if groundCollision.positive:
        block.applyForce((0, 0, jump), True)     
    
    