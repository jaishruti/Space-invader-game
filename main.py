import pygame
import random
from Shooter import Shooter
from bullet import Bullet
from alien import Alien
bullets = pygame.sprite.Group()
aliens = pygame.sprite.Group()

def alien_setup(rows,cols,x_distance = 60,y_distance = 48,x_offset = 70, y_offset = 100):   
            for row_index, row in enumerate(range(rows)):
                for col_index, col in enumerate(range(cols)):
                    x = col_index * x_distance + x_offset
                    y = row_index * y_distance + y_offset
                    
                    if row_index == 0: alien_sprite = Alien('Alien1',x,y)
                    elif 1 <= row_index <= 2: alien_sprite = Alien('Alien2',x,y)
                    else: alien_sprite = Alien('bug',x,y)
                    aliens.add(alien_sprite)
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
    alien_setup(rows=6, cols=8)
    clock = pygame.time.Clock()
    #main game loop
    while run:
        keys = pygame.key.get_pressed()
        
        win.blit(bg,(0,0))
        win.blit(player.surf, player.rect)

        #appear bullet
        for bulletOb in bullets:
             win.blit(bulletOb.surf,bulletOb.rect)
             bulletOb.move()

        #move aliens
        for alien in aliens:
            win.blit(alien.surf,alien.rect)
            alien.update()
        
        #when bullet hits alien -> kill alien and bullet
        if bullets:
             for bullet in bullets:
                  aliens_hit = pygame.sprite.spritecollide(bullet,aliens,True)
                  if aliens_hit:
                         for alien in aliens_hit:
                              bullet.kill()

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