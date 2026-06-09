import pygame
  
pygame.init()
screen = pygame.display.set_mode((736,414))
pygame.display.set_caption("LOLgame 2026")
clock = pygame.time.Clock()
icon = pygame.image.load('images\icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('images/background11.jpg')
bd_width = background.get_width() # ширина фона

player = pygame.image.load('images/player_right.png')
player = pygame.transform.scale(player, (60, 60))
player_left = pygame.transform.flip(player, True, False)
walk_right = pygame.image.load('images/player_right1.png')
walk_right = pygame.transform.scale(walk_right, (60, 60))
walk_left = pygame.image.load('images/player_left1.png')
walk_left = pygame.transform.scale(walk_left, (60, 60))

player_x = 75
player_y = 310
speed = 1

is_jump = False
jump_count = 8

image = player

look_right = True
b_x = 0

running = True
while running:
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    move_b = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and player_x < 600:
        player_x += speed
        image = walk_right
        move_b = -5
        look_right = True
    elif keys[pygame.K_a] and player_x > 75:
        player_x -= speed
        image = walk_left
        move_b = 5
        look_right = False
    else:
        if look_right:
            image = player
        else:
            image = player_left
    
    
    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -8:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 8



    b_x += move_b

    if b_x <= -bd_width:
        b_x += bd_width
    if b_x >= bd_width:
        b_x -= bd_width

    screen.blit(background,(b_x,0))
    screen.blit(background,(b_x + bd_width,0))
    screen.blit(background,(b_x - bd_width,0))
    screen.blit(image, (player_x,player_y))


    pygame.display.update()
pygame.quit()

# подумать, хорошая ли идея со самостоятельным движением, ну и сделать прыжок и врагов



