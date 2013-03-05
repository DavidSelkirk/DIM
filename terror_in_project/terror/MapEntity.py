class MapEntity:
	def __init__(self):
		self.xPos = 0 #x position on map
		self.yPos = 0 #y position on map
		self.mapImage = "undefined" #image on map

class Tile(MapEntity):
	def __init__(self):
                MapEntity.__init__(self)
		self.passable = "false" #can players walk through this

class Character(Tile):
        def __init__(self):
                Tile.__init__(self)
                self.health = 2
                

class Player(Character):
        def __init__(self, i):
                Character.__init__(self)
                self.health = 5
                self.playerNumber = i;
                self.mapImage = "P"+str(i)

class Zombie(Character):
        def __init__(self, i, x, y):
                Character.__init__(self)
                self.playerNumber = i;
                self.mapImage = "Z"+str(i)
                #print "zombie x " + str(x) + " zombie y " + str(y)
                self.xPos = x
		self.yPos = y
		#print "zombie x " + str(self.xPos) + " zombie y " + str(self.yPos)
                

