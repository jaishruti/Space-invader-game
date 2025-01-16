import pygame
from Shooter import Shooter

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

    #main game loop
    while run:
        win.blit(bg,(0,0))
        win.blit(player.surf, player.rect)

        #close win on Quit button click
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        player.move()
        pygame.display.flip()

game()