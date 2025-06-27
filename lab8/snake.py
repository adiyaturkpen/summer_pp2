import pygame
import time
from random import randrange

# Инициализация всех модулей pygame
pygame.init()

# Настройки окна игры
size = 600  # Размер игрового окна: 600x600 пикселей
block = 30  # Размер одного блока змейки и еды
screen = pygame.display.set_mode((size, size))  # Создание окна
pygame.display.set_caption("Змейка")  # Название окна

# Определение цветов (в формате RGB)
green = (0, 150, 0)          # Цвет фона (зелёный)
snake_color = (255, 137, 0)  # Цвет тела змейки
head_color = (255, 247, 0)   # Цвет головы змейки
food_color = (255, 0, 0)     # Цвет еды (красный)
white = (255, 255, 255)      # Белый цвет (фон для экрана конца игры)
red = (255, 0, 0)            # Красный цвет (текст Game Over)

# Шрифты для текста на экране
font = pygame.font.SysFont("Verdana", 60)       # Крупный шрифт для Game Over / Next Level
font_small = pygame.font.SysFont("Verdana", 20) # Маленький шрифт для счёта и уровня

# Начальные координаты головы змейки (рандомные)
x = randrange(0, size, block)
y = randrange(0, size, block)

# Список, представляющий змейку (сначала только голова)
snake = [(x, y)]

# Направление движения (dx, dy) — 0 означает, что змейка стоит
dx, dy = 0, 0

# Словарь, ограничивающий возможность поворота назад (например, нельзя сразу пойти влево после движения вправо)
dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}

# Длина змейки, текущий счёт и уровень
length = 1
score = 0
level = 1

# Начальная скорость змейки (кадров в секунду)
fps = 10

# Координаты яблока (рандомно)
apple = randrange(0, size, block), randrange(0, size, block)

# Переменная для управления основным игровым циклом
running = True

# Создаём объект для управления частотой обновлений экрана
clock = pygame.time.Clock()

# Главный игровой цикл
while running:
    # Заливка фона однотонным зелёным цветом
    screen.fill(green)

    # Обработка всех событий (например, нажатия клавиш, закрытие окна)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Завершаем игру, если нажали "крестик" окна

        # Обработка нажатий клавиш стрелок для управления направлением змейки
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

    # Обновляем координаты головы змейки
    x += dx * block
    y += dy * block

    # Добавляем новое положение головы в список змейки
    snake.append((x, y))

    # Обрезаем хвост, чтобы длина оставалась постоянной (если не съели яблоко)
    snake = snake[-length:]

    # Отрисовка всей змейки
    for segment in snake[:-1]:
        pygame.draw.rect(screen, snake_color, (segment[0], segment[1], block, block))  # Тело
    pygame.draw.rect(screen, head_color, (snake[-1][0], snake[-1][1], block, block))    # Голова

    # Отрисовка яблока
    pygame.draw.rect(screen, food_color, (*apple, block, block))

    # Отображение текущего уровня и счёта
    level_text = font_small.render(f"Level: {level}", True, white)
    score_text = font_small.render(f"Score: {score}", True, white)
    screen.blit(level_text, (10, 10))
    screen.blit(score_text, (150, 10))

    # Проверка, съела ли змейка яблоко
    if snake[-1] == apple:
        score += 1         # Увеличиваем счёт
        length += 1        # Увеличиваем длину змейки
        apple = randrange(0, size, block), randrange(0, size, block)  # Новое яблоко

        # Если длина змейки кратна 5, поднимаем уровень и увеличиваем скорость
        if (length - 1) % 5 == 0:
            level += 1
            fps += 1
            # Показываем надпись "Next level"
            screen.fill(white)
            next_level = font.render("Next level", True, (0, 0, 0))
            screen.blit(next_level, (size // 2 - 150, size // 2 - 30))
            pygame.display.update()
            time.sleep(2)

    # Проверка: врезалась ли змейка в саму себя
    if len(snake) != len(set(snake)):
        screen.fill(white)
        game_over = font.render("Game Over", True, red)
        screen.blit(game_over, (size // 2 - 150, size // 2 - 30))
        pygame.display.update()
        time.sleep(2)
        running = False  # Завершаем игру

    # Проверка: врезалась ли змейка в стену
    if x < 0 or x >= size or y < 0 or y >= size:
        screen.fill(white)
        game_over = font.render("Game Over", True, red)
        screen.blit(game_over, (size // 2 - 150, size // 2 - 30))
        pygame.display.update()
        time.sleep(2)
        running = False  # Завершаем игру

    # Обновляем экран
    pygame.display.update()

    # Ограничиваем FPS (скорость движения)
    clock.tick(fps)

# Завершаем работу pygame
pygame.quit()
