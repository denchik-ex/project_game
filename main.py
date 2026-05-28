import pygame
  
pygame.init()
screen = pygame.display.set_mode((626,351))
pygame.display.set_caption("LOLgame 2026")
icon = pygame.image.load('images\icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('images/background1.png')
player = pygame.image.load('images/player_right.png')
player = pygame.transform.scale(player, (60, 60))

running = True
while running:

    screen.blit(background, (0,0))
    screen.blit(player, (100,225))
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()



