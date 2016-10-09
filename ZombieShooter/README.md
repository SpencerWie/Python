<h2>Zombie Shooter</h2>

To play this game simply open the file "game.blend" with [Blender](https://www.blender.org/), note this game runs within the Blender Game Engine. All files are included within "game.blend", the other files in this GitHub page are duplicates purefully for the purpose of easy broswering without neededing to download the .blend file.

*Note:* If not set by default, put blender in *"Texture Mode"*, otherwise game textures will not showup in the player.

Notice: All textures are from the follwoing site:
    
    http://www.cgtextures.com/
    
In this game the ASDW Keys are used to move the player, the Space key
is used for jumping and the left mouse button is used for firing bullets.

In this game zombie (many who just need a hug) will be attemping to
hug your player. If they do so you lose the game. For getting a high score 
the player must be aware of their surroundings as it is easy for a zombie
to sneek up on the player. Be careful and alert, check your surroundings often.

The game gets harder as time goes on. It starts off as creating a zombie
every 5 seconds (this info can be togged in the debug screen). As your
score gets higher this delay gets smaller. Note that the green boundry 
cannot be passed by the player but zombie may bespawns pass this boundry. 
The player cannot shoot the zombie until they pass the green boundry.

The limit is 100 zomibes on the map, if there are more than 100 zomibes 
no more will be made until the player kills a zomibe. This is to prevent
an infinite amount of zombies to be spawned.