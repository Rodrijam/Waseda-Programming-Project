import pygame
import time
from pygame.locals import *
from shipClass import *
from gameBoard import *

#Initializes Pygame and Pygame's Font
pygame.init()
pygame.font.init()
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

debug = True;

placeLocation = (0,0)

gameTiles = []
mainBoard = []

clock = pygame.time.Clock()

def game_setup(screenWidth = 1200, screenHeight = 675):

    #Display Setup
    #screenDisp = pygame.display.set_mode((screenWidth,screenHeight), pygame.RESIZABLE)
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
    #491x84

    for i in range(5):
        shipRect = pygame.Surface((screenWidth - innerWidth - cellWidth*2, innerCellHeight))
        shipRect.fill(BLACK)
        screenDisp.blit(shipRect,(innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*(2+i)))
        sshipImg = pygame.image.load(f'sprites/sideship{i+1}IN.png')
        sshipImg = pygame.transform.scale(sshipImg, (round(screenWidth - innerWidth - cellWidth*2), innerCellHeight))
        screenDisp.blit(sshipImg, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*(2+i)))
        #pygame.draw.rect(screenDisp, RED, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*(2+i), screenWidth - innerWidth - cellWidth*2, innerCellHeight), 1)

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
            #print (j)

    #Image Check
    if debug:
        imageSetPoint = (round(cellWidth)+innerCellWidth*10, round(cellHeight)+innerCellHeight*10)
        imageSetPoint2 = (round(cellWidth), round(cellHeight))
        pygame.draw.circle(screenDisp, RED, (imageSetPoint), 10, 1)
        pygame.draw.circle(screenDisp, RED, (imageSetPoint2), 10, 1)



    return screenDisp

def game_start(screenDisp, compGameBoard):

    #NOT EFFICIENT REPEATED
    screenWidth = screenDisp.get_width()
    screenHeight = screenDisp.get_height()

    #Buffer Cells
    cellWidth = round(screenWidth/10)
    cellHeight = round(screenHeight/10)

    #True Cells
    innerHeight = screenHeight - (2*cellHeight)
    innerWidth = innerHeight * 1.3
    innerCellWidth = round((innerHeight*1.3)/10)
    innerCellHeight = round(innerHeight/10)

    seg = (screenWidth - innerWidth - cellWidth*2) / 4

    shipTest = True
    turnCounter = 0
    activePower = 0
    redraw = True
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            #elif event.type == VIDEORESIZE:
            #    game_setup(screenDisp.get_width(), screenDisp.get_height())
            elif event.type == MOUSEBUTTONDOWN:
                mouseClick = pygame.mouse.get_pos()
                if mouseClick[0] > innerWidth + cellWidth*1.5 and mouseClick[0] < innerWidth + cellWidth*1.5 + seg*4 and \
                   mouseClick[1] > cellHeight + innerCellHeight*9 and mouseClick[1] < cellHeight + innerCellHeight*9 + innerCellHeight:
                    if mouseClick[0] < innerWidth + cellWidth*1.5 + seg:
                        if activePower != 1:
                            #activate power 1 
                            redraw = True
                            activePower = 1
                            #currentPower = specialBullet()
                        else:
                            activePower = 0

                    elif mouseClick[0] < innerWidth + cellWidth*1.5 + seg*2 and mouseClick[0] > innerWidth + cellWidth*1.5 + seg:
                        if activePower != 2:
                            #activate power 2
                            redraw = True
                            activePower = 2
                        else:
                            activePower = 0

                    elif mouseClick[0] < innerWidth + cellWidth*1.5 + seg*3 and mouseClick[0] > innerWidth + cellWidth*1.5 + seg*2:
                        if activePower !=3:
                            #activate power 3
                            redraw = True
                            activePower = 3
                        else:
                            activePower = 0

                    elif mouseClick[0] > innerWidth + cellWidth*1.5 + seg*3:
                        if activePower != 4:
                            #activate power 4
                            redraw = True
                            activePower = 4
                        else:
                            activePower = 0
                            
                    else:
                        print("Power Error")
                    if debug:
                        print(f"Using Power: {activePower}")

                    if activePower == 0 or redraw:
                     #redraw power boxes (not efficient)
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
                        redraw = False
                    if activePower != 0:
                        selectRect = pygame.Surface((seg, innerCellHeight))
                        selectRect.fill(YELLOW)
                        selectRect.set_alpha(128)
                        screenDisp.blit(selectRect,(innerWidth + cellWidth*1.5 + seg*(activePower-1), cellHeight + innerCellHeight*9))

                    
                    #powerRect = pygame.Surface((cellseg, innerCellHeight))
                    #powerRect.fill(RED)
                    #screenDisp.blit(powerRect,(innerWidth + cellWidth*1.5 + seg*i, cellHeight + innerCellHeight*9))
                
                        #Check for powerUp Click
                        #if within range of powerup
                            #if specialBulletTile.isActive and specialBullet !=  specialBulletTile.spBullet:
                                #specialBullet.tileActive = False
                                #specialBullet = specialBulletTile.spBullet
                                #specialBullet.tileActive = True
                            #elif specialBulletTile.isActive and specialBullet =  specialBulletTile.spBullet:
                                #specialBulletTile.isActive = False
                                #specialBullet = None
                            #elif not specialBulletTile.isActive:
                                #specialBullet = specialBulletTile.spBullet
                                #specialBullet.tileActive = True
                        #Else
                elif mouseClick[0] > cellWidth and mouseClick[0] < cellWidth + innerWidth and mouseClick[1] > cellHeight and mouseClick[1] < cellHeight + innerHeight:
                    try:
                        if debug:
                            pygame.draw.rect(screenDisp, BLACK, (mouseClick[0] - 5, mouseClick[1] - 5, 10,10), 1)
                        #gamespace = ()
                        #top_left = round(cellWidth), round(cellHeight)
                        #bottom_right = round(cellWidth)+innerCellWidth*10, round(cellHeight)+innerCellHeight*10
                        xTile = int((mouseClick[0] - cellWidth) / innerCellWidth)
                        yTile = int((mouseClick[1] - cellHeight) / innerCellHeight)
                        clickedTile = mainBoard[xTile][yTile]
                        if debug:
                            print(clickedTile)
                        if ( not clickedTile.isHit()):
                            specialBullet = None #temp
                            print(activePower)
                            if specialBullet != None:
                                for target in specialBullet.targets:
                                    isShip, isAlive = mainBoard[xTile + target[0]][yTile + target[1]].fire()
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
    print(grade)
    file.write(f"Name: XYZ Score: {turnCounter} Grade:{scoreTable[grade]}\n")
    file.close()

screen = game_setup()
#screen = game_setup(vidInfo.current_w, vidInfo.current_h)
compGameBoard = GameBoard(mainBoard)
score = game_start(screen, compGameBoard)
game_end(screen, score)
save_to_file(score)
