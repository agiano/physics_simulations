import pygame

wheel_png = pygame.image.load("./simulation/cannon_wheel.png")
barrel_png = pygame.image.load("./simulation/cannon_barrel.png")

width, height = 1280, 720

ball_radius = 10
ball_color = pygame.Color(200, 100, 0)

air_resistance = 0.05
friction = 0.05
gravity = 0.5

ball_x, ball_y = 120, height - 190
velocity_x, velocity_y = 6, -10
dt = 0  # number of time passed between frames --> consistent gameplay regardless of perfomance

# rectangle
rect_color = pygame.Color(0, 100, 255)
rectangle = pygame.Rect(0, height - 150, width, height)

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption("Cannon")  # set window title


def draw_cannon(screen):
    left = 100
    screen.blit(barrel_png, (left, height - 150 - 35))
    screen.blit(wheel_png, (left, height - 150 - 40))


timer = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    rect = pygame.draw.rect(screen, rect_color, rectangle)
    draw_cannon(screen)

    if timer > 2:

        velocity_y += gravity
        ball_y += velocity_y
        ball_x += velocity_x

        ball = pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

        if ball_y + ball_radius >= rect.top:
            ball_y = rect.top - ball_radius
            velocity_y *= -(1 - friction)
            velocity_x *= 1 - friction
        if ball_x + ball_radius >= width or ball_x - ball_radius <= 0:
            velocity_x *= -1

    pygame.display.flip()

    dt = clock.tick(60) / 1000  # in seconds
    timer += dt

pygame.quit()
