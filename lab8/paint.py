import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Paint")
screen.fill(pygame.Color('white'))

# Основные переменные
clock = pygame.time.Clock()
FPS = 60  # Частота обновления экрана
radius = 15  # Радиус кисти
color = 'blue'  # Цвет по умолчанию
mode = 'tail'  # Текущий режим рисования
points = []  # Список точек для режима "хвост"
draw = False  # Флаг, указывающий, рисуем ли мы
prev_pos = (0, 0)  # Предыдущая позиция мыши
font = pygame.font.SysFont(None, 60)  # Шрифт для отображения цвета

# Функция для рисования однотонной линии между точками
def drawLineBetween(screen, start, end, width, color_name):
    # Вычисляем расстояние между точками
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    # Получаем цвет
    color = pygame.Color(color_name)

    # Рисуем линию из маленьких кружков между двумя точками
    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_t:
                mode = 'tail'
            elif event.key == pygame.K_e:
                mode = 'eraser'
            elif event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))
            elif event.key == pygame.K_1:
                color = 'black'
            elif event.key == pygame.K_2:
                color = 'green'
            elif event.key == pygame.K_3:
                color = 'red'
            elif event.key == pygame.K_4:
                color = 'blue'
            elif event.key == pygame.K_5:
                color = 'yellow'
            elif event.key == pygame.K_6:
                color = 'orange'
            elif event.key == pygame.K_7:
                color = 'purple'
            elif event.key == pygame.K_8:
                color = 'brown'
            elif event.key == pygame.K_9:
                color = 'gray'
            elif event.key == pygame.K_0:
                color = 'pink'

        # Нажатие кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            prev_pos = event.pos
            if mode == 'tail':
                points.append(event.pos)

        # Отпускание кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
            if mode == 'rectangle':
                x1, y1 = prev_pos
                x2, y2 = event.pos
                pygame.draw.rect(screen, pygame.Color(color),
                                 pygame.Rect(min(x1, x2), min(y1, y2),
                                             abs(x2 - x1), abs(y2 - y1)), radius)
            elif mode == 'circle':
                x1, y1 = prev_pos
                x2, y2 = event.pos
                center = ((x1 + x2) // 2, (y1 + y2) // 2)
                rad = max(abs(x2 - x1), abs(y2 - y1)) // 2
                pygame.draw.circle(screen, pygame.Color(color), center, rad, radius)
            points.clear()

        # Движение мыши
        if event.type == pygame.MOUSEMOTION:
            if draw:
                if mode == 'tail':
                    points.append(event.pos)
                    points = points[-256:]  # Ограничение длины следа
                elif mode == 'eraser':
                    pygame.draw.circle(screen, pygame.Color('white'), event.pos, radius)

    # Рисуем однотонный хвост
    if mode == 'tail' and len(points) > 1:
        for i in range(len(points) - 1):
            drawLineBetween(screen, points[i], points[i + 1], radius, color)

    # Отображаем текущий цвет кисти в левом верхнем углу
    render_radius = font.render(str("color"), True, pygame.Color(color))
    screen.blit(render_radius, (5, 5))

    # Обновляем экран
    pygame.display.flip()
    clock.tick(FPS)