import pygame
  
pygame.init()
screen = pygame.display.set_mode((736,414))
pygame.display.set_caption("LOLgame 2026")
clock = pygame.time.Clock()
icon = pygame.image.load('images\icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('images/background11.jpg')
player = pygame.image.load('images/player_right.png')
player = pygame.transform.scale(player, (60, 60))
walk_right = pygame.image.load('images/player_right1.png')
walk_right = pygame.transform.scale(walk_right, (60, 60))
walk_left = pygame.image.load('images/player_left.png')
walk_left = pygame.transform.scale(walk_left, (60, 60))

player_x = 75
player_y = 310
speed = 1
image = player

b_x = 0

running = True
while running:
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    move_b = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player_x += speed
        image = walk_right
        move_b = -5
    elif keys[pygame.K_LEFT]:
        player_x -= speed
        image = walk_left
        move_b = 5
    else:
        image = player
    
    b_x += move_b

    if b_x <= -736:
        b_x = 0
    if b_x >= 736:
        b_x = 0

    screen.blit(background,(b_x,0))
    screen.blit(background,(b_x + 736,0))
    screen.blit(image, (player_x,player_y))


    pygame.display.update()
pygame.quit()        



