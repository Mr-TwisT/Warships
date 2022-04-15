from abc import ABC, abstractmethod
import pygame
from pygame.locals import *
import random
import time

WIDTH = 1000
HEIGHT = 750
SIZE = 50
# 10 frakcji z których będzie losowanie
FRACTION_LIST = ["Pirates", "Poland", "Sparrows",
                 "Avengers", "United", "Soccers", "Assassins", "Titans", "Students", "Idk"]


class Ship(ABC):
    def __init__(self, surface, name, fraction, speed, endurance, color, x, y):
        self.surface = surface
        self.name = name
        self.fraction = fraction
        self.speed = speed
        self.endurance = endurance
        self.color = color
        self.x = x * SIZE
        self.y = y * SIZE

    @abstractmethod
    def typeOfShip(self):
        pass

    def draw(self, image):
        self.surface.blit(image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        directions = [1, 2, 3, 4]  # Góra, prawo, dół, lewo
        randomDirection = directions[random.randint(0, 3)]
        match randomDirection:
            case 1:
                self.y -= SIZE
                if self.y < (0*SIZE):
                    self.y += SIZE
                return self.y
            case 2:
                self.x += SIZE
                if self.x > (19*SIZE):
                    self.x -= SIZE
                return self.x
            case 3:
                self.y += SIZE
                if self.y > (14*SIZE):
                    self.y -= SIZE
                return self.y
            case 4:
                self.x -= SIZE
                if self.x < (0*SIZE):
                    self.x += SIZE
                return self.x
            case _:
                print("Error! Wynik jest niemożliwy!")
                return 0

    def sayHello(self):
        print(
            f"Hi, my name is {self.name} and my class is {self.typeOfShip()}. My color is {self.color}, my fraction is {self.fraction}, and I have speed equal to {self.speed}!")


class AircraftCarrier(Ship):  # Lotniskowiec
    def __init__(self, surface, name, fraction, x=0, y=0, speed=1, endurance=5, color="lightblue"):
        super().__init__(surface, name, fraction, speed, endurance, color, x, y)
        self.shipImage = pygame.image.load("./images/lotniskowiec.png")

    def typeOfShip(self):
        return "Lotniskowiec"

    def draw(self):
        super().draw(self.shipImage)


class Battleship(Ship):  # Pancernik
    def __init__(self, surface, name, fraction, x=0, y=0, speed=2, endurance=6, color="brown"):
        super().__init__(surface, name, fraction, speed, endurance, color, x, y)
        self.shipImage = pygame.image.load("./images/pancernik.png")

    def typeOfShip(self):
        return "Pancernik"

    def draw(self):
        super().draw(self.shipImage)


class Cruiser(Ship):  # Krążownik
    def __init__(self, surface, name, fraction, x=0, y=0, speed=3, endurance=3, color="green"):
        super().__init__(surface, name, fraction, speed, endurance, color, x, y)
        self.shipImage = pygame.image.load("./images/krazownik.png")

    def typeOfShip(self):
        return "Krążownik"

    def draw(self):
        super().draw(self.shipImage)


class Destroyer(Ship):  # Niszczyciel
    def __init__(self, surface, name, fraction, x=0, y=0, speed=4, endurance=5, color="red"):
        super().__init__(surface, name, fraction, speed, endurance, color, x, y)
        self.shipImage = pygame.image.load("./images/niszczyciel.png")

    def typeOfShip(self):
        return "Niszczyciel"

    def draw(self):
        super().draw(self.shipImage)


class Submarine(Ship):  # Okręt podwodny
    def __init__(self, surface, name, fraction, x=0, y=0, speed=5, endurance=4, color="black"):
        super().__init__(surface, name, fraction, speed, endurance, color, x, y)
        self.shipImage = pygame.image.load("./images/okret_podwodny.png")

    def typeOfShip(self):
        return "Okręt podwodny"

    def draw(self):
        super().draw(self.shipImage)


class Motorboat(Ship):  # Motorówka
    def __init__(self, surface, name, fraction, x=0, y=0, speed=6, endurance=1, color="white"):
        super().__init__(surface, name, fraction, speed, endurance, color, x, y)
        self.shipImage = pygame.image.load("./images/motorowka.png")

    def typeOfShip(self):
        return "Motorówka"

    def draw(self):
        super().draw(self.shipImage)


class Tanker(Ship):  # Tankowiec
    def __init__(self, surface, name, fraction, x=0, y=0, speed=1, endurance=2, color="grey"):
        super().__init__(surface, name, fraction, speed, endurance, color, x, y)
        self.shipImage = pygame.image.load("./images/tankowiec.png")

    def typeOfShip(self):
        return "Tankowiec"

    def draw(self):
        super().draw(self.shipImage)


class PassengerFerry(Ship):  # Prom pasażerski
    def __init__(self, surface, name, fraction, x=0, y=0, speed=2, endurance=3, color="orange"):
        super().__init__(surface, name, fraction, speed, endurance, color, x, y)
        self.shipImage = pygame.image.load("./images/prom_pasazerski.png")

    def typeOfShip(self):
        return "Prom pasażerski"

    def draw(self):
        super().draw(self.shipImage)


class Hovercraft(Ship):  # Poduszkowiec
    def __init__(self, surface, name, fraction, x=0, y=0, speed=4, endurance=2, color="purple"):
        super().__init__(surface, name, fraction, speed, endurance, color, x, y)
        self.shipImage = pygame.image.load("./images/poduszkowiec.png")

    def typeOfShip(self):
        return "Poduszkowiec"

    def draw(self):
        super().draw(self.shipImage)


class RockIsland:  # Wyspa skalna
    def __init__(self):
        pass


class FractionOne:
    def __init__(self, surface, fractionName):
        self.name = fractionName

        self.battleship1 = Battleship(surface, "someName", self.name, 2, 4)
        self.battleship2 = Battleship(surface, "someName", self.name, 3, 3)
        self.battleship3 = Battleship(surface, "someName", self.name, 4, 2)
        self.cruiser1 = Cruiser(surface, "someName", self.name, 1, 3)
        self.cruiser2 = Cruiser(surface, "someName", self.name, 2, 2)
        self.cruiser3 = Cruiser(surface, "someName", self.name, 3, 1)

        self.submarine1 = Submarine(surface, "someName", self.name, 2, 3)
        self.submarine2 = Submarine(surface, "someName", self.name, 3, 2)
        self.passengerFerry1 = PassengerFerry(surface, "someName", self.name, 1, 2)
        self.passengerFerry2 = PassengerFerry(surface, "someName", self.name, 2, 1)

        self.allMyShips = [
            self.battleship1,
            self.battleship2,
            self.battleship3,
            self.cruiser1,
            self.cruiser2,
            self.cruiser3,
            self.submarine1,
            self.submarine2,
            self.passengerFerry1,
            self.passengerFerry2
        ]
        # All speed = 29
        # All endurance = 41


class FractionTwo:
    def __init__(self, surface, fractionName):
        self.name = fractionName

        self.aircraftCarrier1 = AircraftCarrier(surface, "someName", self.name, 16, 2)
        self.aircraftCarrier2 = AircraftCarrier(surface, "someName", self.name, 16, 3)
        self.aircraftCarrier3 = AircraftCarrier(surface, "someName", self.name, 17, 3)
        self.motorboat1 = Motorboat(surface, "someName", self.name, 16, 1)
        self.motorboat2 = Motorboat(surface, "someName", self.name, 17, 2)
        self.motorboat3 = Motorboat(surface, "someName", self.name, 18, 3)

        self.passengerFerry = PassengerFerry(surface, "someName", self.name, 18, 1)
        self.submarine = Submarine(surface, "someName", self.name, 15, 4)
        self.hovercraft1 = Hovercraft(surface, "someName", self.name, 17, 1)
        self.hovercraft2 = Hovercraft(surface, "someName", self.name, 18, 2)

        self.allMyShips = [
            self.aircraftCarrier1,
            self.aircraftCarrier2,
            self.aircraftCarrier3,
            self.motorboat1,
            self.motorboat2,
            self.motorboat3,
            self.passengerFerry,
            self.submarine,
            self.hovercraft1,
            self.hovercraft2
        ]
        # All speed = 36
        # All endurance = 29


class FractionThree:
    def __init__(self, surface, fractionName):
        self.name = fractionName

        self.destroyer1 = Destroyer(surface, "someName", self.name, 8, 12)
        self.destroyer2 = Destroyer(surface, "someName", self.name, 9, 11)
        self.destroyer3 = Destroyer(surface, "someName", self.name, 10, 12)
        self.tanker1 = Tanker(surface, "someName", self.name, 8, 13)
        self.tanker2 = Tanker(surface, "someName", self.name, 9, 13)
        self.tanker3 = Tanker(surface, "someName", self.name, 10, 13)

        self.submarine1 = Submarine(surface, "someName", self.name, 9, 12)
        self.submarine2 = Submarine(surface, "someName", self.name, 9, 10)
        self.hovercraft1 = Hovercraft(surface, "someName", self.name, 7, 13)
        self.hovercraft2 = Hovercraft(surface, "someName", self.name, 11, 13)

        self.allMyShips = [
            self.destroyer1,
            self.destroyer2,
            self.destroyer3,
            self.tanker1,
            self.tanker2,
            self.tanker3,
            self.submarine1,
            self.submarine2,
            self.hovercraft1,
            self.hovercraft2
        ]
        # All speed = 33
        # All endurance = 33


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

        self.drawFraction()  # losuj frakcje
        self.fraction1 = FractionOne(self.surface, self.fractions[0])
        self.fraction2 = FractionTwo(self.surface, self.fractions[1])
        self.fraction3 = FractionThree(self.surface, self.fractions[2])

        self.drawAllShips()  # rysuj statki

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

    def drawAllShips(self):
        for i in range(10):
            self.fraction1.allMyShips[i].draw()
            self.fraction2.allMyShips[i].draw()
            self.fraction3.allMyShips[i].draw()

    def moveAllShips(self):
        for i in range(10):
            self.fraction1.allMyShips[i].move()
            self.fraction2.allMyShips[i].move()
            self.fraction3.allMyShips[i].move()

    def clearScreen(self):
        self.surface.fill((0, 0, 255))
        self.drawGrid(15, 20)
        pygame.display.flip()

    def play(self):
        self.moveAllShips()
        self.clearScreen()
        self.drawAllShips()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False

            self.play()
            time.sleep(0.3)


if __name__ == "__main__":
    game = Game()
    game.run()

# Każda frakcja będzie miała 3/4 rodzaje statków (w tym 2 wyjątkowe dla siebie - różne od pozostałych). W sumie na planszy niech będzie 30 statków (Po 10 dla każdej frakcji).
# Jeśli pierwsza litera napotkanej frakcji będzie taka sama jaką ma dana frakcja to statki nie walczą
# Każda 'kratka' ma mieć 50px i w takim razie każda ikona powinna mieć 48px
# W sumie jest 300 pól. Niech 30 pól to będą wyspy skalne (10%) + 30 pól statki (10%)
# Speed i endurance jest w granicach <1, 6>
