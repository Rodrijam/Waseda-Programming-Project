import pygame
from pygame.locals import *
from shipClass import *

pygame.init()

#Color & Image Definitions
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

#ship1Img = pygame.image.load('ship1.png')
placeLocation = (0,0)

def game_setup(screenWidth = 1200, screenHeight = 675):
    
    #Display Setup
    screenDisp = pygame.display.set_mode((screenWidth,screenHeight))
    pygame.display.set_caption("Basic Battleship")


    #Buffer Cells
    cellWidth = round(screenWidth/10)
    cellHeight = round(screenHeight/10)

    #True Cells
    innerWidth = screenWidth - (2*cellWidth)
    innerHeight = screenHeight - (2*cellHeight)
    innerCellWidth = round(innerWidth/10)
    innerCellHeight = round(innerHeight/10)

    #Display Modification
    screenDisp.fill(WHITE)
    waterImg = pygame.image.load('sprites/watertile.jpg')
    waterImg = pygame.transform.scale(waterImg, (innerCellWidth, innerCellHeight))
    
    #Water Image Display
    for i in range (10):
        for j in range(10):
            screenDisp.blit(waterImg, (cellWidth + (i*innerCellWidth), cellHeight + (j*innerCellHeight)))

    #Drawing the Grid with rectangles
    for i in range (10):
        for j in range(10):
            pygame.draw.rect(screenDisp, BLUE, (cellWidth + (i*innerCellWidth), cellHeight + (j*innerCellHeight), innerCellWidth, innerCellHeight), 1)
            pygame.draw.rect(screenDisp, BLACK, (cellWidth + (i*innerCellWidth), cellHeight - innerCellHeight , innerCellWidth, innerCellHeight), 1)
            pygame.draw.rect(screenDisp, BLACK, (cellWidth - innerCellWidth, cellHeight + (j*innerCellHeight) , innerCellWidth, innerCellHeight), 1)

    #Image Check
    imageSetPoint = (round(cellWidth), round(cellHeight))
    pygame.draw.circle(screenDisp, RED, (imageSetPoint), 10, 1)

    return screenDisp


def game_start(screenDisp):
    #Game Loop
    while True:
        #Need to modify ship object to have its own head/tail/body properties
        ship1Head = Ship("sprites/shipHL")
        ship1Tail = Ship("sprites/shipHR")

        ship2Head = Ship("sprites/shipVH")
        ship2Body = Ship("sprites/shipVB")
        ship2Tail = Ship("sprites/shipVT")

        ship3Head = Ship("sprites/shipVH")
        ship3Tail = Ship("sprites/shipVT")
        
        ship4Head = Ship("sprites/shipHL")
        ship4Body = Ship("sprites/shipHB")
        ship4Tail = Ship("sprites/shipHR")
        
        ship1Head.place(2,8,screenDisp)
        ship1Tail.place(3,8,screenDisp)

        ship2Head.place(1,1,screenDisp)
        ship2Body.place(1,2,screenDisp)
        ship2Tail.place(1,3,screenDisp)

        ship3Head.place(8,2,screenDisp)
        ship3Tail.place(8,3,screenDisp)
        
        ship4Head.place(5,5,screenDisp)
        ship4Body.place(6,5,screenDisp)
        ship4Tail.place(7,5,screenDisp)
        #ship1.place(placeLocation, screenDisp)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        pygame.display.update()





screen = game_setup()
game_start(screen)
