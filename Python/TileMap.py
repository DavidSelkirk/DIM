tiles = []
#rowSize = 0
#columnSize = 0

class TileMap:
	def __init__(self, filename):
                f = open(filename)
                #read the size of the map
                self.rowSize, self.columnSize = [int(x) for x in f.readline().split()]
                #read each tile symbol from file
                for i in range(0, self.rowSize):
			x = []
			for j in range(0, self.columnSize):
                                c = f.read(1)
                                if c != " " and c != "\n":
                                        x.append(c)
                        tiles.append(x)
                        
		self.printMap()
		print "Class created"
		tiles[2][2] = "This is position (2,2)"

	def function(self, i, j):
		if i < self.rowSize and j < self.columnSize:
			print (tiles[2][2])
		else:
			print "Arguments out of range"

	def printMap(self):
                for i in range(0, self.rowSize):
                        print(tiles[i])
