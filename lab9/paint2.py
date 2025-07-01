# r - rectangle
# s - square
# c - circle
# v - triangle (right)
# w - triangle (equilateral)
# y - rhombus
# t - tail
# e - eraser
# q - clear
import pygame
import math

# Инициализация библиотеки Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 1200, 800  # Ширина и высота окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание игрового окна
pygame.display.set_caption("Pygame Paint")  # Название окна
screen.fill(pygame.Color('white'))  # Заполнение экрана белым цветом

# Основные переменные для работы программы
clock = pygame.time.Clock()  # Таймер для управления FPS
FPS = 60  # Частота обновления экрана (кадров в секунду)
radius = 15  # Толщина линий и границ фигур
color = 'blue'  # Цвет по умолчанию
mode = 'tail'  # Текущий режим рисования ('tail' означает свободное рисование)
points = []  # Список точек для режима свободного рисования
draw = False  # Флаг, указывающий, удерживается ли кнопка мыши
prev_pos = (0, 0)  # Предыдущая позиция мыши (для начала рисования фигуры)
font = pygame.font.SysFont(None, 60)  # Шрифт для отображения цвета на экране

# Функция для рисования плавной линии между двумя точками
def drawLineBetween(screen, start, end, width, color_name):
    # Вычисляем разницу координат между начальной и конечной точкой
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))  # Количество шагов для рисования линии

    # Преобразуем имя цвета в объект pygame.Color
    color = pygame.Color(color_name)

    # Проходим по всем шагам от одной точки до другой
    for i in range(iterations):
        progress = i / iterations  # Прогресс от 0 до 1
        aprogress = 1 - progress  # Обратный прогресс
        # Вычисляем промежуточную точку на линии
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        # Рисуем маленький кружок (точку) на этой позиции
        pygame.draw.circle(screen, color, (x, y), width)

# Основной цикл программы — работает до закрытия окна
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # При закрытии окна завершаем программу
            pygame.quit()
            exit()

        # Обработка нажатий клавиш
        if event.type == pygame.KEYDOWN:
            # Выбор режима рисования по клавишам
            if event.key == pygame.K_r:
                mode = 'rectangle'  # Прямоугольник
            elif event.key == pygame.K_c:
                mode = 'circle'  # Круг
            elif event.key == pygame.K_t:
                mode = 'tail'  # Рисование "хвостом"
            elif event.key == pygame.K_e:
                mode = 'eraser'  # Ластик
            elif event.key == pygame.K_s:
                mode = 'square'  # Квадрат
            elif event.key == pygame.K_v:
                mode = 'right_triangle'  # Прямоугольный треугольник
            elif event.key == pygame.K_w:
                mode = 'equilateral_triangle'  # Равносторонний треугольник
            elif event.key == pygame.K_y:
                mode = 'rhombus'  # Ромб

            # Очистка всего холста
            elif event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))

            # Выбор цвета по цифрам
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

        # При нажатии кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True  # Устанавливаем флаг рисования
            prev_pos = event.pos  # Сохраняем начальную точку
            if mode == 'tail':
                points.append(event.pos)  # Добавляем точку для хвоста

        # При отпускании кнопки мыши
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False  # Прекращаем рисование
            x1, y1 = prev_pos  # Начальные координаты
            x2, y2 = event.pos  # Конечные координаты

            # В зависимости от выбранного режима рисуем соответствующую фигуру
            if mode == 'rectangle':
                pygame.draw.rect(screen, pygame.Color(color),
                                 pygame.Rect(min(x1, x2), min(y1, y2),
                                             abs(x2 - x1), abs(y2 - y1)), radius)

            elif mode == 'square':
                side = min(abs(x2 - x1), abs(y2 - y1))  # Сторона квадрата
                pygame.draw.rect(screen, pygame.Color(color),
                                 pygame.Rect(x1, y1, side, side), radius)

            elif mode == 'circle':
                center = ((x1 + x2) // 2, (y1 + y2) // 2)  # Центр круга
                rad = max(abs(x2 - x1), abs(y2 - y1)) // 2  # Радиус
                pygame.draw.circle(screen, pygame.Color(color), center, rad, radius)

            elif mode == 'right_triangle':
                # Прямоугольный треугольник с прямым углом в (x1, y2)
                points_rt = [(x1, y1), (x2, y2), (x1, y2)]
                pygame.draw.polygon(screen, pygame.Color(color), points_rt, radius)

            elif mode == 'equilateral_triangle':
                # Равносторонний треугольник, основание внизу
                side = abs(x2 - x1)
                height = int((3 ** 0.5 / 2) * side)  # Высота по формуле
                points_eq = [
                    (x1, y2),
                    (x1 + side, y2),
                    (x1 + side // 2, y2 - height)
                ]
                pygame.draw.polygon(screen, pygame.Color(color), points_eq, radius)

            elif mode == 'rhombus':
                # Ромб с центром между двумя точками
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2
                dx = abs(x2 - x1) // 2  # Половина ширины
                dy = abs(y2 - y1) // 2  # Половина высоты
                points_rh = [
                    (center_x, center_y - dy),  # Верх
                    (center_x + dx, center_y),  # Право
                    (center_x, center_y + dy),  # Низ
                    (center_x - dx, center_y)   # Лево
                ]
                pygame.draw.polygon(screen, pygame.Color(color), points_rh, radius)

            points.clear()  # Очищаем хвост

        # Обработка движения мыши
        if event.type == pygame.MOUSEMOTION:
            if draw:
                if mode == 'tail':
                    points.append(event.pos)  # Добавляем точку к траектории
                    points = points[-256:]  # Ограничиваем длину хвоста
                elif mode == 'eraser':
                    # В режиме ластика рисуем белым кругом (стираем)
                    pygame.draw.circle(screen, pygame.Color('white'), event.pos, radius)

    # Если активен режим "tail" и есть хотя бы 2 точки — рисуем плавную линию
    if mode == 'tail' and len(points) > 1:
        for i in range(len(points) - 1):
            drawLineBetween(screen, points[i], points[i + 1], radius, color)

    # Отображение текста "color" текущим выбранным цветом в левом верхнем углу
    render_text = font.render("color", True, pygame.Color(color))
    screen.blit(render_text, (5, 5))

    # Обновляем экран
    pygame.display.flip()
    clock.tick(FPS)
