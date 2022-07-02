import fire as fire
import pygame
import random
import math
from pygame import mixer

# инициализируем модуль PyGame
pygame.init()

# создаём экран
screen = pygame.display.set_mode((800, 600))

# фоновый рисунок
background = pygame.image.load('background.png')

#фоновая музыка
mixer.music.load('background.wav')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

# название окна и иконка
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# игрок
playerImg = pygame.image.load('ship.png')
playerX = 370
playerY = 480
playerX_change = 0

# противник
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# пуля
# ready = мы не можем видеть пулю на экране
# fire - пуля сейчас на экране
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

#score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = font.render('GAME OVER', True, (255,255,255))
    screen.blit(over_text, (200, 250))

def show_Score(x,y):
    score = font.render('Score : '+ str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 28:
        return True
    else:
        return False


#создаём игровой цикл
running = True
while running:
    # цвета в пигейме работают в цветовом диапазоне ргб
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # если нажата какая-нибудь клавиша - надо проверить, нажата правая или левая
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    playerX += playerX_change
    # границы игры
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # границы игры
    for i in range(num_of_enemies):

        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    # движение пули
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

#столкновения


player(playerX, playerY)
show_Score(textX, textY)
pygame.display.update()