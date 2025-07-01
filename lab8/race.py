# Импорт необходимых библиотек
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Настройка FPS (количество кадров в секунду)
FPS = 60
FramePerSec = pygame.time.Clock()

# Определение цветов
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Параметры экрана и переменные игры
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5            # Скорость врагов и монет
SCORE = 0            # Счёт за объезженные машины
COINS = 0            # Количество собранных монет

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Фон
background = pygame.image.load("lab8\\AnimatedStreet.png")
pygame.mixer.music.load("lab8\\background.wav") 
pygame.mixer.music.play(loops=-1)

# Создание игрового окна
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Класс врага (машины)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("lab8\\Enemy.png"), (48,93))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Метод для передвижения врага вниз
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        # Если враг выходит за нижнюю границу — начисляем очко и сбрасываем его вверх
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.transform.scale(pygame.image.load("lab8\\Player.png"), (50,96))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    # Метод для передвижения игрока влево и вправо
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("lab8\\coin.png"), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Метод для движения монеты вниз
    def move(self):
        self.rect.move_ip(0, SPEED)
        # Если монета выходит за нижнюю границу — сбрасываем её вверх
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Создание объектов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Событие для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Главный игровой цикл
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # Увеличиваем скорость каждую секунду
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Отображение фона
    DISPLAYSURF.blit(background, (0, 0))

    # Отображение счёта и количества монет
    score_text = font_small.render("Очки: " + str(SCORE), True, BLACK)
    coin_text = font_small.render("Монеты: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 110, 10))

    # Передвижение и отрисовка всех спрайтов
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Проверка столкновения игрока с врагом — конец игры
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('lab8\\crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Проверка сбора монеты
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += 1
        for coin in coins:
            coin.rect.top = 0
            coin.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    # Обновление экрана и ограничение FPS
    pygame.display.update()
    FramePerSec.tick(FPS)
