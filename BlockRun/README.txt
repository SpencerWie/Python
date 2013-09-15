Block Run V 1.0.0

~ Game made by Spencer Wieczorek.

### Items needed to Play: ###

*Python 2.6.1

*pygame 1.8.2 (or higher)

*All images must be located in the same directory as "blockRun.py"

### How To Play: ###

-Player: The player can move either with the arrow keys or the ASDW keys. The up (W) key makes the player jump. The Down (S) key makes the player duck, while the player is ducking his speed is reduced by half. The SHIFT key makes the player run, while the player is running he cannot duck, running increases your speed. Also if the SHIFT key is double tapped and held while ducking the player will move faster while ducked. The right and left (A and D) keys move the player left or right.

-Goal: There is a goal at the end of each level, the object of the game is to reach this goal. The player will center itself and show its winning image, then the game will move on to the next level.

-Enemys: In order to kill enemys the player needs to jump on their head twice. The red Block Enemy is the only enemy that can drop items. It has a 60% change of dropping a coin and a 5% change of dropping a heart. This enemys moves side-to-side arross the stage. The UFO enemy does not drop any items, but can be used as a jumping device to get across a gap; this enemy also takes 2 hits to kill. The Spike Block enemy cannot be killed, to avoid this enemy often the player must duck.

-Coins: There are a number of coins in the game for the player to collect, if the player gathers 10 of these coins the coins wil reset to 0 and give the player an extra life.

-Hearts: There is only a single heart per level, these hearts are often in hard to get areas or hidden. These hearts can only be found if the player has not yet been killed in that level, if the player is killed even once the heart dissapears. The reason is so the player cannot take advantage of these hearts after each death.

-Levels: There are 3 levels in the game currectly, reaching the goal lets you move on to the next level. Once the player beats all 3 levels the game goes back to the main menu.

-Main Menu: In this menu the player can either press SPACE to start the game or press "i" to look at the general How To Play rules. To go back to the menu press "i" again.

-Deaths: There are 3 ways the player can die. 

	1. Fall off the cliff.
	2. Hit by spikes.
	3. Killed by an enemy.

###Known Bugs:

	Collision: The collision system is not perfect, when the player jumps and holds up in a certain way up a wall, the player may scale up that wall. If the player lands on a block from a very short distance upwards the player will bouce slightly up and down, this was not on purpose but will not be taken out of the game.

	Floating Platform Edges: If a block has a width less than that of the players there is a chance the player will to move either left or right even after the collsion and when the player falls to the floor still be dectecting that collsion. The player will either be unable to move right or left, to fix this simply move in the other direction and movement will return to normal.

	Enemys: Very rarly if the player jumps while moving upwards towards an enemy and hits the top corners of that enemy he may fly very high in the sky after the jump on the enemy, this is due to the addition of the normal jumping and the jump gained from killing a monster. Also after an enemy dies the item it drops position may vary, but should still be able to be picked up.

	Level3 coin spawn: The enemies on the pyamind and the last enemy in the level has a bug in their coin spawn, the coin will spawn far below them. This will be fixed later in the next update.

	UFO Monster Bug: Rarely, mostly on an indirect hit on the UFO enemy and while the UFO monster is moving up. The player will die, this is due to from one frame to the next that the player moved past the "kill point" of that monster; and therefore the system assumes you didn't hit the target on the head. It is recomended to hit the UFO enemy on the hat.

	*If you find any bugs in the game please tell me so I can try to fix them.*


###Graphics:

	All graphics were made by me accept for the UFO monster, which was made by my bother Calvin. I would like to give his thanks for being a beta tester for my game also.


###Single File: 

	The reason that the *.py file is not seperated because both objects and functions work with the global variables of a single file. There are very few functions or classes that do not work with global variables and would not be worth seperating from the main file. Although I'm sure there is a way to do that I didn't think it would be neccesary.

###Game Cheats:

	Level Skipping: If you press the "n" key you will move to the next level. This was orginally for me to quickly move to a level for testing, I kept it in there if you feel like one of the levels are too hard to play or if you happen to get stuck in one of the levels you can skip to the next one with this.

	Faster movement while ducked: If you double tab and hold the SHIFT key the player will start moving at normal walking speed while ducked. 

###Coding Setup:

-----------------------------------------------------------------------------------
Global Variables

Game Setup (pygame)

All Objects

All Functions

Game Setup (BlockRun)

Main Game Loop

Event Handler
-FPS Tick and display Update

-----------------------------------------------------------------------------------

###Data Setup

-Most of the data in the game is the interaction between boolean variables that can be acess in both objects and function in the code, so these variables are global. Other variables are intergers that are mostly either meant for game properties, such as window width and size; to object properties such as how fast the player can move and how fast can the player sprint. The LEVEL variable is meant to show which scene to show, for example if LEVEL = 1 then the scene would be showing the first level, at LEVEL = 0 the scene is the main menu and at LEVEL = -1 the scene is at the how-to-play menu. The last type of variables are turples, there are meant to simplfy which color to color which object.

### Visual Setup

-The player is always centered in the middle of the screen only by it's x-coordinates, which it's y-coordinates can change freely. Instead of moving the player, all objects move except for the player. Reseting means to deystory all objects but the player and replace them on the stage. At the end of the level the objects are destroyed and new objects are created after a 2 second delay on the level win. 