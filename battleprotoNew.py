import pygame
import time
from pygame.locals import *
from shipClass import *
from gameBoard import *

#Initializes Pygame and Pygame's Font
pygame.init()
setFont = pygame.font.SysFont('Comic Sans MS', 100)

#Used for determining user's screen size
vidInfo = pygame.display.Info()

#Color & Image Definitions
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (192,192,192)
YELLOW = (255,255,0)

debug = False;

placeLocation = (0,0)

gameTiles = []
mainBoard = []

powerList = [1,2,3,4]

clock = pygame.time.Clock()


"""
Game Setup
by James Rodriguez
"""

def game_setup(screenWidth = 1200, screenHeight = 675):

    #Display Setup
    screenDisp = pygame.display.set_mode((screenWidth,screenHeight))
    pygame.display.set_caption("Basic Battleship")
    pygame.display.set_icon(pygame.image.load("sprites/ship1.png"))

    #Buffer Cells
    cellWidth = round(screenWidth/10)
    cellHeight = round(screenHeight/10)

    #True Cells
    innerHeight = screenHeight - (2*cellHeight)
    innerWidth = innerHeight * 1.3
    innerCellWidth = round((innerHeight*1.3)/10)
    innerCellHeight = round(innerHeight/10)

    #Display Modification
    screenDisp.fill(WHITE)

    loadingScreen = setFont.render("Loading...", False, (0, 0, 0))
    screenDisp.blit(loadingScreen,(screenWidth/3, screenHeight/3))
    pygame.display.update()

    #Water Image Display
    waterImg = pygame.image.load('sprites/watertile.jpg')
    waterImg = pygame.transform.scale(waterImg, (innerCellWidth, innerCellHeight))
    for i in range (10):
        for j in range(10):
            screenDisp.blit(waterImg, (cellWidth + (i*innerCellWidth), cellHeight + (j*innerCellHeight)))

    #Side Menu Display
    movesRect = pygame.Surface((screenWidth - innerWidth - cellWidth*2, innerCellHeight))
    movesRect.fill(GREY)
    shipsRect = pygame.Surface((screenWidth - innerWidth - cellWidth*2, innerCellHeight*6))
    shipsRect.fill(GREY)
    powerRect = pygame.Surface((screenWidth - innerWidth - cellWidth*2, innerCellHeight*2))
    powerRect.fill(GREY)
    screenDisp.blit(movesRect,(innerWidth + cellWidth*1.5, cellHeight - innerCellHeight))
    screenDisp.blit(shipsRect,(innerWidth + cellWidth*1.5, cellHeight + innerCellHeight))
    screenDisp.blit(powerRect,(innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*8))


    #Moves Box
    movesText = setFont.render(" Moves: 0", False, (0, 0, 0))
    movesText = pygame.transform.scale(movesText, (round(screenWidth - innerWidth - cellWidth*2)-innerCellWidth, innerCellHeight))
    screenDisp.blit(movesText,(innerWidth + cellWidth*1.5, cellHeight - innerCellHeight))

    pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5, cellHeight - innerCellHeight, screenWidth - innerWidth - cellWidth*2, innerCellHeight), 1)

    #Ships Remaining Box
    shipsText = setFont.render(" Ships Remaining ", False, (0, 0, 0))
    shipsText = pygame.transform.scale(shipsText, (round(screenWidth - innerWidth - cellWidth*2), innerCellHeight))
    screenDisp.blit(shipsText,(innerWidth + cellWidth*1.5, cellHeight + innerCellHeight))
    pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight, screenWidth - innerWidth - cellWidth*2, innerCellHeight), 1)

    if debug:
        pygame.draw.rect(screenDisp, RED, (innerWidth + cellWidth*1.5 + (screenWidth - innerWidth - cellWidth*2), cellHeight + innerCellHeight, innerCellHeight, innerCellHeight), 1)

    for i in range(5):
        shipRect = pygame.Surface((screenWidth - innerWidth - cellWidth*2, innerCellHeight))
        shipRect.fill(BLACK)
        screenDisp.blit(shipRect,(innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*(2+i)))
        sshipImg = pygame.image.load(f'sprites/sideship{i+1}IN.png')
        sshipImg = pygame.transform.scale(sshipImg, (round(screenWidth - innerWidth - cellWidth*2), innerCellHeight))
        screenDisp.blit(sshipImg, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*(2+i)))

    pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight, screenWidth - innerWidth - cellWidth*2, innerCellHeight*6), 1)

    #Powers Box
    powersText = setFont.render(" Powers ", False, (0, 0, 0))
    powersText = pygame.transform.scale(powersText, (round(screenWidth - innerWidth - cellWidth*2), innerCellHeight))
    screenDisp.blit(powersText,(innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*8))
    

    seg = (screenWidth - innerWidth - cellWidth*2) / 4

    for i in range(4):
        powerImg = pygame.image.load(f'sprites/power{i+1}.png')
        powerImg = pygame.transform.scale(powerImg, (round(seg), innerCellHeight))
        screenDisp.blit(powerImg,(innerWidth + cellWidth*1.5 + seg*i, cellHeight + innerCellHeight*9))
        pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5 + seg*i, cellHeight + innerCellHeight*9, seg, innerCellHeight), 1)


    pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*8, screenWidth - innerWidth - cellWidth*2, innerCellHeight*2), 1)

    #Drawing the Grid with Tiles
    for i in range (10):
        rowSet = []
        for j in range(10):
            newTile = GameBoardTile(cellWidth + (i*innerCellWidth),cellHeight + (j*innerCellHeight),j+1,i+1, screenDisp)
            rowSet.append(newTile)

          #Axis Labels
            gFill = pygame.Surface((innerCellWidth, innerCellHeight))
            gFill.fill(GREY)
            screenDisp.blit(gFill,(cellWidth + (i*innerCellWidth), cellHeight - innerCellHeight ))
            screenDisp.blit(gFill,(cellWidth - innerCellWidth, cellHeight + (j*innerCellHeight)))

            pygame.draw.rect(screenDisp, BLUE, (cellWidth + (i*innerCellWidth), cellHeight - innerCellHeight , innerCellWidth, innerCellHeight), 1)
            pygame.draw.rect(screenDisp, BLUE, (cellWidth - innerCellWidth, cellHeight + (j*innerCellHeight) , innerCellWidth, innerCellHeight), 1)

            letterSurfaceSide = setFont.render(f"{j+1}", False, (0, 0, 0))
            letterSurfaceTop = setFont.render(chr(65+i), False, (0, 0, 0))
            letterSurfaceSide = pygame.transform.scale(letterSurfaceSide, (round(innerCellWidth/2), round(innerCellHeight/2)))
            letterSurfaceTop = pygame.transform.scale(letterSurfaceTop, (round(innerCellWidth/2), round(innerCellHeight/2)))
            screenDisp.blit(letterSurfaceSide,(cellWidth - innerCellWidth*0.75, cellHeight + (j*innerCellHeight)+innerCellHeight*0.25))
            screenDisp.blit(letterSurfaceTop,(cellWidth + (i*innerCellWidth)+innerCellWidth*0.25, cellHeight - innerCellHeight*0.75))

        mainBoard.append(rowSet)

    for i in mainBoard:
        for j in i:
            pygame.draw.rect(screenDisp, RED, (j.getX(), j.getY(), innerCellWidth, innerCellHeight), 1)

    #Image Check
    if debug:
        imageSetPoint = (round(cellWidth)+innerCellWidth*10, round(cellHeight)+innerCellHeight*10)
        imageSetPoint2 = (round(cellWidth), round(cellHeight))
        pygame.draw.circle(screenDisp, RED, (imageSetPoint), 10, 1)
        pygame.draw.circle(screenDisp, RED, (imageSetPoint2), 10, 1)



    return screenDisp

