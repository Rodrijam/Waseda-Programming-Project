import random
from shipClass import *

'''
    This class will track information about the game state.
    Ship locations, etc.
'''

class GameBoardTile:

    def __init__(self, xCoord, yCoord, row, column):
        self.debug_mode = False
        self.x = xCoord
        self.y = yCoord
        self.row = row      #row the tile in in
        self.col = column   #column the tile is in
        self.ship = False   #boolean for if there is a ship piece
        self.hit = False    #boolean for if this space has already been hit
        self.shipReference = None

    def __str__(self):
        return f"X:{self.x} Y:{self.y} Column:{self.col} Row:{self.row} "

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def setShipReference(self, ship):
        if self.shipReference == None:
            self.shipReference = ship

    def getImg(self,h,sType):
        shipImg = pygame.image.load(f'sprites/ship{sType}.jpg')
        #shipImg = pygame.image.load(f'sprites/ship.jpg')
        shipImg = pygame.transform.scale(shipImg, (round((4*h*1.3)/50), round((4*h)/50)))
        return shipImg

    def placeShipPiece(self, ship, display, tile):
        if not self.ship:
            self.ship = True
            if self.debug_mode:
                tile = tile[0]+1, tile[1]+1
                print(f"Placing {ship} on tile {tile}")
                w, h = pygame.display.get_surface().get_size()
                cell = (round(w/10)+((tile[0]-1)*(round((4*h*1.3)/50))), round(h/10)+((tile[1]-1)*(round((4*h)/50))))
                display.blit(self.getImg(h,ship.getSize()), cell)
            return True
        return False
        
    '''
        draws a hit mark on the game screen?
    '''
    def hit(self):
        if not self.hit:
            self.hit = True
            return True
        return False

class GameBoard:

    def __init__(self, mainboard, maindisplay, height=10, width=10):
        # initially 10 x 10 grid, based on grid drawn in 'battleprotoNew.py'
        self.height = height
        self.width = width
        #self.board = [[GameBoardTile() for h in range(height)] for w in range(width)]
        self.board = mainboard
        self.display = maindisplay

        # creates inverted list of all free spaces. Useful for the ai.
        # touples
        self.freePool = [(i,j) for i in range(10) for j in range(10)]

        shipSizes = [2,3,3,4,5]
        for ship in shipSizes:
            successfulPlace = False
            print(f"Size: {ship}")
            while not successfulPlace:
                init = self.getRandomFreeSpace()
                direction = random.randrange(0, 3)

                if direction == 0:
                    indicies = self.checkShipSpacesLeft(init, ship)
                    successfulPlace = self.setShips(indicies, ship)
                elif direction == 1:
                    indicies = self.checkShipSpacesRight(init, ship)
                    successfulPlace = self.setShips(indicies, ship)
                elif direction == 2:
                    indicies = self.checkShipSpacesUp(init, ship)
                    successfulPlace = self.setShips(indicies, ship)
                elif direction == 3:
                    indicies = self.checkShipSpacesDown(init, ship)
                    successfulPlace = self.setShips(indicies, ship)
                else:
                    print("Direction Error")

    def setShips(self,indicies,ship):
        if indicies != None:
            # create ship part
            newShip = Ship(ship)
            for tile in indicies:
                self.removeSpace(tile)
                self.board[tile[0]][tile[1]].setShipReference(newShip)
                self.board[tile[0]][tile[1]].placeShipPiece(newShip,self.display,tile)
            return True     

    def checkShipSpacesLeft(self, init, size):
        next = (init[0],init[1])
        indicies = []
        indicies.append(next)
        for i in range(size):
            next = (next[0]-1,next[1])
            if not self.isSpaceFree(next[0],next[1]):
                return None
            indicies.append(next)
        print(indicies)
        return indicies

    def checkShipSpacesRight(self, init, size):
        next = (init[0],init[1])
        indicies = []
        indicies.append(next)
        for i in range(size):
            next = (next[0]+1,next[1])
            if not self.isSpaceFree(next[0],next[1]):
                return None
            indicies.append(next)

        return indicies

    def checkShipSpacesUp(self, init, size):
        next = (init[0],init[1])
        indicies = []
        indicies.append(next)
        for i in range(size):
            next = (next[0],next[1]-1)
            if not self.isSpaceFree(next[0],next[1]):
                return None
            indicies.append(next)

        return indicies

    def checkShipSpacesDown(self, init, size):
        next = (init[0],init[1])
        indicies = []
        indicies.append(next)
        for i in range(size):
            next = (next[0],next[1]+1)
            if not self.isSpaceFree(next[0],next[1]):
                return None
            indicies.append(next)

        return indicies

    '''
        Check the status of grid space x,y. returns
    '''
    def checkSpace(self, x, y):
        return self.board[x][y]

    def getRandomFreeSpace(self):
        return random.choice(self.freePool)

    def removeSpace(self, coords):
        # o(n)
        # searches list and removes element with that value.
        # throws ValueError if the value is not found inside the list
        # add in try/catch later
        self.freePool.remove(coords)

    def isSpaceFree(self, x, y):
        # ValueError to return none
        try:
            newID = self.freePool.index((x,y))
        except ValueError as err:
            print(f"{x+1,y+1} is out of bounds or taken.")
            return False
        return newID

    '''
        Expects to recieve: a ship object, an integer for the size of the ship,
        and an array of touples? representing the corrdinates of where the ship is placed.
    '''
    def placeShip(self, ship, size, coordinates):
        # check if the coordinates passed in are in a straight line
        #z and there are no collisions.
        # inverted list?
        for coord in coordinates:
            # error check
            self.board[coord[0]][coord[1]].placeShipPiece()
