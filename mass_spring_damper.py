import pygame
import matplotlib.pyplot as plt


class Game:
    def __init__(self):
        self.width, self.height = 720, 480

        self.m = 2  # mass - kg
        self.k = 100  # spring constant - N/m
        self.b = 1  # damping coef - kg/s
        self.x = 100  # initial displacement - px
        self.v = 0  # initial velocity - m/s
        self.dt = 0.01  # time passed - s

        self.eq_x = 300  # resting position of spring

        self.time_array = []
        self.disp_array = []
        self.vel_array = []
        self.acc_array = []

    def run(self):

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.running = True
        t = 0  # timer
        while self.running:
            self.screen.fill("white")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            spring = pygame.image.load("./simulation/spring.png")

            # acceleration equation (hooke's law) for damped oscillation
            a = (-self.k * (self.x - self.eq_x) - self.b * self.v) / self.m

            # update v and x with simple Euler integration
            self.v += a * self.dt
            self.x += self.v * self.dt

            self.x = max(0, self.x)  # prevent negative values

            scaled_spring = pygame.transform.scale(spring, (self.x, 100))
            self.screen.blit(scaled_spring, (0, self.height / 2 - 50))

            self.rect = pygame.draw.rect(
                self.screen,
                pygame.Color(50, 50, 50),
                pygame.Rect(self.x, self.height / 2 - 50, 100, 100),
            )

            pygame.display.flip()

            self.time_array.append(t)
            self.disp_array.append(self.x)
            self.vel_array.append(self.v)
            self.acc_array.append(a)

            self.clock.tick(60)
            t += self.dt
        pygame.quit()

    def plot_graphs(self):
        fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(10, 8), sharex=True)
        ax1.plot(self.time_array, self.disp_array)
        ax1.set_title("Spring Length over Time")
        ax1.set_ylabel("Position (m)")

        ax2.plot(self.time_array, self.vel_array)
        ax2.set_title("Spring Velocity over Time")
        ax2.set_ylabel("Velocity (m/s)")

        ax3.plot(self.time_array, self.acc_array)
        ax3.set_title("Spring Acceleration over Time")
        ax3.set_xlabel("Time (s)")
        ax3.set_ylabel("Acceleration (m/s^2)")
        plt.show()


if __name__ == "__main__":
    game = Game()
    game.run()
    game.plot_graphs()
