import pygame
import random
from Shooter import Shooter
from bullet import Bullet
bullets = pygame.sprite.Group()

            
def game():
    win_height = 600
    win_width = 800
    win = pygame.display.set_mode(size=(win_width,win_height))
    bg = pygame.image.load('./assets/background.png')
    #size of each object
    s = 50
    
    #create shooter object
    player = Shooter((win_width//2,win_height-30),(s,s))
    run = True
    def fire_bullet():  
            bulletOb = Bullet('player',player.rect.center)
            bullets.add(bulletOb)
            print(len(bullets))
            
    clock = pygame.time.Clock()
    #main game loop
    while run:
        keys = pygame.key.get_pressed()
        
        win.blit(bg,(0,0))
        win.blit(player.surf, player.rect)
        for bulletOb in bullets:
             win.blit(bulletOb.surf,bulletOb.rect)
             bulletOb.move()

        #close win on Quit button click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        player.move()
        player.boundary()
        if keys[pygame.K_SPACE]:
            if random.randint(1,10) == 1:
                fire_bullet()

        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)

game()