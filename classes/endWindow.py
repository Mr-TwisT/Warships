import pygame
from pygame.locals import *


WIDTH = 500
HEIGHT = 100


class EndWindow:
    def __init__(self):
        pygame.init()

        icon = pygame.image.load("./images/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Warships")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((0, 0, 0))

    def displayText(self, winner):
        self.winner = winner
        self.font = pygame.font.SysFont("Arial", 28)
        text = self.font.render(f"{self.winner}!", True, (250, 250, 250))
        self.screen.blit(text, (10, 25))
        pygame.display.flip()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == QUIT:
                    running = False
