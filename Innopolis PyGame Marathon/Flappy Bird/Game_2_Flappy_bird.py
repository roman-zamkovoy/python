import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos + 288, 450))

pygame.init()
# если окно слишком большое - дробите надвое
screen = pygame.display.set_mode((288, 512))
# 576, 1024 делайте 288, 512
clock = pygame.time.Clock()

# игровые переменные
gravity = 0.25
bird_movement = 0


#сначала сделаем фоновую поверхность
bg_surface = pygame.image.load('assets/background-day.png').convert() #если картинка маловата - делайте следующий шаг
 # не делайте, если все ок с самого начала, если картинка в 0,0

floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_pos = 0

bird_surface = pygame.image.load('assets/yellowbird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (50, 256))

while True:
    # обработчик событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               bird_movement -= 12

    screen.blit(bg_surface, (0, 0))
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0
    # изображение игрока 1
    # фоновый рисунок
    pygame.display.update()
    clock.tick(120)