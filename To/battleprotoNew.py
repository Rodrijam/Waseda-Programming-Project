import pygame
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

placeLocation = (0,0)

gameTiles = []
gameBoard = []

clock = pygame.time.Clock()

def game_setup(screenWidth = 1200, screenHeight = 675):

    #Display Setup
    screenDisp = pygame.display.set_mode((screenWidth,screenHeight), pygame.RESIZABLE)
    pygame.display.set_caption("Basic Battleship")


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
    waterImg = pygame.image.load('sprites/watertile.jpg')
    waterImg = pygame.transform.scale(waterImg, (innerCellWidth, innerCellHeight))
    
    #Water Image Display
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
            
            pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5, cellHeight - innerCellHeight, screenWidth - innerWidth - cellWidth*2, innerCellHeight), 1)
            pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight, screenWidth - innerWidth - cellWidth*2, innerCellHeight*6), 1)
            pygame.draw.rect(screenDisp, GREEN, (innerWidth + cellWidth*1.5, cellHeight + innerCellHeight*8, screenWidth - innerWidth - cellWidth*2, innerCellHeight*2), 1)

    #Drawing the Grid with rectangles
    for i in range (10):
        rowSet = []
        for j in range(10):
            print(f"Making Col {j+1}")
            newTile = Tile(cellWidth + (i*innerCellWidth),cellHeight + (j*innerCellHeight),i+1,j+1)
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

        gameBoard.append(rowSet)
    
    for i in gameBoard:
        for j in i:
            pygame.draw.rect(screenDisp, RED, (j.getX(), j.getY(), innerCellWidth, innerCellHeight), 1)
            print (j)

    #Image Check
    imageSetPoint = (round(cellWidth)+innerCellWidth*10, round(cellHeight)+innerCellHeight*10)
    imageSetPoint2 = (round(cellWidth), round(cellHeight))
    pygame.draw.circle(screenDisp, RED, (imageSetPoint), 10, 1)
    pygame.draw.circle(screenDisp, RED, (imageSetPoint2), 10, 1)
            
            

    return screenDisp


def game_start(screenDisp):

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
    
    while True:
        turnCounter = 0
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            #elif event.type == VIDEORESIZE:
            #    game_setup(screenDisp.get_width(), screenDisp.get_height())
            elif event.type == MOUSEBUTTONDOWN:
                mouseClick = pygame.mouse.get_pos()
                #pygame.draw.rect(screenDisp, BLACK, (mouseClick[0], mouseClick[1], 10,10), 1)
                gamespace = ()
                top_left = round(cellWidth), round(cellHeight)
                bottom_right = round(cellWidth)+innerCellWidth*10, round(cellHeight)+innerCellHeight*10
                #First Column is 1; not 0
                xTile = int((mouseClick[0] - cellWidth) / innerCellWidth)
                yTile = int((mouseClick[1] - cellHeight) / innerCellHeight)
                try:
                    clickedTile = gameBoard[xTile][yTile]
                    #imageSetPoint = ())
                    #pygame.draw.circle(screenDisp, RED, (imageSetPoint), 10, 1)
                    print(mouseClick[0])
                    print(mouseClick[1])
                    print(xTile)
                    print(yTile)
                    print(clickedTile)
                    if ( not clickedTile.getHit()):
                        if (clickedTile.hasShip()):
                            clickedTile.getShip().hit()
                            #circle(surface, color, center, radius)
                            pygame.draw.circle(screenDisp, RED, (mouseClick[0], mouseClick[1]), 1)
                        else:
                            pygame.draw.rect(screenDisp, RED, (mouseClick[0], mouseClick[1], 10,10), 1)
                        clickedTile.hit()
                        turnCounter += 1
                except:
                    pass
            #if event.type ==
            #    pygame.display.toggle_fullscreen() 
            #elif event.type == pygame.MOUSEBUTTONDOWN:
            #    if


                
        pygame.display.update()




screen = game_setup()
#screen = game_setup(vidInfo.current_w, vidInfo.current_h)
game_start(screen)
