import pygame         # Библиотека для создания игр
import time           # Для использования пауз (например, между уровнями)
import psycopg2       # Библиотека для работы с PostgreSQL
from random import randrange, choice  # Для генерации случайных координат и значений еды

# === НАСТРОЙКА ПОДКЛЮЧЕНИЯ К БАЗЕ ДАННЫХ ===
conn = psycopg2.connect(
    host="localhost",          # Сервер базы данных
    database="phonebook",      # Название базы
    user="postgres",           # Имя пользователя PostgreSQL
    password="21062007",       # Пароль
    port=5432                  # Порт подключения
)
cur = conn.cursor()            # Создаем курсор для выполнения SQL-запросов

# === РАБОТА С ПОЛЬЗОВАТЕЛЕМ ===
username = input("Введите имя пользователя: ")  # Запрашиваем имя игрока

# Проверка — есть ли уже такой пользователь в таблице users
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    # Если пользователь найден, загружаем его score и level
    user_id = user[0]
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    if result:
        score, level = result
        print(f"Добро пожаловать, {username}! Текущий уровень: {level}, очки: {score}")
    else:
        # Если запись о score отсутствует — создаём её
        score, level = 0, 1
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
        conn.commit()
else:
    # Если пользователь не найден — создаём нового
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    score, level = 0, 1
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    print(f"Пользователь {username} создан!")

# === НАСТРОЙКА ИГРЫ ===
pygame.init()                          # Инициализация Pygame
size = 600                             # Размер окна: 600x600 пикселей
block = 30                             # Размер одной клетки (змейки и еды)
screen = pygame.display.set_mode((size, size))  # Создаем окно
pygame.display.set_caption("Змейка")   # Заголовок окна

# Цвета
green = (0, 150, 0)        # Цвет фона
snake_color = (255, 137, 0)  # Цвет тела змейки
head_color = (255, 247, 0)   # Цвет головы змейки
food_color = (255, 0, 0)     # Цвет еды
white = (255, 255, 255)      # Белый цвет (например, для Game Over)
red = (255, 0, 0)            # Красный цвет (текст Game Over)

# Шрифты
font = pygame.font.SysFont("Verdana", 60)       # Крупный шрифт
font_small = pygame.font.SysFont("Verdana", 20) # Маленький шрифт

# Начальное положение змейки — случайное
x = randrange(0, size, block)
y = randrange(0, size, block)
snake = [(x, y)]          # Список координат всех блоков змейки
dx, dy = 0, 0             # Направление движения (0 = не двигается)
dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}  # Система для ограничения разворота назад

length = 1                # Начальная длина змейки
fps = 5 + level           # Скорость зависит от уровня (увеличивается)

# Функция генерации новой еды
def new_food():
    pos = randrange(0, size, block), randrange(0, size, block)  # Случайная позиция
    value = choice([1, 2, 3])              # Значение еды (очки и рост)
    timer = pygame.time.get_ticks()       # Время появления
    return {'pos': pos, 'value': value, 'spawn_time': timer}

food = new_food()        # Первая еда
running = True
clock = pygame.time.Clock()

# === ГЛАВНЫЙ ИГРОВОЙ ЦИКЛ ===
while running:
    screen.fill(green)   # Заливаем экран фоном

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Выход из игры

        if event.type == pygame.KEYDOWN:
            # Управление змейкой
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
            elif event.key == pygame.K_p:
                # Пауза: сохраняем текущие очки и уровень в БД
                cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
                conn.commit()
                print(f"Игра сохранена: Уровень {level}, Очки {score}")

    # Обновление позиции головы змейки
    x += dx * block
    y += dy * block
    snake.append((x, y))            # Добавляем новую голову
    snake = snake[-length:]         # Отрезаем хвост, если не увеличивалась

    # Отрисовка змейки
    for s in snake[:-1]:
        pygame.draw.rect(screen, snake_color, (s[0], s[1], block, block))  # Тело
    pygame.draw.rect(screen, head_color, (snake[-1][0], snake[-1][1], block, block))  # Голова

    # Отрисовка еды
    pygame.draw.rect(screen, food_color, (*food['pos'], block, block))  # Квадратик еды
    screen.blit(font_small.render(str(food['value']), True, white), (food['pos'][0]+5, food['pos'][1]+5))  # Число на еде

    # Если еда слишком старая (больше 5 секунд) — обновляем
    if pygame.time.get_ticks() - food['spawn_time'] > 5000:
        food = new_food()

    # Вывод уровня и очков
    screen.blit(font_small.render(f"Level: {level}", True, white), (10, 10))
    screen.blit(font_small.render(f"Score: {score}", True, white), (150, 10))

    # Проверка: съела ли змейка еду
    if snake[-1] == food['pos']:
        score += food['value']       # Добавляем очки
        length += food['value']      # Увеличиваем длину
        if (length - 1) % 5 == 0:    # Каждые 5 очков длины — новый уровень
            level += 1
            fps += 1                 # Увеличиваем скорость
            screen.fill(white)
            screen.blit(font.render("Next level", True, (0, 0, 0)), (size // 2 - 150, size // 2 - 30))
            pygame.display.update()
            time.sleep(2)
        food = new_food()

    # Проверка: врезалась ли змейка в себя или в стену
    if len(snake) != len(set(snake)) or x < 0 or x >= size or y < 0 or y >= size:
        screen.fill(white)
        screen.blit(font.render("Game Over", True, red), (size // 2 - 150, size // 2 - 30))
        pygame.display.update()
        time.sleep(2)
        running = False

    pygame.display.update()   # Обновление экрана
    clock.tick(fps)           # Управление частотой кадров (скоростью)

# === СОХРАНЕНИЕ ДАННЫХ ПРИ ВЫХОДЕ ===
cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
conn.commit()

# Закрытие соединения
cur.close()
conn.close()
pygame.quit()
