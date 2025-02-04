import pygame
from pygame.locals import *
import time


class Snake:
    def __init__(self, surface, length):
        self.parent_screen = surface
        self.block = pygame.image.load("resources/block.jpg").convert()

        self.length = length
        self.x = [40]*length
        self.y = [40]*length
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= 40
        if self.direction == 'right':
            self.x[0] += 40
        if self.direction == 'up':
            self.y[0] -= 40
        if self.direction == 'down':
            self.y[0] += 40

        self.draw()

    def draw(self):
        self.parent_screen.fill((110, 110, 5))

        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))

        pygame.display.flip()


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((500, 500))
        self.snake = Snake(self.surface, 6)
        self.snake.draw()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                elif event.type == QUIT:
                    running = False

            self.snake.walk()
        time.sleep(0.4)

        if __name__ == '__main__':
            game = Game()
            game.run()