def clearPower(screenDisp): 

    powerRect = pygame.Surface((screenWidth - innerWidth - cellWidth*2, innerCellHeight*2))
    powerRect.fill(GREY)
    screenDisp.blit(powerRect,(innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*8))
    powersText = setFont.render(" Powers ", False, (0, 0, 0))
    powersText = pygame.transform.scale(powersText, (round(screenWidth - innerWidth - cellWidth*2), innerCellHeight))
    screenDisp.blit(powersText,(innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*8))
    for i in range(4):
        powerImg = pygame.image.load(f'sprites/power{i+1}.png')
        powerImg = pygame.transform.scale(powerImg, (round(seg), innerCellHeight))
        screenDisp.blit(powerImg,(innerWidth + cellWidth*1.5 + seg*i, cellHeight + innerCellHeight*9))
        pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5 + seg*i, cellHeight + innerCellHeight*9, seg, innerCellHeight), 1)
    pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*8, screenWidth - innerWidth - cellWidth*2, innerCellHeight*2), 1)
    for j in range(4):
        print(f"J: {j} PowerList: {powerList}")
        if j+1 not in powerList:
            powerImg = pygame.image.load('sprites/icon.png')
            powerImg = pygame.transform.scale(powerImg, (round(seg), innerCellHeight))
            screenDisp.blit(powerImg,(innerWidth + cellWidth*1.5 + seg*j, cellHeight + innerCellHeight*9))

