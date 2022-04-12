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


class RockIsland:  # Wyspa skalna
    def __init__(self):
        pass


class FractionOne:
    def __init__(self, surface, fractionName):
        self.name = fractionName

        self.battleship1 = Battleship(surface, "someName", self.name)
        self.battleship2 = Battleship(surface, "someName", self.name)
        self.battleship3 = Battleship(surface, "someName", self.name)
        self.cruiser1 = Cruiser(surface, "someName", self.name)
        self.cruiser2 = Cruiser(surface, "someName", self.name)
        self.cruiser3 = Cruiser(surface, "someName", self.name)

        self.submarine1 = Submarine(surface, "someName", self.name)
        self.submarine2 = Submarine(surface, "someName", self.name)
        self.passengerFerry1 = PassengerFerry(surface, "someName", self.name)
        self.passengerFerry2 = PassengerFerry(surface, "someName", self.name)
        # All speed = 29


class FractionTwo:
    def __init__(self, surface, fractionName):
        self.name = fractionName

        self.aircraftCarrier1 = AircraftCarrier(surface, "someName", self.name)
        self.aircraftCarrier2 = AircraftCarrier(surface, "someName", self.name)
        self.aircraftCarrier3 = AircraftCarrier(surface, "someName", self.name)
        self.motorboat1 = Motorboat(surface, "someName", self.name)
        self.motorboat2 = Motorboat(surface, "someName", self.name)
        self.motorboat3 = Motorboat(surface, "someName", self.name)

        self.passengerFerry = PassengerFerry(surface, "someName", self.name)
        self.submarine = Submarine(surface, "someName", self.name)
        self.hovercraft1 = Hovercraft(surface, "someName", self.name)
        self.hovercraft2 = Hovercraft(surface, "someName", self.name)
        # All speed = 36


class FractionThree:
    def __init__(self, surface, fractionName):
        self.name = fractionName

        self.destroyer1 = Destroyer(surface, "someName", self.name)
        self.destroyer2 = Destroyer(surface, "someName", self.name)
        self.destroyer3 = Destroyer(surface, "someName", self.name)
        self.tanker1 = Tanker(surface, "someName", self.name)
        self.tanker2 = Tanker(surface, "someName", self.name)
        self.tanker3 = Tanker(surface, "someName", self.name)

        self.submarine1 = Submarine(surface, "someName", self.name)
        self.submarine2 = Submarine(surface, "someName", self.name)
        self.hovercraft1 = Hovercraft(surface, "someName", self.name)
        self.hovercraft2 = Hovercraft(surface, "someName", self.name)
        # All speed = 33


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
        self.fraction1 = FractionOne(self.surface, self.fractions[0])
        self.fraction2 = FractionTwo(self.surface, self.fractions[1])
        self.fraction3 = FractionThree(self.surface, self.fractions[2])

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
