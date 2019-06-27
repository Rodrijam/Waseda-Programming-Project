import pygame

class Ship():
    def __init__(self, shipType):
        self.type = shipType
        self.location = None
        
    def getImg(self, w,h):

        shipImg = pygame.image.load(f'{self.type}.png')
        shipImg = pygame.transform.scale(shipImg, (round((4*w)/50), round((4*h)/50)))
        #shipImg = pygame.transform.scale(shipImg, ((4*w)/50, (4*h)/50))
        return shipImg

    def place(self, cellX, cellY, display):
        w, h = pygame.display.get_surface().get_size()
        #print(f"X: {round(w/10)*cellX} Y: {round(h/10)*cellY}")
        #cell = (round(w/10)*cellX, round(h/10)*cellY)
        cell = (round(w/10)+((cellX-1)*(round((4*w)/50))), round(h/10)+((cellY-1)*(round((4*h)/50))))
        self.location = cell
        display.blit(self.getImg(w,h), self.location)
        return

    def shipHit(self):
        pass

    def shipSink(self):
        pass

    
