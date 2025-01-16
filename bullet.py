import pygame

#define Bullet class - to add image in constructor, kill the bullet when goes beyond boundary, add movement
class Bullet(pygame.sprite.Sprite):
    def __init__(self,choice,pos):
        super().__init__()
        img_path = './assets/'+choice+'Bullet.png'
        print(img_path)
        self.surf = pygame.image.load(img_path)
        self.surf = pygame.transform.scale(self.surf,(10,30))
        self.rect = self.surf.get_rect(center=(pos))
    
    def move(self):
        self.rect.move_ip(0,-10)