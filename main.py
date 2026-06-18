import pygame
  
pygame.init()
screen = pygame.display.set_mode((736,414))
pygame.display.set_caption("Охотник за привидениями")
clock = pygame.time.Clock()
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('images/background11.jpg')
bd_width = background.get_width() # ширина фона

player = pygame.image.load('images/player_right.png')
player = pygame.transform.scale(player, (60, 60))
player_left = pygame.transform.flip(player, True, False)

ghost = pygame.image.load('images/ghost.png')
ghost = pygame.transform.scale(ghost, (40, 40))
ghost_list = []

my_sound = pygame.mixer.Sound('sounds/melodia.mp3')
my_sound.play()
my_sound.set_volume(0.2)

win_sound = pygame.mixer.Sound('sounds/win.mp3') 
win_sound.set_volume(0.5)

walk_right = pygame.image.load('images/player_right1.png')
walk_right = pygame.transform.scale(walk_right, (60, 60))

walk_left = pygame.image.load('images/player_left1.png')
walk_left = pygame.transform.scale(walk_left, (60, 60))

player_x = 75
player_y = 310
speed = 1

is_jump = False
jump_count = 9

image = player

look_right = True
b_x = 0
auto_move = 3

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 1700)

shrift = pygame.font.Font('fonts/font_SolKol.ttf', 40)
lose_shrift = shrift.render('Вы проиграли!!!', False, (255,46,46))
win_shrift = shrift.render('Вы выиграли!!!', False, (0,255,0))
restart_shrift = shrift.render('Играть заново', False, (46,46,255))
restart_shrift_rect = restart_shrift.get_rect(topleft=(240,100))
screen_lose = pygame.image.load('images/lose.jpg')
screen_win = pygame.image.load('images/win.jpg')
small_shrift = pygame.font.Font('fonts/font_SolKol.ttf', 30)

start_game = False
start_screen = pygame.image.load('images/start_image.png')
startik = shrift.render('ИГРАТЬ', False, (255, 255, 255))
startik_rect = startik.get_rect(center=(368, 250))
title = shrift.render('ОХОТНИК ЗА ПРИВИДЕНИЯМИ', False, (255, 255, 0))
title_rect = title.get_rect(center=(368, 120))


bullet = pygame.image.load('images/bullet.png')
bullet = pygame.transform.scale(bullet, (25, 25))
bullets = []
bullets_gun = 10

max_ghosts = 20
ghost_spawned = 0
win_game = False

gameplay = True

running = True
while running:
    if not start_game:
        screen.blit(start_screen,(0,0))
        screen.blit(title, title_rect)
        screen.blit(startik, startik_rect)

        mouse = pygame.mouse.get_pos()
        if startik_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            start_game = True
    else:
        screen.blit(background,(b_x,0))
        screen.blit(background,(b_x + bd_width,0))
        screen.blit(background,(b_x - bd_width,0))
        clock.tick(30)

        if gameplay:
            player_rect = image.get_rect(topleft=(player_x, player_y))


            move_b = -auto_move
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
                screen.blit(shrift.render('Призраки ускоряются!', False, (255, 46, 46)), (180, 200))
            else:
                if look_right:
                    image = player
                else:
                    image = player_left
            
            
            if not is_jump:
                if keys[pygame.K_SPACE]:
                    is_jump = True
            else:
                if jump_count >= -9:
                    if jump_count > 0:
                        player_y -= (jump_count ** 2) / 2
                    else:
                        player_y += (jump_count ** 2) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 9

            b_x += move_b 

            if b_x <= -bd_width:
                b_x += bd_width
            if b_x >= bd_width:
                b_x -= bd_width
        
            if ghost_list:
                for element in ghost_list[:]:
                    screen.blit(ghost, element)
                    element.x -= 7

                    if element.x < -7:
                        ghost_list.remove(element)
                    
                    if player_rect.colliderect(element):
                        gameplay = False
                        win_game = False
            
            if not ghost_list and ghost_spawned >= max_ghosts and gameplay:
                win_game = True
                gameplay = False
                my_sound.stop()
                win_sound.play()
                
            screen.blit(image, (player_x, player_y))
            
            if bullets_gun <= 3:
                bullets_text = small_shrift.render(f'{bullets_gun}',False, (255,0,0))
            else:
                bullets_text = small_shrift.render(f'{bullets_gun}', False, (255,255,255))

            text_rect = bullets_text.get_rect(center=(player_x + 30, player_y -20))
            screen.blit(bullets_text, text_rect)

            if bullets:
                for (i,element) in enumerate(bullets):
                    screen.blit(bullet, (element.x, element.y))
                    element.x += 5

                    if element.x > 740:
                        bullets.pop(i)

                    if ghost_list:
                        for (index, ghost_element) in enumerate(ghost_list):
                            if element.colliderect(ghost_element):
                                ghost_list.pop(index)
                                bullets.pop(i)

        else:
            if win_game:
                screen.blit(screen_win,(0,0))
                screen.blit(win_shrift, (240,250))
                screen.blit(restart_shrift, restart_shrift_rect)
            else:
                screen.blit(screen_lose,(0,0))
                screen.blit(lose_shrift, (240,200))
                screen.blit(restart_shrift, restart_shrift_rect)

            mouse = pygame.mouse.get_pos()
            if restart_shrift_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                gameplay = True
                win_game = False
                player_x = 75
                ghost_list.clear()
                bullets.clear()
                bullets_gun = 10
                ghost_spawned = 0
                my_sound.play()

    pygame.display.update()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if start_game and event.type == ghost_timer:
                if ghost_spawned < max_ghosts:
                    ghost_list.append(ghost.get_rect(topleft=(738,310)))
                    ghost_spawned += 1
                else:
                    if not ghost_list:
                        win_game = True
                        gameplay = False
            if start_game and gameplay and event.type == pygame.KEYUP and event.key == pygame.K_g and bullets_gun > 0:
                bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
                bullets_gun -= 1




