import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
is_red = True
x = 400
y = 300
radius = 25
speed = 20
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y-speed-radius>=0:
        y-=speed
    if pressed[pygame.K_DOWN] and y+speed+radius<=600:
        y+=speed
    if pressed[pygame.K_LEFT] and x-speed-radius>=0:
        x-=speed
    if pressed[pygame.K_RIGHT] and x+speed+radius<=800:
        x+=speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), [x, y], radius)

    pygame.display.flip()
    clock.tick(60)
