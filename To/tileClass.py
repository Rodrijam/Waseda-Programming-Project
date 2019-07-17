from shipClass import*

class Tile():

    def __init__(self, xCoord, yCoord, row, column):
        #X,Y coordinates for top left of tile.
        self.x = xCoord
        self.y = yCoord
        self.row = row
        self.col = column
        self.hit = False
        self.ship = None

    def __str__(self):
        return f"X:{self.x} Y:{self.y} Row:{self.row} Column:{self.col}"

    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getHit(self):
        return self.hit
    
    def hit(self):
        self.hit = True
        
    def hasShip(self):
        return not(self.ship is None)
    
    def getShip(self):
        return self.ship
    
