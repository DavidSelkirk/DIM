class MapEntity:
	def __init__(self):
		self.xPos = 0 #x position on map
		self.yPos = 0 #y position on map
		self.mapImage = "undefined" #image on map

class Tile(MapEntity):
	def __init__(self):
                MapEntity.__init__(self)
		self.passable = "false" #can players walk through this

class Player(Tile):
        def __init__(self, i):
                Tile.__init__(self)
                self.playerNumber = i;
                self.mapImage = "P"+str(i)

