import pygame
#Step 1: create shooter class 
class Shooter:
    #step 2: define constructor method to load image on surfance
    def __init__(self,pos,siz):
        self.surf = pygame.image.load('./assets/Shooter.png')
        self.surf = pygame.transform.scale(self.surf, siz)
        self.rect = self.surf.get_rect(center=(pos))
    def fire_bullet(self):
        pass
    def move(self):
        pass
