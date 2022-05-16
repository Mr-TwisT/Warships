import pygame
from pygame.locals import *
import random
import time

from classes.fractionOne import FractionOne
from classes.fractionTwo import FractionTwo
from classes.fractionThree import FractionThree
from classes.rockIsland import RockIsland

WIDTH = 1500
HEIGHT = 750
SIZE = 50
ISLANDS_AMOUNT = 5  # Musi być > 0
FRACTION_LIST = ["Pirates", "Poland", "Sparrows",
                 "Avengers", "United", "Soccers", "Assassins", "Titans", "Students", "Aliens"]


class Game:
    def __init__(self):
        pygame.init()

        icon = pygame.image.load("./images/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Warships")

        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.surface.fill((0, 0, 255))
        self.drawGrid(15, 20)
        self.displayHeader()
        pygame.display.flip()

        self.drawFraction()  # losuj frakcje
        self.fraction1 = FractionOne(self.surface, self.fractions[0])
        self.fraction2 = FractionTwo(self.surface, self.fractions[1])
        self.fraction3 = FractionThree(self.surface, self.fractions[2])

        self.allShips()
        self.drawAllShips()  # rysuj statki

        self.displayRockIslands()
        self.displayInfo()

        self.deadShips = []
        self.copyOfDeadShips = []

    def drawGrid(self, rows, columns):
        sizeBlockInX = (WIDTH-500) // columns  # 50px
        sizeBlockInY = HEIGHT // rows  # 50px

        x = 0
        y = 0
        for i in range(rows):
            y += sizeBlockInY
            pygame.draw.line(self.surface, (255, 255, 255),
                             (0, y), ((WIDTH-500), y))

        for i in range(columns):
            x += sizeBlockInX
            pygame.draw.line(self.surface, (255, 255, 255),
                             (x, 0), (x, HEIGHT))

    def allShips(self):
        self.allShipsOnBoard = []
        self.allShipsOnBoard.extend(self.fraction1.allMyShips)
        self.allShipsOnBoard.extend(self.fraction2.allMyShips)
        self.allShipsOnBoard.extend(self.fraction3.allMyShips)

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

    def displayRockIslands(self):
        self.rockIslands = []
        for i in range(ISLANDS_AMOUNT):
            randomX = random.randint(0, 19)
            randomY = random.randint(0, 14)
            j = -1
            while j < (len(self.allShipsOnBoard)-1):
                j += 1
                while self.isCollision(self.allShipsOnBoard[j].x, self.allShipsOnBoard[j].y, randomX*SIZE, randomY*SIZE):
                    randomX = random.randint(0, 19)
                    randomY = random.randint(0, 14)
                    j = 0
            self.rockIslands.append(RockIsland(
                self.surface, randomX*SIZE, randomY*SIZE))
            self.rockIslands[i].display()
            pygame.display.flip()

    def clearScreen(self):
        self.surface.fill((0, 0, 255))
        self.drawGrid(15, 20)
        for i in range(len(self.rockIslands)):
            self.rockIslands[i].display()
        self.displayHeader()
        self.displayInfo()
        pygame.display.flip()

    def drawAllShips(self):
        for i in range(len(self.allShipsOnBoard)):
            self.allShipsOnBoard[i].draw()

    def moveAllShips(self):
        for i in range(len(self.allShipsOnBoard)):
            copyOfI = i
            for j in range(len(self.rockIslands)):
                if self.isCollision(self.allShipsOnBoard[i].x, self.allShipsOnBoard[i].y, self.rockIslands[j].x, self.rockIslands[j].y, True):
                    copyOfI += 1
                    self.allShipsOnBoard[i].move(
                        self.rockIslands[j].x, self.rockIslands[j].y)
                elif (j+1 == len(self.rockIslands)) and (copyOfI == i):
                    self.allShipsOnBoard[i].move()

    def shipsOnBoard(self, shipsToRemove):
        copyOfAllShipsOnBoard = self.allShipsOnBoard.copy()
        if len(shipsToRemove) > 0:
            for i in range(len(copyOfAllShipsOnBoard)):
                for j in range(len(shipsToRemove)):
                    if copyOfAllShipsOnBoard[i] == shipsToRemove[j]:
                        self.allShipsOnBoard.remove(shipsToRemove[j])

    def isCollision(self, x1, y1, x2, y2, rock=False):
        if rock:
            if (((x1-SIZE) == x2) and (y1 == y2)) or (((x1+SIZE) == x2) and (y1 == y2)) or (((y1-SIZE) == y2) and (x1 == x2)) or (((y1+SIZE) == y2) and (x1 == x2)):
                return True
            else:
                return False

        if x1 == x2 and y1 == y2:
            return True
        return False

    def fight(self, ship1, ship2):
        ship1.endurance -= ship2.strength
        ship2.endurance -= ship1.strength

        if ship1.endurance <= 0:
            self.deadShips.append(ship1)
        if ship2.endurance <= 0:
            self.deadShips.append(ship2)

    def displayHeader(self):
        headerFont = pygame.font.SysFont("Arial", 30)
        info = headerFont.render("STATUS WALKI: ", True, (200, 200, 200))
        self.surface.blit(info, (1150, 10))

    def displayInfo(self):
        font = pygame.font.SysFont("Arial", 20)
        i = -1
        j = -1

        for k in range(len(self.allShipsOnBoard)):
            if self.allShipsOnBoard[k].fraction == self.fraction1.name:
                info = font.render(
                    f"Statek: {self.allShipsOnBoard[k].name}", True, (200, 200, 200))
                smallColor = pygame.transform.scale(
                    self.allShipsOnBoard[k].shipImage, (20, 20))
                self.surface.blit(info, (1010, 115+(k*25)))
                self.surface.blit(
                    smallColor, (1020 + info.get_width(), 115+(k*25)))

            elif self.allShipsOnBoard[k].fraction == self.fraction2.name:
                i += 1
                info = font.render(
                    f"Statek: {self.allShipsOnBoard[k].name}", True, (200, 200, 200))
                smallColor = pygame.transform.scale(
                    self.allShipsOnBoard[k].shipImage, (20, 20))
                self.surface.blit(info, (1280, 115+(i*25)))
                self.surface.blit(
                    smallColor, (1290 + info.get_width(), 115+(i*25)))

            elif self.allShipsOnBoard[k].fraction == self.fraction3.name:
                j += 1
                info = font.render(
                    f"Statek: {self.allShipsOnBoard[k].name}", True, (200, 200, 200))
                smallColor = pygame.transform.scale(
                    self.allShipsOnBoard[k].shipImage, (20, 20))
                self.surface.blit(info, (1010, 440+(j*25)))
                self.surface.blit(
                    smallColor, (1020 + info.get_width(), 440+(j*25)))

        info1 = font.render(
            f"Frakcja - {self.fraction1.name}", True, (200, 200, 200))
        info2 = font.render(
            f"Frakcja - {self.fraction2.name}", True, (200, 200, 200))
        info3 = font.render(
            f"Frakcja - {self.fraction3.name}", True, (200, 200, 200))

        self.surface.blit(info1, (1010, 65))
        self.surface.blit(info2, (1280, 65))
        self.surface.blit(info3, (1010, 390))

    def play(self):
        self.moveAllShips()
        self.clearScreen()
        self.drawAllShips()

        if self.copyOfDeadShips != self.deadShips:
            self.shipsOnBoard(self.deadShips)
        self.copyOfDeadShips = self.deadShips.copy()

        for i in range(len(self.allShipsOnBoard)):
            for j in range(i, len(self.allShipsOnBoard)):
                if i != j:
                    if self.isCollision(self.allShipsOnBoard[i].x, self.allShipsOnBoard[i].y, self.allShipsOnBoard[j].x, self.allShipsOnBoard[j].y) and (self.allShipsOnBoard[i].fraction[0] != self.allShipsOnBoard[j].fraction[0]):
                        self.fight(
                            self.allShipsOnBoard[i], self.allShipsOnBoard[j])

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
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
