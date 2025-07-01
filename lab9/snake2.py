import pygame
import time
from random import randrange, choice

# Инициализация всех модулей Pygame
pygame.init()

# Параметры окна
size = 600           # Ширина и высота окна (600x600 пикселей)
block = 30           # Размер одной клетки (для змейки и еды)
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Змейка")

# Цвета (в формате RGB)
green = (0, 150, 0)          # Цвет фона (зелёный)
snake_color = (255, 137, 0)  # Цвет тела змейки (оранжевый)
head_color = (255, 247, 0)   # Цвет головы змейки (жёлтый)
food_color = (255, 0, 0)     # Цвет еды (красный)
white = (255, 255, 255)      # Белый (для надписей и Game Over)
red = (255, 0, 0)            # Красный (текст Game Over)

# Шрифты
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# Начальные координаты змейки (головы)
x = randrange(0, size, block)
y = randrange(0, size, block)
snake = [(x, y)]  # Список сегментов змейки

# Направление движения (dx, dy) — начально змейка стоит
dx, dy = 0, 0

# Разрешённые направления — чтобы змейка не могла повернуть назад сразу
dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}

# Длина змейки, очки, уровень, скорость
length = 1
score = 0
level = 1
fps = 10  # Скорость (кадров в секунду)

# --- ФУНКЦИЯ ДЛЯ СОЗДАНИЯ НОВОЙ ЕДЫ С ВЕСОМ И ВРЕМЕНЕМ ---
def new_food():
    pos = randrange(0, size, block), randrange(0, size, block)  # Случайная позиция
    value = choice([1, 2, 3])  # Случайный "вес" еды (сколько очков/длины даёт)
    timer = pygame.time.get_ticks()  # Время появления еды (в миллисекундах)
    return {'pos': pos, 'value': value, 'spawn_time': timer}

# Создаём первое яблоко
food = new_food()

# Основной цикл игры
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(green)  # Закрашиваем фон зелёным

    # Обработка событий (клавиши, выход)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Изменение направления движения при нажатии стрелок
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dirs['UP']:
                dx, dy = 0, -1
                dirs = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}
            elif event.key == pygame.K_DOWN and dirs['DOWN']:
                dx, dy = 0, 1
                dirs = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
            elif event.key == pygame.K_LEFT and dirs['LEFT']:
                dx, dy = -1, 0
                dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}
            elif event.key == pygame.K_RIGHT and dirs['RIGHT']:
                dx, dy = 1, 0
                dirs = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}

    # Обновляем позицию головы змейки
    x += dx * block
    y += dy * block
    snake.append((x, y))         # Добавляем новую голову
    snake = snake[-length:]      # Удаляем лишние сегменты, если не ели еду

    # Отрисовка тела змейки
    for segment in snake[:-1]:
        pygame.draw.rect(screen, snake_color, (segment[0], segment[1], block, block))
    # Отрисовка головы змейки
    pygame.draw.rect(screen, head_color, (snake[-1][0], snake[-1][1], block, block))

    # Отрисовка еды
    pygame.draw.rect(screen, food_color, (*food['pos'], block, block))
    # Отображение "веса" еды — число от 1 до 3
    food_label = font_small.render(str(food['value']), True, white)
    screen.blit(food_label, (food['pos'][0] + 5, food['pos'][1] + 5))

    # Проверка: прошло ли больше 5 секунд с момента появления еды
    if pygame.time.get_ticks() - food['spawn_time'] > 5000:
        food = new_food()  # Если да — создаём новую еду

    # Отображение текущего уровня и очков
    level_text = font_small.render(f"Level: {level}", True, white)
    score_text = font_small.render(f"Score: {score}", True, white)
    screen.blit(level_text, (10, 10))
    screen.blit(score_text, (150, 10))

    # Проверка: съела ли змейка еду
    if snake[-1] == food['pos']:
        score += food['value']      # Прибавляем очки
        length += food['value']     # Увеличиваем длину
        # Повышаем уровень и скорость каждые 5 очков длины
        if (length - 1) % 5 == 0:
            level += 1
            fps += 1
            # Показ "Next level"
            screen.fill(white)
            next_level = font.render("Next level", True, (0, 0, 0))
            screen.blit(next_level, (size // 2 - 150, size // 2 - 30))
            pygame.display.update()
            time.sleep(2)
        food = new_food()  # Создаём новую еду после поедания

    # Проверка: столкновение змейки с самой собой
    if len(snake) != len(set(snake)):
        screen.fill(white)
        game_over = font.render("Game Over", True, red)
        screen.blit(game_over, (size // 2 - 150, size // 2 - 30))
        pygame.display.update()
        time.sleep(2)
        running = False

    # Проверка: столкновение со стенами
    if x < 0 or x >= size or y < 0 or y >= size:
        screen.fill(white)
        game_over = font.render("Game Over", True, red)
        screen.blit(game_over, (size // 2 - 150, size // 2 - 30))
        pygame.display.update()
        time.sleep(2)
        running = False

    pygame.display.update()
    clock.tick(fps)  # Ограничение FPS (скорости игры)

pygame.quit()  # Завершение Pygame
