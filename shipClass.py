import pygame

class Ship:
    
    def __init__(self, size):
        self.isAlive = True
        self.size = size

    def __str__(self):
        return "Ship with " + str(self.size) + " parts"

    def isFullyAlive(self):
        return (selfsize > 0)

    def getSize(self):
        return self.size
    
    def hit(self):
        self.size -= 1
