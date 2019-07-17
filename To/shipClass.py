import pygame
from tileClass import *

class Ship():
    
    def __init__(self, parts):
        self.isAlive = True
        self.parts = parts

    def __str__(self):
        return "Ship with: " + str(len(self.parts)) + " parts."

    def isFullyAlive(self):
        isAliveTemp = True
        for part in self.parts:
            if not part.isAlive():
                isAliveTemp = False
                break
        self.isAlive = isAliveTemp
        return isAlive

    
class ShipPart:

    def __init__(self, partImg = "sprites/shipHB"):
        self.isAlive = True
        self.img = partImg

    def Hit():
        self.isAlive = False

    def getImg(self, w,h):
        shipImg = pygame.image.load(f'{self.img}.png')
        shipImg = pygame.transform.scale(shipImg, (round((4*w)/50), round((4*h)/50)))
        return shipImg

    def place(self, tile, display):
        w, h = pygame.display.get_surface().get_size()
        cell = (round(w/10)+((tile.getRow()-1)*(round((4*w)/50))), round(h/10)+((tile.getCol()-1)*(round((4*h)/50))))
        display.blit(self.getImg(w,h), cell)
        return
