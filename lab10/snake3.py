import pygame
import time
import psycopg2
from random import randrange, choice

# === DB SETUP ===
conn = psycopg2.connect(
    host="localhost",
    database="phonebook",  # или твоя база
    user="postgres",
    password="21062007",
    port=5432
)
cur = conn.cursor()

username = input("Введите имя пользователя: ")

# Проверка — есть ли такой пользователь
cur.execute("SELECT id FROM users WHERE username = %s", (username,))
user = cur.fetchone()

if user:
    user_id = user[0]
    cur.execute("SELECT score, level FROM user_score WHERE user_id = %s", (user_id,))
    result = cur.fetchone()
    if result:
        score, level = result
        print(f"Добро пожаловать, {username}! Текущий уровень: {level}, очки: {score}")
    else:
        score, level = 0, 1
        cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
        conn.commit()
else:
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    score, level = 0, 1
    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)", (user_id, score, level))
    conn.commit()
    print(f"Пользователь {username} создан!")

# === GAME SETUP ===
pygame.init()
size = 600
block = 30
screen = pygame.display.set_mode((size, size))
pygame.display.set_caption("Змейка")

green = (0, 150, 0)
snake_color = (255, 137, 0)
head_color = (255, 247, 0)
food_color = (255, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

x = randrange(0, size, block)
y = randrange(0, size, block)
snake = [(x, y)]
dx, dy = 0, 0
dirs = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}

length = 1
fps = 5 + level  # Увеличивается с уровнем

def new_food():
    pos = randrange(0, size, block), randrange(0, size, block)
    value = choice([1, 2, 3])
    timer = pygame.time.get_ticks()
    return {'pos': pos, 'value': value, 'spawn_time': timer}

food = new_food()
running = True
clock = pygame.time.Clock()

# === GAME LOOP ===
while running:
    screen.fill(green)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
            elif event.key == pygame.K_p:
                # Сохраняем игру при паузе
                cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
                conn.commit()
                print(f"Игра сохранена: Уровень {level}, Очки {score}")

    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-length:]

    for s in snake[:-1]:
        pygame.draw.rect(screen, snake_color, (s[0], s[1], block, block))
    pygame.draw.rect(screen, head_color, (snake[-1][0], snake[-1][1], block, block))

    pygame.draw.rect(screen, food_color, (*food['pos'], block, block))
    screen.blit(font_small.render(str(food['value']), True, white), (food['pos'][0]+5, food['pos'][1]+5))

    if pygame.time.get_ticks() - food['spawn_time'] > 5000:
        food = new_food()

    screen.blit(font_small.render(f"Level: {level}", True, white), (10, 10))
    screen.blit(font_small.render(f"Score: {score}", True, white), (150, 10))

    if snake[-1] == food['pos']:
        score += food['value']
        length += food['value']
        if (length - 1) % 5 == 0:
            level += 1
            fps += 1
            screen.fill(white)
            screen.blit(font.render("Next level", True, (0, 0, 0)), (size // 2 - 150, size // 2 - 30))
            pygame.display.update()
            time.sleep(2)
        food = new_food()

    if len(snake) != len(set(snake)) or x < 0 or x >= size or y < 0 or y >= size:
        screen.fill(white)
        screen.blit(font.render("Game Over", True, red), (size // 2 - 150, size // 2 - 30))
        pygame.display.update()
        time.sleep(2)
        running = False

    pygame.display.update()
    clock.tick(fps)

# Сохраняем при выходе
cur.execute("UPDATE user_score SET score = %s, level = %s WHERE user_id = %s", (score, level, user_id))
conn.commit()

cur.close()
conn.close()
pygame.quit()
