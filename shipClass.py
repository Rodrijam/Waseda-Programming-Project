import pygame

class Ship():
    
    def __init__(self, size):
        self.isAlive = True
        self.size = size

    def __str__(self):
        return "Ship with: " + str(len(self.parts)) + " parts."

    def isFullyAlive(self):
        return (size > 0)
    
    def hit(self):
        self.size -= 1
