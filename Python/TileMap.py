tiles = []
#rowSize = 0
#columnSize = 0

class TileMap:
	def __init__(self, rSize, cSize):
		self.rowSize = rSize
		self.columnSize = cSize
		for i in range(0, self.rowSize):
			x = []
			for j in range(0, self.columnSize):
				x.append(0)
				tiles.append(x)
		for i in range(0, self.rowSize):
			print tiles[i]
		print "Class created"
		tiles[2][2] = "This is position (2,2)"

	def function(self, i, j):
		if i < self.rowSize and j < self.columnSize:
			print tiles[2][2]
		else:
			print "Arguments out of range"