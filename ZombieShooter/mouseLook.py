# mouselook.py
# adapted from
# http://www.cgmasters.net/free-tutorials/fps-mouselook-script-plus-real-text/
# adapted and commented by Andy Harris
# modified by Spencer Wieczorek
import bge

from bge import render as r
import math

cont = bge.logic.getCurrentController()
camera = cont.owner
mouse = cont.sensors["Mouse"]
player = camera.parent

# set speed for camera movement
# larger # = more sensitive
sensitivity = 0.08

# set camera rotation limits
high_limit = 180
low_limit = 60

#original script used w and h, pand swapped them!

# determine center of window
cy = r.getWindowHeight()//2  
cx = r.getWindowWidth()//2  

# calculate dx and dy based on position
# dx and dy are actually distance from center
dx = (cx - mouse.position[0])*sensitivity
dy = (cy - mouse.position[1])*sensitivity

r.setMousePosition(cx, cy)
rot = camera.localOrientation.to_euler()

# calculate new pitch (rotation around local X)
pitch = abs(math.degrees(rot[0]))

if high_limit > (pitch+dy) > low_limit:
    pitch += dy
elif (pitch+dy) < low_limit:
    pitch = low_limit
elif (pitch+dy) > high_limit:
    pitch = high_limit
    
rot[0] = math.radians(pitch)
camera.localOrientation = rot.to_matrix()

# calculate new yaw (rotation around local Z) - apply yaw to player
playerRot = player.localOrientation.to_euler()
yaw = math.degrees(playerRot[2]) + dx
playerRot[2] = math.radians(yaw)
player.localOrientation = playerRot.to_matrix()