def game_start(screenDisp, compGameBoard):

    #PowerSetUp

    XPowerUp = SpBullet([[-1, -1], [1, -1], [-1, 1], [1,1]])
    CrossPowerUp = SpBullet([[-1, 0], [0, -1], [0, 1], [0, 2], [1, 0]])
    SideLPowerUp = SpBullet([[0, 1], [1, 0], [2, 0]])
    JPowerUp = SpBullet([[-1, 0], [0, 1], [0, 2]])

    shipTest = True
    turnCounter = 0
    activePower = 0
    specialBullet = None

    """
    Mouse Click Detection
    by Chun Tat Chan & James Rodriguez
    """
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN:
                mouseClick = pygame.mouse.get_pos()
                if (mouseClick[0] > innerWidth + cellWidth*1.5 and mouseClick[0] < innerWidth + cellWidth*1.5 + seg*4 and \
                   mouseClick[1] > cellHeight + innerCellHeight*9 and mouseClick[1] < cellHeight + innerCellHeight*9 + innerCellHeight):
                    clearPower(screenDisp)
                    if mouseClick[0] < innerWidth + cellWidth*1.5 + seg and 1 in powerList:
                        if activePower != 1:
                            #activate power 1 
                            activePower = 1
                            specialBullet = XPowerUp 
                        else:
                            activePower = 0

                    elif mouseClick[0] < innerWidth + cellWidth*1.5 + seg*2 and mouseClick[0] > innerWidth + cellWidth*1.5 + seg and 2 in powerList:
                        if activePower != 2:
                            #activate power 2
                            activePower = 2
                            specialBullet = CrossPowerUp 
                        else:
                            activePower = 0

                    elif mouseClick[0] < innerWidth + cellWidth*1.5 + seg*3 and mouseClick[0] > innerWidth + cellWidth*1.5 + seg*2 and 3 in powerList:
                        if activePower !=3:
                            #activate power 3
                            activePower = 3
                            specialBullet = SideLPowerUp
                        else:
                            activePower = 0

                    elif mouseClick[0] > innerWidth + cellWidth*1.5 + seg*3 and 4 in powerList:
                        if activePower != 4:
                            #activate power 4
                            activePower = 4
                            specialBullet = JPowerUp 
                        else:
                            activePower = 0
                            
                    else:
                        print("Power Error")
                    if debug:
                        print(f"Using Power: {activePower}")
                        
                    if activePower == 0:
                        clearPower(screenDisp)
                        specialBullet = None

                    if activePower != 0:
                        selectRect = pygame.Surface((seg, innerCellHeight))
                        selectRect.fill(YELLOW)
                        selectRect.set_alpha(128)
                        screenDisp.blit(selectRect,(innerWidth + cellWidth*1.5 + seg*(activePower-1), cellHeight + innerCellHeight*9))
                elif mouseClick[0] > cellWidth and mouseClick[0] < cellWidth + innerWidth and mouseClick[1] > cellHeight and mouseClick[1] < cellHeight + innerHeight:
                    try:
                        if debug:
                            pygame.draw.rect(screenDisp, BLACK, (mouseClick[0] - 5, mouseClick[1] - 5, 10,10), 1)
                        xTile = int((mouseClick[0] - cellWidth) / innerCellWidth)
                        yTile = int((mouseClick[1] - cellHeight) / innerCellHeight)
                        clickedTile = mainBoard[xTile][yTile]
                        if debug:
                            print(clickedTile)
                        if ( not clickedTile.isHit()):
                            if specialBullet != None:
                                for target in specialBullet.targets:
                                    if (xTile + target[0] >= 0 and xTile + target[0] < 10 and yTile + target[1] >= 0 and yTile + target[1] < 10):
                                        isShip, isAlive = mainBoard[xTile + target[0]][yTile + target[1]].fire()
                                powerList.remove(activePower)
                                activePower = 0
                                specialBullet = None
                                clearPower(screenDisp)
                            else:
                                isShip, isAlive = clickedTile.fire()
                            if isShip:
                                if not isAlive:
                                    if debug:
                                        print("DEATH")
                                    shipRect = pygame.Surface((screenWidth - innerWidth - cellWidth*2, innerCellHeight))
                                    shipRect.fill(BLACK)
                                    screenDisp.blit(shipRect,(innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*(2+clickedTile.getShipImgNum()-1)))
                                    sshipImg = pygame.image.load(f'sprites/sideship{clickedTile.getShipImgNum()}OUT.png')
                                    sshipImg = pygame.transform.scale(sshipImg, (round(screenWidth - innerWidth - cellWidth*2), innerCellHeight))
                                    screenDisp.blit(sshipImg, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*(2+clickedTile.getShipImgNum()-1)))
                                    compGameBoard.shipLoss()
                            turnCounter += 1
                            movesRect = pygame.Surface((round(innerCellWidth), innerCellHeight*0.9))
                            movesRect.fill(GREY)
                            screenDisp.blit(movesRect,(innerWidth + cellWidth*1.5 + innerCellWidth*2.3, cellHeight - innerCellHeight*0.9))
                            movesText = setFont.render(f"{turnCounter}", False, (0, 0, 0))
                            movesText = pygame.transform.scale(movesText, (round(innerCellWidth*0.7), innerCellHeight))
                            screenDisp.blit(movesText,(innerWidth + cellWidth*1.5 + innerCellWidth*2.3, cellHeight - innerCellHeight))
                    except IndexError:
                        pass

                #Destruction testing
                if debug:
                    if mouseClick[0] > innerWidth + cellWidth*1.5 + (screenWidth - innerWidth - cellWidth*2) and \
                       mouseClick[0] < innerWidth + cellWidth*1.5 + (screenWidth - innerWidth - cellWidth*2) + innerCellHeight and \
                       mouseClick[1] > cellHeight + innerCellHeight and mouseClick[1] < cellHeight + innerCellHeight*2:
                        print("INSTANT DEATH")
                        for i in range (compGameBoard.shipsLeft):
                            compGameBoard.shipLoss()

        #Check here for end of game...
        if compGameBoard.checkWin():
            pygame.display.update()
            for i in [3,2,1]:
                if i != 3:
                    time.sleep(1)
                numFill = pygame.Surface((innerCellWidth, innerCellHeight*2.1))
                numFill.fill(WHITE)
                screenDisp.blit(numFill, (screenWidth/3.05, screenHeight/2.8))
                endScreen = setFont.render(f"{i}", False, (0, 0, 0))
                screenDisp.blit(endScreen,(screenWidth/3, screenHeight/3))
                pygame.display.update()
            time.sleep(1)
            pygame.display.update()
            return turnCounter



        pygame.display.update()


