import pygame


class RockIsland:  # Wyspa skalna
    def __init__(self, surface, x, y):
        self.rockIslandImage = pygame.image.load("./images/rock.png")
        self.surface = surface
        self.x = x
        self.y = y

    def display(self):
        self.surface.blit(self.rockIslandImage, (self.x, self.y))
