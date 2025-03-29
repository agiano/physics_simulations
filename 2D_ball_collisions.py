import pygame
import random
import math


class Button:
    def __init__(self, x, y, width, height, text, onclick=None):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x / 10, y / 10, width, height)
        self.color = pygame.Color(200, 255, 200)
        self.text = text
        self.onclick = onclick

    def draw_button(self, surface, font):
        pygame.draw.rect(
            surface, self.color, self.rect, 0, int(min(self.width, self.height) / 10)
        )

        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = pygame.Color(
            random.randint(100, 255), random.randint(100, 255), random.randint(100, 255)
        )
        self.velocity_x = random.uniform(-5, 5)
        self.velocity_y = random.uniform(-5, 5)

    def update(self, dt, width, height):

        # move position based on velocity
        self.x += self.velocity_x
        self.y += self.velocity_y

        # bounce off walls
        if self.x - self.radius <= 0 or self.x + self.radius >= width:
            self.velocity_x *= -1
        if self.y - self.radius <= 0 or self.y + self.radius >= height:
            self.velocity_y *= -1

        return self.x, self.y

    def draw_circle(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def check_collision(self, other):
        import math


def check_collision(ball1, ball2):

    dx = ball2.x - ball1.x
    dy = ball2.y - ball1.y
    distance = math.sqrt(dx**2 + dy**2)  # distance between ball centers

    min_distance = ball1.radius + ball2.radius  # check if balls overlap
    if distance < min_distance:
        # normalize collision vectors
        nx = dx / distance
        ny = dy / distance

        # push balls apart to prevent sticking
        overlap = min_distance - distance
        ball1.x -= nx * (overlap / 2)
        ball1.y -= ny * (overlap / 2)
        ball2.x += nx * (overlap / 2)
        ball2.y += ny * (overlap / 2)

        # compute velocity components along normal and tangent
        v1n = ball1.velocity_x * nx + ball1.velocity_y * ny
        v2n = ball2.velocity_x * nx + ball2.velocity_y * ny

        v1t = -ball1.velocity_x * ny + ball1.velocity_y * nx
        v2t = -ball2.velocity_x * ny + ball2.velocity_y * nx

        # add velocity components -> elastic collision
        ball1.velocity_x = v2n * nx - v1t * ny
        ball1.velocity_y = v2n * ny + v1t * nx
        ball2.velocity_x = v1n * nx - v2t * ny
        ball2.velocity_y = v1n * ny + v2t * nx


class Game:
    def __init__(self):
        self.width = 720
        self.height = 480
        self.circle_radius = 10
        self.x = self.width / 2
        self.y = self.height / 2
        self.dt = 0
        pygame.font.init()  # font must be initialized
        self.font = pygame.font.SysFont("Arial", 16)
        self.circles = []

        pygame.init()
        pygame.display.set_caption("Balls")
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.running = True

    def run(self):

        while self.running:
            self.screen.fill("black")
            button = Button(self.x, self.y, 80, 40, "Add Ball")  # initialize button
            button.draw_button(self.screen, self.font)  # add button to surface (screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button.rect.collidepoint(event.pos):
                        circle = Circle(self.x / 2, self.y / 2, self.circle_radius)
                        circle.draw_circle(self.screen)
                        self.circles.append(circle)

            # check collisions and update values if necessary
            for i in range(len(self.circles)):
                for j in range(i + 1, len(self.circles)):
                    check_collision(self.circles[i], self.circles[j])

            # draw all circles
            for c in self.circles:
                c.update(self.dt, self.width, self.height)
                c.draw_circle(self.screen)

            pygame.display.flip()
            self.dt = self.clock.tick(60) / 1000
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
