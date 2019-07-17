import random
import "shipClass.py"
'''
    This class will track information about the game state.
    Ship locations, etc.
'''

class GameBoardSpace:

    # maybe a bit over-engineered
    def __init__(self):
        self.ship = False #boolean for if there is a ship piece
        self.hit = False #boolean for if this space has already been hit
        self.open = True #boolean for checking if this space is occupied by a ship
        self.shipReference = None
        # states: the space is empty:

    def setShipReference(self, ship):
        if self.shipReference == None:
            self.shipReference = ship


    def placeShipPiece(self):
        # return true/false for error checking in game board class
        if !self.ship:
            self.ship = True
            self.open = False
            # put ship drawing code here
            return True
        return False

    '''
        draws a hit mark on the game screen?
    '''
    def hit(self):
        if !self.hit:
            self.hit = True
            return True
        return False

class GameBoard:

    # 2 3 3 4 5

    def __init__(self, height=10, width=10):
        # initially 10 x 10 grid, based on grid drawn in 'battleprotoNew.py'
        self.height = height
        self.width = width
        self.board = [[GameBoardSpace() for h in range(height)] for w in range(width)]

        # creates inverted list of all free spaces. Useful for the ai.
        # touples
        self.freePool = [(i,j) for i in range(height) for j in range(width)]

        shipSizes = [2,3,3,4,5]
        successfulPlace = False
        for ship in shipSizes:

            while !successfulPlace:
                init = self.getRandomFreeSpace()
                direction = random.randrange(0, 3)

                if direction == 0:
                    indicies = self.checkShipSpacesRight(init, ship)
                    if indicies != None:
                        # create ship part
                        newShip = Ship()
                        for index in indicies:
                            space = self.freePool[index]
                            self.removeSpace(space[0], space[1])
                            self.board[space[0]][space[1]].setShipReference(newShip)
                            self.board[space[0]][space[1]].placeShipPiece(newShip)
                        successfulPlace = True

                if direction == 1:
                    indicies = self.checkShipSpacesDown(init, ship)
                    if indicies != None:
                        # create ship part
                        newShip = Ship()
                        for index in indicies:
                            space = self.freePool[index]
                            self.removeSpace(space[0], space[1])
                            self.board[space[0]][space[1]].setShipReference(newShip)
                            self.board[space[0]][space[1]].placeShipPiece(newShip)
                        successfulPlace = True

                if direction == 2:
                    indicies = self.checkShipSpacesLeft(init, ship)
                    if indicies != None:
                        # create ship part
                        newShip = Ship()
                        for index in indicies:
                            space = self.freePool[index]
                            self.removeSpace(space[0], space[1])
                            self.board[space[0]][space[1]].setShipReference(newShip)
                            self.board[space[0]][space[1]].placeShipPiece(newShip)
                        successfulPlace = True

                if direction == 3:
                    indicies = self.checkShipSpacesUp(init, ship)
                    if indicies != None:
                        # create ship part
                        newShip = Ship()
                        for index in indicies:
                            space = self.freePool[index]
                            self.removeSpace(space[0], space[1])
                            self.board[space[0]][space[1]].setShipReference(newShip)
                            self.board[space[0]][space[1]].placeShipPiece(newShip)
                        successfulPlace = True

    def checkShipSpacesLeft(self, init, size):
        next = (init[0],init[1])
        indicies = []
        indicies.append(next)
        for i in range(size):
            next = (next[0]-1,next[1])
            if self.isSpaceFree(next[0],next[1]) == None: # more pythonic to use 'is'
                return None
            indicies.append(next)

        return indicies

    def checkShipSpacesRight(self, init, size):
        next = (init[0],init[1])
        indicies = []
        indicies.append(next)
        for i in range(size):
            next = (next[0]+1,next[1])
            if self.isSpaceFree(next[0],next[1]) == None:
                return None
            indicies.append(next)

        return indicies

    def checkShipSpacesUp(self, init, size):
        next = (init[0],init[1])
        indicies = []
        indicies.append(next)
        for i in range(size):
            next = (next[0],next[1]-1)
            if self.isSpaceFree(next[0],next[1]) == None:
                return None
            indicies.append(next)

        return indicies

    def checkShipSpacesDown(self, init, size):
        next = (init[0],init[1])
        indicies = []
        indicies.append(next)
        for i in range(size):
            next = (next[0],next[1]+1)
            if self.isSpaceFree(next[0],next[1]) == None:
                return None
            indicies.append(next)

        return indicies

    '''
        Check the status of grid space x,y. returns
    '''
    def checkSpace(self, x, y):
        return self.board[x][y]

    def getRandomFreeSpace(self):
        return random.randrange(len(self.freePool))
        # maybe remove from free space

    def removeSpace(self, x, y):
        # o(n)
        # searches list and removes element with that value.
        # throws ValueError if the value is not found inside the list
        # add in try/catch later
        self.freePool.remove((x,y))

    def isSpaceFree(self, x, y):
        # ValueError to return none
        return self.freePool.index((x,y))

    '''
        Expects to recieve: a ship object, an integer for the size of the ship,
        and an array of touples? representing the corrdinates of where the ship is placed.
    '''
    def placeShip(self, ship, size, coordinates):
        # check if the coordinates passed in are in a straight line
        # and there are no collisions.
        # inverted list?

        for coord in coordinates:
            # error check
            self.board[coord[0]][coord[1]].placeShipPiece()
