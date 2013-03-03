import TileMap
from MapEntity import *



# This is the main class for the game Terror In The Boyd Orr.
# Written by David Selkirk 26/02/13

# Read and instantiate the tilemap
tilemap = TileMap.TileMap("Map.txt")

# Randomly place items

# Place players in starting positions
player = Player(1)
tilemap.populateMap(player)

# Loop waiting for player input, or for zombie to move
d = raw_input('Please enter a move (up, down, left, right):')
while d != "q":
      tilemap.movePlayer(player, d)
      print "Enter a command (up, down, left, right)"
      print "or q to quit"
      d = raw_input('Please enter a move (up, down, left, right):')

