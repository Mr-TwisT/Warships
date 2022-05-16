import pygame
from pygame.locals import *
import os


WIDTH = 380
HEIGHT = 60


class StartWindow:
    def __init__(self):
        x = 20
        y = 50
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

        self.islandsAmount = 0
        pygame.init()

        icon = pygame.image.load("./images/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Warships")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        self.inputRect = pygame.Rect(315, 10, 100, 32)

        self.displayText()
        pygame.display.flip()

    def displayText(self):
        self.font = pygame.font.SysFont("Arial", 28)
        text = self.font.render(
            "PODAJ ILOŚĆ WYSP (1-15): ", True, (250, 250, 250))
        self.screen.blit(text, (10, 15))

        self.usersText = ""

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_BACKSPACE:
                        self.usersText = self.usersText[:-1]
                    if event.key == K_RETURN:
                        if self.usersText != "":
                            self.islandsAmount = int(self.usersText)
                        running = False
                    else:
                        if (event.key == K_0) or (event.key == K_1) or (event.key == K_2) or (event.key == K_3) or (event.key == K_4) or (event.key == K_5) or (event.key == K_6) or (event.key == K_7) or (event.key == K_8) or (event.key == K_9):
                            self.usersText += event.unicode

                if event.type == QUIT:
                    running = False

            pygame.draw.rect(self.screen, (0, 0, 0), self.inputRect)
            textSurface = self.font.render(
                self.usersText, True, (250, 250, 250))
            self.screen.blit(
                textSurface, (self.inputRect.x+5, self.inputRect.y+5))

            pygame.display.flip()
            self.clock.tick(60)
