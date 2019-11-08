import pygame
import random
class Pipe:
    def __init__(self):
        self.x = 500

        self.gapDistanse = 80
        self.gapTop = random.randint(50, 500 - self.gapDistanse - 10)
        self.y = self.gapTop + self.gapDistanse

        self.width = 50
        self.speed = 6

    def move(self):
        self.x -= self.speed

    def draw(self, win):
        pygame.draw.rect(win, (0, 128, 0), (self.x, 0, self.width, self.gapTop))
        pygame.draw.rect(win, (0, 128, 0), (self.x, self.y, self.width, 500))