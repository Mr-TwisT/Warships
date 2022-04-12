from abc import ABC, abstractmethod
import pygame
from pygame.locals import *
import random
import time

WIDTH = 1000
HEIGHT = 750
# 10 frakcji z których będzie losowanie
FRACTION_LIST = ["Pirates", "Poland", "Sparrows",
                 "Avengers", "United", "Soccers", "Assassins", "Titans", "Students", "Idk"]


class Ship(ABC):
    def __init__(self, surface, name, color, fraction, speed):
        self.surface = surface
        self.name = name
        self.color = color
        self.fraction = fraction
        self.speed = speed

    @abstractmethod
    def typeOfShip(self):
        pass

    def sayHello(self):
        print(
            f"Hi, my name is {self.name} and my class is {self.typeOfShip()}. My color is {self.color}, my fraction is {self.fraction}, and I have speed equal to {self.speed}!")


class AircraftCarrier(Ship):  # Lotniskowiec
    def __init__(self, surface, name, fraction, speed=1, color="lightblue"):
        super().__init__(surface, name, color, fraction, speed)

    def typeOfShip(self):
        return "Lotniskowiec"


class Battleship(Ship):  # Pancernik
    def __init__(self, surface, name, fraction, speed=2, color="brown"):
        super().__init__(surface, name, color, fraction, speed)

    def typeOfShip(self):
        return "Pancernik"


class Cruiser(Ship):  # Krążownik
    def __init__(self, surface, name, fraction, speed=3, color="green"):
        super().__init__(surface, name, color, fraction, speed)

    def typeOfShip(self):
        return "Krążownik"


class Destroyer(Ship):  # Niszczyciel
    def __init__(self, surface, name, fraction, speed=4, color="red"):
        super().__init__(surface, name, color, fraction, speed)

    def typeOfShip(self):
        return "Niszczyciel"


class Submarine(Ship):  # Okręt podwodny
    def __init__(self, surface, name, fraction, speed=5, color="black"):
        super().__init__(surface, name, color, fraction, speed)

    def typeOfShip(self):
        return "Okręt podwodny"


class Motorboat(Ship):  # Motorówka
    def __init__(self, surface, name, fraction, speed=6, color="white"):
        super().__init__(surface, name, color, fraction, speed)

    def typeOfShip(self):
        return "Motorówka"


class Tanker(Ship):  # Tankowiec
    def __init__(self, surface, name, fraction, speed=1, color="grey"):
        super().__init__(surface, name, color, fraction, speed)

    def typeOfShip(self):
        return "Tankowiec"


class PassengerFerry(Ship):  # Prom pasażerski
    def __init__(self, surface, name, fraction, speed=2, color="orange"):
        super().__init__(surface, name, color, fraction, speed)

    def typeOfShip(self):
        return "Prom pasażerski"


class Hovercraft(Ship):  # Poduszkowiec
    def __init__(self, surface, name, fraction, speed=4, color="purple"):
        super().__init__(surface, name, color, fraction, speed)

    def typeOfShip(self):
        return "Poduszkowiec"


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

        self.drawFraction()
        self.statek = Motorboat(self.surface, "Pogromca", "Avengers")
        self.statek.sayHello()

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
            pygame.draw.line(self.surface, (255, 255, 255),
                             (x, 0), (x, HEIGHT))

    def drawFraction(self):
        self.fractions = []
        firstFraction = FRACTION_LIST[random.randint(0, 9)]
        self.fractions.append(firstFraction)
        FRACTION_LIST.remove(firstFraction)
        while len(self.fractions) < 3:
            randomEnd = len(FRACTION_LIST) - 1
            randomFraction = FRACTION_LIST[random.randint(0, randomEnd)]
            self.fractions.append(randomFraction)
            FRACTION_LIST.remove(randomFraction)

        print(self.fractions)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False


if __name__ == "__main__":
    game = Game()
    game.run()

# Każda frakcja będzie miała 3/4 rodzaje statków (w tym 2 wyjątkowe dla siebie - różne od pozostałych). W sumie na planszy niech będzie 30 statków (Po 10 dla każdej frakcji).
# Jeśli pierwsza litera napotkanej frakcji będzie taka sama jaką ma dana frakcja to statki nie walczą
# Każda 'kratka' ma mieć 50px i w takim razie każda ikona powinna mieć 48px
# W sumie jest 300 pól. Niech 30 pól to będą wyspy skalne (10%) + 30 pól statki (10%)
# Speed jest w granicach <1, 6>
