from abc import abstractclassmethod
from turtle import width
import pygame
import time

WIDTH = 1000
HEIGHT = 750
FRACTION_LIST = ["", "", "", ""]


@abstractclassmethod
class Ship:
    def __init__(self):
        pass


class aircraftCarrier:  # Lotniskowiec
    def __init__(self):
        pass


class battleship:  # Pancernik
    def __init__(self):
        pass


class cruiser:  # Krążownik
    def __init__(self):
        pass


class destroyer:  # Niszczyciel
    def __init__(self):
        pass


class submarine:  # Okręt podwodny
    def __init__(self):
        pass


class motorboat:  # Motorówka
    def __init__(self):
        pass


class rockIsland:  # Wyspa skalna
    def __init__(self):
        pass


class Game:
    def __init__(self):
        pygame.init()

        icon = pygame.image.load("./images/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Warships")

        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.surface.fill((0, 0, 255))
        self.drawGrid(15, 20)
        pygame.display.flip()

        time.sleep(5)

    def drawGrid(self, rows, columns):
        sizeBlockInX = WIDTH // columns  # 50px
        sizeBlockInY = HEIGHT // rows  # 50px

        x = 0
        y = 0
        for i in range(rows):
            y += sizeBlockInY
            pygame.draw.line(self.surface, (255, 255, 255), (0, y), (WIDTH, y))
        
        for i in range(columns):
            x += sizeBlockInX
            pygame.draw.line(self.surface, (255, 255, 255), (x, 0), (x, HEIGHT))

    def run(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.run()

# Każda frakcja będzie miała 3 rodzaje statków (w tym 2 wyjątkowe dla siebie - różne od pozostałych). W sumie na planszy niech będzie 15 statków.
# Jeśli pierwsza litera napotkanej frakcji będzie taka sama jaką ma dana frakcja to statki nie walczą
# Każda 'kratka' ma mieć 50px i w takim razie każda ikona powinna mieć 48px
