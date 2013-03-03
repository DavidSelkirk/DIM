import MapEntity

#tiles = []
#backgroundTiles = [];
#rowSize = 0
#columnSize = 0

class TileMap:
        def __init__(self, filename):
                self.tiles = []
                backgroundTiles = []
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
                        self.tiles.append(x)
                self.backgroundTiles = self.copy(self.tiles)
                for i in range(0, self.rowSize):
                        print self.backgroundTiles[i]
                self.printMap()

        def copy(self, source):
                temp = []
                for i in range(0, self.rowSize):
                        x = []
                        x = source[i][:]
                        temp.append(x)
                return temp

                        
        def populateMap(self, p):
                #for p in players:
                #set player position
                self.tiles = self.copy(self.backgroundTiles)
                self.tiles[p.xPos][p.yPos] = p.mapImage
                #self.printMap()

        #print the game map
        def printMap(self):
                print
                for i in range(0, self.rowSize):
                        print(self.tiles[i])
                print

        def movePlayer(self, p, moves, direction):
                if not direction in moves:
                        print "Not a legal move"
                        return
                if(direction == "up" and self.tiles[p.xPos-1][p.yPos] != "W"):
                        p.xPos -= 1
                if(direction == "down" and self.tiles[p.xPos+1][p.yPos] != "W"):
                        p.xPos += 1
                        print "Here"
                self.populateMap(p)
                self.printMap()

        def getPlayerMoves(self, p):
                moveList = []
                #up
                if(p.xPos - 1 >= 0  and self.tiles[p.xPos-1][p.yPos] != "W"):
                        moveList.append("up")
                #down
                if(p.xPos + 1 < self.rowSize and self.tiles[p.xPos+1][p.yPos] != "W"):
                        moveList.append("down")
                return moveList
