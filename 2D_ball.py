# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
running = True
dt = 0

width, height = 720, 480
radius = 10
gravity = 0.5
friction = 0.9

ball_x, ball_y = width // 2, 50
velocity_y = 0
velocity_x = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")  # resets the screen

    velocity_y += gravity  # ball accelerates
    ball_y += velocity_y  # ball moves
    ball_x += velocity_x

    # collision with frame
    if ball_y + radius >= height:
        ball_y = height - radius
        velocity_y *= -(friction)

    if ball_y - radius <= 0:
        ball_y = radius
        velocity_y *= -(friction)

    if ball_x - radius <= 0:
        ball_x = radius
        velocity_x *= -(friction)

    if ball_x + radius >= width:
        ball_x = width - radius
        velocity_x *= -(friction)

    circle = pygame.draw.circle(screen, "blue", (ball_x, int(ball_y)), radius)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        velocity_y -= 1
    if keys[pygame.K_s]:
        velocity_y += 1
    if keys[pygame.K_a]:
        velocity_x -= 1
    if keys[pygame.K_d]:
        velocity_x += 1

    pygame.display.flip()  # updates the visible display

    dt = clock.tick(60) / 10000  # limits FPS to 60

pygame.quit()