def game_end(screenDisp, score):
    screenWidth = screenDisp.get_width()
    screenHeight = screenDisp.get_height()
    screenDisp.fill(WHITE)
    endScreen = setFont.render("Finished!", False, (0, 0, 0))
    screenDisp.blit(endScreen,(screenWidth/3, screenHeight/10))
    scoreText = setFont.render(f"Your score is:", False, (0, 0, 0))
    screenDisp.blit(scoreText,(screenWidth/4, screenHeight/3))
    movesText = setFont.render(f"{score} Moves!", False, (0, 0, 0))
    screenDisp.blit(movesText,(screenWidth/3, screenHeight - screenHeight*0.4))
    pygame.display.update()


"""
File Save by Ryan Yu
"""
def save_to_file(turnCounter):
    file = open("score.txt", "a")
    scoreTable = {
        10: "A",
        9: "B",
        8: "C",
        7: "D",
        6: "D",
        5: "D",
        4: "D",
        3: "D",
        2: "D",
        1: "D",
        0: "D"
    }
    grade = int((17 / turnCounter) * 10)
    file.write(f"Name: XYZ Score: {turnCounter} Grade:{scoreTable[grade]} Powers Used:{4-len(powerList)}\n")
    file.close()

screen = game_setup()

screenWidth = screen.get_width()
screenHeight = screen.get_height()

#Buffer Cells
cellWidth = round(screenWidth/10)
cellHeight = round(screenHeight/10)

#True Cells
innerHeight = screenHeight - (2*cellHeight)
innerWidth = innerHeight * 1.3
innerCellWidth = round((innerHeight*1.3)/10)
innerCellHeight = round(innerHeight/10)

seg = (screenWidth - innerWidth - cellWidth*2) / 4  


compGameBoard = GameBoard(mainBoard)
score = game_start(screen, compGameBoard)
game_end(screen, score)
save_to_file(score)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
