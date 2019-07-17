import pygame
from pygame.locals import *
from shipClass import *

pygame.init()

vidInfo = pygame.display.Info()

#Color & Image Definitions
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

placeLocation = (0,0)

gameTiles = []

clock = pygame.time.Clock()

def game_setup(screenWidth = 1200, screenHeight = 675):

    gameBoard = []
    
    #Display Setup
    screenDisp = pygame.display.set_mode((screenWidth,screenHeight), pygame.RESIZABLE)
    pygame.display.set_caption("Basic Battleship")


    #Buffer Cells
    cellWidth = round(screenWidth/10)
    cellHeight = round(screenHeight/10)

    #True Cells
    innerWidth = screenWidth - (2*cellWidth)
    innerHeight = screenHeight - (2*cellHeight)
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

    #Drawing the Grid with rectangles
    for i in range (10):
        rowSet = []
        for j in range(10):
            print(f"Making Col {j+1}")
            newTile = Tile(cellWidth + (i*innerCellWidth),cellHeight + (j*innerCellHeight),i+1,j+1)
            rowSet.append(newTile)

            #Main Grid  
            #pygame.draw.rect(screenDisp, BLUE, (cellWidth + (i*innerCellWidth), cellHeight + (j*innerCellHeight), innerCellWidth, innerCellHeight), 1)

            #Axis Labels
            pygame.draw.rect(screenDisp, BLACK, (cellWidth + (i*innerCellWidth), cellHeight - innerCellHeight , innerCellWidth, innerCellHeight), 1)
            pygame.draw.rect(screenDisp, BLACK, (cellWidth - innerCellWidth, cellHeight + (j*innerCellHeight) , innerCellWidth, innerCellHeight), 1)
        gameBoard.append(rowSet)
    
    for i in gameBoard:
        for j in i:
            pygame.draw.rect(screenDisp, RED, (j.getX(), j.getY(), innerCellWidth, innerCellHeight), 1)
            print (j)

    #Image Check
    imageSetPoint = (round(cellWidth), round(cellHeight))
    pygame.draw.circle(screenDisp, RED, (imageSetPoint), 10, 1)

            
            

    return screenDisp


def game_start(screenDisp):
    #Game Loop
    shipList = [Ship([ShipPart() for i in range(2)]),
                Ship([ShipPart() for i in range(3)]),
                Ship([ShipPart() for i in range(3)]),
                Ship([ShipPart() for i in range(4)]),
                Ship([ShipPart() for i in range(5)])]

    for ship in shipList:
        print(ship)
    
    #print(shipList)
    while True:
        
        #Need to modify ship object to have its own head/tail/body properties

        #Test image depiction for ships, needs ability to place ships or
        #drag them from a try onto the battlefield
        """
        ship1Head = ShipPart("sprites/shipHL")
        ship1Tail = ShipPart("sprites/shipHR")

        ship2Head = ShipPart("sprites/shipVH")
        ship2Body = ShipPart("sprites/shipVB")
        ship2Tail = ShipPart("sprites/shipVT")

        ship3Head = ShipPart("sprites/shipVH")
        ship3Tail = ShipPart("sprites/shipVT")
        
        ship4Head = ShipPart("sprites/shipHL")
        ship4Body = ShipPart("sprites/shipHB")
        ship4Tail = ShipPart("sprites/shipHR")
        
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
        """


        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            #elif event.type == VIDEORESIZE:
            #    game_setup(screenDisp.get_width(), screenDisp.get_height())
            elif event.type == MOUSEBUTTONDOWN:
                mouseClick = pygame.mouse.get_pos()
                pygame.draw.rect(screenDisp, BLACK, (mouseClick[0], mouseClick[1], 10,10), 1)
               
                
            #if event.type ==
            #    pygame.display.toggle_fullscreen() 
            #elif event.type == pygame.MOUSEBUTTONDOWN:
            #    if


                
        pygame.display.update()




screen = game_setup()
#screen = game_setup(vidInfo.current_w, vidInfo.current_h)
game_start(screen)
