import pygame
import math

# Initialize Pygame
pygame.init()

# Screen setup
w, h = 720, 480
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()


# Pendulum parameters
x0, y0 = w // 2, 0  # pivot point (fixed)
l = 200  # string length
theta = math.pi / 4  # angle
g = 9.8
dt = 0.1
omega = 0  # angular velocity

running = True
while running:
    screen.fill("black")  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Angular acceleration (θ'' = - g/L * sin(θ))
    alpha = -(g / l) * math.sin(theta)

    # Angular velocity and angle
    omega += alpha * dt
    theta += omega * dt

    # Calculate ball position
    x = x0 + l * math.sin(theta)
    y = y0 + l * math.cos(theta)

    # Draw pendulum
    pygame.draw.line(screen, "white", (x0, y0), (x, y), 3)
    pygame.draw.circle(screen, pygame.Color(100, 100, 255), (int(x), int(y)), 20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
