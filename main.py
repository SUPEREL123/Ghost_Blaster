import pygame
import random
import sys


pygame.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

fps = 60

score = 0
level = 0
speed_limiter = 10

screen_width = 800
screen_height = 600


prize_image = pygame.image.load("prize.jpg") 
prize_image = pygame.transform.scale(prize_image, (75, 75))
prize_width = 25
prize_height = 25
prize_timer = 0
prize_spawn_time = 10000
prizes = [] 

ghost_image = pygame.image.load("ghost.jpg") 
ghost_image = pygame.transform.scale(ghost_image, (75, 75))

enemy_width = 50
enemy_height = 60
enemy_speed = 2
enemies = []

enemy_timer = 0
enemy_spawn_time = 2000

rock_timer = 0
rock_spawn_time = 9000


enemy_timer = 0
# enemy_spawn_time = 5000

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Space Shooter")
clock = pygame.time.Clock()

player_image = pygame.image.load("player.jpg") 
player_image = pygame.transform.scale(player_image, (75, 75))
player_width = 50
player_height = 60
player_x = screen_width//2 - player_width//2
player_y = screen_height - player_height-10
player_speed = 5


rock_image = pygame.image.load("rock.jpg")
rock_image = pygame.transform.scale(rock_image, (100, 100))
rock_width = 100
rock_height = 100
rock_speed = 10
rocks = []


bullet_image = pygame.image.load("bullet.jpg")
bullet_image = pygame.transform.scale(bullet_image, (40, 25))
rotated_bullet_image = pygame.transform.rotate(bullet_image, 90)
bullet_width = 5
bullet_height = 10
bullet_speed = 7
bullets = []



def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_width//2 - bullet_width//2
                bullet_y = player_y
                bullets.append(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height))




    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < screen_height - player_height:
        player_y += player_speed


    for bullet in bullets:
        bullet.y -= bullet_speed

    bullets = [bullet for bullet in bullets if bullet.y > 0]




    screen.fill(black)

    current_time = pygame.time.get_ticks()
    if current_time - enemy_timer > enemy_spawn_time:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = -enemy_height
        enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height))
        enemy_timer = current_time

    current_time = pygame.time.get_ticks()
    if current_time - rock_timer > rock_spawn_time:
        rock_x = random.randint(0, screen_width - enemy_width)
        rock_y = -rock_height
        rocks.append(pygame.Rect(rock_x, rock_y, rock_width, rock_height))
        rock_timer = current_time

    current_time = pygame.time.get_ticks()
    if current_time - prize_timer > prize_spawn_time:
        prize_x = random.randint(0, screen_width - prize_width)
        prize_y = random.randint(0, screen_height - prize_height)
        if len(prizes) == 0 :
            prizes.append(pygame.Rect(prize_x, prize_y, prize_width, prize_height))


    for enemy in enemies:
        enemy.y += enemy_speed

    for rock in rocks:
        rock.y += rock_speed

    for bullet in bullets:
        for enemy in enemies:
            if check_collision(bullet, enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score = score + 1
                break    



    enemies = [enemy for enemy in enemies if enemy.y < screen_height]
    rocks = [rock for rock in rocks if rock.y < screen_height]

    player_obj = screen.blit(player_image, (player_x, player_y))
    # player_obj = pygame.draw.rect(screen, (0,128,255), (player_x, player_y, player_width, player_height))

    text_surface = my_font.render(f'Score: {score}| Level: {level}', False, white)
    screen.blit(text_surface, (0,0))
    
    for enemy in enemies:
        if check_collision(player_obj, enemy):
            pygame.quit()
            sys.exit()

    for rock in rocks:
        if check_collision(player_obj, rock):
            pygame.quit()
            sys.exit()


    for prize in prizes:
        if check_collision(prize, player_obj):
            score = score + 5
            if score // speed_limiter == 1:
                level = level + 1
                speed_limiter = speed_limiter + 10
            prizes.remove(prize)
        


    if score / speed_limiter == 1:
        level = int(score/10)
        enemy_speed = enemy_speed + level*7
        player_speed = player_speed + level
        speed_limiter = speed_limiter + 10
        


    for bullet in bullets:
        # pygame.draw .rect(screen, white, bullet)
        screen.blit(rotated_bullet_image, bullet.topleft)

    for enemy in enemies:
        #  pygame.draw.rect(screen, red, enemy)
        screen.blit(ghost_image, enemy.topleft)
    
    for rock in rocks:
        screen.blit(rock_image, rock.topleft)

    for prize in prizes:
        screen.blit(prize_image, prize.topleft)




    pygame.display.flip()

    clock.tick(fps)


# all init variables


# all keys pressing logic


# creating all objects


# drawing all objects


# checking scores