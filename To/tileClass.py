
class Tile():

    def __init__(self, xCoord, yCoord, row, column):
        #X,Y coordinates for top left of tile.
        self.x = xCoord
        self.y = yCoord
        self.row = row
        self.col = column

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
