import random
from shipClass import *

'''
    This class will track information about the game state.
    Ship locations, etc.
'''

class Bullet:
    
    def __init__(self):
        self.target = [0,0]
        
class SpBullet(Bullet):
    
    def __init__(self, targets):
        Bullet.__init__(self)
        #Targets = [[0,0], [0,1], [1,0], etc.]
        self.targets = targets
        self.targets.append(self.target)

class GameBoardTile:

    def __init__(self, xCoord, yCoord, row, column, display):
        self.debug_mode = True
        self.x = xCoord
        self.y = yCoord
        self.row = row      #row the tile in in
        self.col = column   #column the tile is in
        self.ship = False   #boolean for if there is a ship piece
        self.hit = False    #boolean for if this space has already been hit
        self.shipReference = None
        self.display = display
        self.displayW, self.displayH = display.get_size()

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

    def getImg(self,sType):
        shipImg = pygame.image.load(f'sprites/ship{sType}.jpg')
        shipImg = pygame.transform.scale(shipImg, (round((4*self.displayH*1.3)/50), round((4*self.displayH)/50)))
        return shipImg

    def placeShipPiece(self, ship):
        if not self.ship:
            self.ship = True
            if self.debug_mode:
                print(f"Placing {ship} on tile {self.row}, {self.col}")
                cell = (round(self.displayW/10)+((self.col-1)*(round((4*self.displayH*1.3)/50))), round(self.displayH/10)+((self.row-1)*(round((4*self.displayH)/50))))
                self.display.blit(self.getImg(ship.getSize()), cell)
            return True
        return False
        
    '''
        draws a hit mark on the game screen?
    '''
    def isHit(self):
        return self.hit
    
    def fire(self):
        self.hit = True
        cell = (round(self.displayW/10)+((self.col-1)*(round((4*self.displayH*1.3)/50))), round(self.displayH/10)+((self.row-1)*(round((4*self.displayH)/50))))
        if self.ship:
            self.display.blit(self.getImg("hit"), cell)
            self.shipReference.hit()
            if self.debug_mode:
                print(self.shipReference)
            if self.shipReference.isAlive():
                return True, True
            else:
                return True, False
        self.display.blit(self.getImg("miss"), cell)
        return False, False

    def getShipImgNum(self):
        return self.shipReference.getImgNum()

class GameBoard:

    def __init__(self, mainboard):
        # initially 10 x 10 grid, based on grid drawn in 'battleprotoNew.py'
        self.debug = True
        self.board = mainboard
        self.shipCount = 5
        self.shipsLeft = 5
        # creates inverted list of all free spaces. Useful for the ai.
        # touples
        self.freePool = [(i,j) for i in range(10) for j in range(10)]

        shipSizes = [2,3,3,4,5]
        for ship in shipSizes:
            successfulPlace = False
            if self.debug:
                print(f"Size: {ship}")
            while not successfulPlace:
                init = self.getRandomFreeSpace()
                direction = random.randrange(0, 3)

                if direction == 0:
                    indicies = self.checkShipSpacesLeft(init, ship-1)
                    successfulPlace = self.setShips(indicies, ship)
                elif direction == 1:
                    indicies = self.checkShipSpacesRight(init, ship-1)
                    successfulPlace = self.setShips(indicies, ship)
                elif direction == 2:
                    indicies = self.checkShipSpacesUp(init, ship-1)
                    successfulPlace = self.setShips(indicies, ship)
                elif direction == 3:
                    indicies = self.checkShipSpacesDown(init, ship-1)
                    successfulPlace = self.setShips(indicies, ship)
                else:
                    print("Direction Error")

    def setShips(self,indicies,ship):
        if indicies != None:
            # create ship part
            newShip = Ship(ship,self.shipCount)
            self.shipCount -= 1
            for tile in indicies:
                self.removeSpace(tile)
                self.board[tile[0]][tile[1]].setShipReference(newShip)
                self.board[tile[0]][tile[1]].placeShipPiece(newShip)
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
            if self.debug:
                print(f"{y+1,x+1} is out of bounds or taken.")
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
            
    def shipLoss(self):
        self.shipsLeft -= 1

    def checkWin(self):
        if not self.shipsLeft > 0:
            return True
        return False
    
