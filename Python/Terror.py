import TileMap
from MapEntity import *



# This is the main class for the game Terror In The Boyd Orr.
# Written by David Selkirk 26/02/13

# Read and instantiate the tilemap
tilemap = TileMap.TileMap("Map.txt")

# Randomly place items and zombies

# Place players in starting positions
player = Player(1)
zombie = Zombie(1, 1, 3)
#print "zombie x " + str(zombie.xPos) + " zombie y " + str(zombie.yPos)
tilemap.populateMap(player, zombie)



# Loop waiting for player input, or for zombie to move
actions = tilemap.getPlayerMoves(player)
print "List of avaliable actions: " + str(actions)
d = raw_input("Choose action: ")
while d != "q":
      tilemap.movePlayer(player, zombie, actions, d)
      #print out avaliable game commands
      actions = tilemap.getPlayerMoves(player)
      print "List of avaliable actions: " + str(actions)
      d = raw_input("Choose action: ")

