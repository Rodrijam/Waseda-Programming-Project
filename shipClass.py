import pygame

class Ship:
    
    def __init__(self, size, img):
        self.alive = True
        self.size = size
        self.imgNum = img

    def __str__(self):
        return "Ship with " + str(self.size) + " parts remaining."

    def isAlive(self):
        return (self.size > 0)

    def getSize(self):
        return self.size
    
    def hit(self):
        self.size -= 1

    def getImgNum(self):
        return self.imgNum
