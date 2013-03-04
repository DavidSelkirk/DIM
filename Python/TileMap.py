import MapEntity
#tiles = []
#backgroundTiles = [];
#rowSize = 0
#columnSize = 0



class TileMap:
        def __init__(self, filename):
                #setup variables
                self.tiles = []
                backgroundTiles = []
                self.legalTiles = []
                self.initLegalTiles()
                f = open(filename)
                #read the size of the map
                self.rowSize, self.columnSize = [int(x) for x in f.readline().split()]
                print self.rowSize, self.columnSize
                #read each tile symbol from file
                for i in range(0, self.rowSize):
                        x = []
                        for j in range(0, self.columnSize):
                                c = f.read(1)
                                #print "Read " + str(c)
                                while c not in self.legalTiles:
                                        c = ""
                                        c = f.read(1)
                                x.append(c)
                        self.tiles.append(x)
                        #print "Next row"
                        #print
                self.backgroundTiles = self.copy(self.tiles)

        def initLegalTiles(self): #base background tiles
                self.legalTiles.append("W")
                self.legalTiles.append("X")
 
                        
        def copy(self, source):
                temp = []
                for i in range(0, self.rowSize):
                        x = []
                        x = source[i][:]
                        temp.append(x)
                return temp
                
        def populateMap(self, p, z):
                #for p in players:
                #set player position
                self.tiles = self.copy(self.backgroundTiles)
                self.tiles[p.xPos][p.yPos] = p.mapImage
                #print z.xPos, z.yPos
                self.tiles[z.xPos][z.yPos] = z.mapImage
                self.printMap()
                #self.printMap()

        #print the game map
        def printMap(self):
                print
                for i in range(0, self.rowSize):
                        print(self.tiles[i])
                print

        def movePlayer(self, p, zombie, moves, direction):
                if not direction in moves:
                        print "Not a legal move"
                        return
                #up
                if(direction == "up" and self.getPassable(p.xPos-1, p.yPos) == 1):
                        p.xPos -= 1
                #down
                if(direction == "down" and self.getPassable(p.xPos+1, p.yPos) == 1):
                        p.xPos += 1
                #left
                if(direction == "left" and self.getPassable(p.xPos,p.yPos-1) == 1):
                        p.yPos -= 1
                #right
                if(direction == "right" and self.getPassable(p.xPos,p.yPos+1) == 1):
                        p.yPos += 1
                self.populateMap(p, zombie)

        def getPassable(self, x, y):
                if(self.tiles[x][y] != "W" and (self.tiles[x][y]).split()[0][0] != "Z"):
                        return 1

        def getPlayerMoves(self, p):
                moveList = []
                #up
                if(p.xPos - 1 >= 0  and self.tiles[p.xPos-1][p.yPos] != "W"):
                        moveList.append("up")
                #down
                if(p.xPos + 1 < self.rowSize and self.tiles[p.xPos+1][p.yPos] != "W"):
                        moveList.append("down")
                #left
                if(p.yPos - 1 >= 0 and self.tiles[p.xPos][p.yPos-1] != "W"):
                        moveList.append("left")
                #right
                #print str(p.yPos + 1) + " " + str(self.columnSize)
                if(p.yPos + 1 < self.columnSize and self.tiles[p.xPos][p.yPos+1] != "W"):
                        moveList.append("right")
                        
                return moveList
