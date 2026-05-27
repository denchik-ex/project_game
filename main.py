import pygame
  
pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("LOLgame 2026")
icon = pygame.image.load('images\icon.png')
pygame.display.set_icon(icon)

running = True
while running:

    
    
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_9:
                screen.fill((168,134,207))
            if event.key == pygame.K_8:
                screen.fill((207,134,185))
            if event.key == pygame.K_7:
                screen.fill((196,75,84))