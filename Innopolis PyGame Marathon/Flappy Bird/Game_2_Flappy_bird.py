import pygame, sys, random

# функции для труб
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    new_pipe = pipe_surface.get_rect(midtop = (350, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (350, random_pipe_pos - 150))
    return new_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3,1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect

# функция для отрисовки пола
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos + 288, 450))

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(f'Score: {int(score)}', True, (225,225,225))
        score_rect = score_surface.get_rect(center = (140, 50))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(str(int(score)), True, (225, 225, 225))
        score_rect = score_surface.get_rect(center=(140, 50))
        screen.blit(score_surface, score_rect)

        height_score_surface = game_font.render(f'Height Score: {height_score}', True, (225, 225, 225))
        height_score_rect = score_surface.get_rect(center = (1, 425))
        screen.blit(height_score_surface, height_score_rect)

def score_updaite(score, height_score):
    if score > height_score:
        height_score = score
    return height_score


pygame.init() 
# если окно слишком большое - дробите надвое
screen = pygame.display.set_mode((288, 512))
# 576, 1024 делайте 288, 512
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.TTF', 40)

# игровые переменные
gravity = 0.16
bird_movement = 0
game_active = True
score = 0
height_score = 0

#сначала сделаем фоновую поверхность
bg_surface = pygame.image.load('assets/background-day.png').convert() #если картинка маловата - делайте следующий шаг
# не делайте, если все ок с самого начала, если картинка в 0,0

# переменные земли
floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_pos = 0

# переменные птицы
bird_downflap = pygame.image.load('assets/yellowbird-downflap.png').convert_alpha()
bird_midflap = pygame.image.load('assets/yellowbird-midflap.png').convert_alpha()
bird_upflap = pygame.image.load('assets/yellowbird-upflap.png').convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100, 512))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
# bird_rect = bird_surface.get_rect(center = (100, 512))

# переменные + события труб
pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1350)
pipe_height = [200, 300, 400]

# игровой цикл
while True:
    # обработчик событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 5.5
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 512)
                bird_movement = 0
                score = 0
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        if event.type == BIRDFLAP:
            if bird_index <  2:
                bird_index += 1
            else:
                bird_index = 0
            bird_surface, bird_rect = bird_animation()

    # фоновый рисунок
    screen.blit(bg_surface, (0, 0))

    if game_active:

        # птица
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # трубы
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score += 0.01
        score_display('main_game')
    else:
        height_score = score_updaite(score, height_score)
        score_display('game_over')

    # земля + движение земли
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -288:
        floor_x_pos = 0


    pygame.display.update()
    clock.tick(120)
