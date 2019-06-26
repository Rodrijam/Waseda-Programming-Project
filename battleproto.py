import pygame, sys
from pygame.locals import *

pygame.init()

screenWidth = 1200
screenHeight = 675
#Display Setup
screenDisp = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Basic Battleship")

#Color & Image Definitions
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
ship1Img = pygame.image.load('ship1.png')
ship1x = 10
ship1y = 10

cellWidth = round(screenWidth/10)
cellHeight = round(screenHeight/10)
innerWidth = screenWidth - (2*cellWidth)
innerHeight = screenHeight - (2*cellHeight)
innerCellWidth = round(innerWidth/10)
innerCellHeight = round(innerHeight/10)

#Display Modification
screenDisp.fill(WHITE)
ship1Img = pygame.transform.scale(ship1Img, (100, 25))

"""
pygame.draw.circle(screenDisp, RED, (cellWidth, cellHeight), 20, 1)
pygame.draw.circle(screenDisp, RED, (innerWidth, innerHeight ), 20, 1)
pygame.draw.circle(screenDisp, RED, (innerCellWidth  + cellWidth, innerCellHeight+ cellHeight), 20, 1)
pygame.draw.rect(screenDisp, BLUE, (cellWidth, cellHeight, innerCellWidth, innerCellHeight), 1)
"""

for i in range (10):
    for j in range(10):
        pygame.draw.rect(screenDisp, BLUE, (cellWidth + (i*innerCellWidth), cellHeight + (j*innerCellHeight), innerCellWidth, innerCellHeight), 1)

"""
for i in range (9):
    #pygame.draw.line(screenDisp, BLACK, (cellWidth + (i*cellWidth), 0),(cellWidth + (i*cellWidth), screenHeight), 1)
    #pygame.draw.line(screenDisp, BLACK, (0, cellHeight + (i*cellHeight)),(screenWidth, cellHeight + (i*cellHeight)), 1)
    pygame.draw.rect(screenDisp, BLUE, (cellWidth, cellHeight, cellWidth * 8, cellHeight * 8), 1)
    pygame.draw.line(screenDisp, GREEN, ((2 * innerCellWidth) + (i * innerCellWidth) , cellHeight),(innerCellWidth + innerCellWidth + (innerCellWidth * i), cellHeight*9), 1)
    #pygame.draw.line(screenDisp, GREEN, (cellWidth, innerCellHeight + innerCellHeight),(cellWidth*9, innerCellHeight + innerCellHeight), 1)

"""

#Game Loop
while True:
    
    

    screenDisp.blit(ship1Img, (ship1x, ship1y))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.quit()
    pygame.display.update()
