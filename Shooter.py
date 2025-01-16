import pygame
#Step 1: create shooter class 

from pygame.locals import (
    K_RIGHT,
    K_LEFT,
    K_SPACE,
    QUIT
)

class Shooter:
    #step 2: define constructor method to load image on surfance
    def __init__(self,pos,siz):
        self.surf = pygame.image.load('./assets/Shooter.png')
        self.surf = pygame.transform.scale(self.surf, siz)
        self.rect = self.surf.get_rect(center=(pos))
        self.speed = 5

    def fire_bullet(self):
        pass
    def boundary(self):
        if self.rect.x-20 < 0:
            self.rect.x += self.speed
        if self.rect.x+60 > 800:
            self.rect.x -= self.speed

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -=self.speed
        if keys[K_RIGHT]:
            self.rect.x +=self.speed
