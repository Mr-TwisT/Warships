from abc import ABC, abstractmethod
import pygame
import random

SIZE = 50


class Ship(ABC):
    def __init__(self, surface, name, fraction, endurance, strength, color, x, y):
        self.surface = surface
        self.name = name
        self.fraction = fraction
        self.endurance = endurance
        self.strength = strength
        self.color = color
        self.x = x * SIZE
        self.y = y * SIZE

    def __repr__(self):
        return f"Statek(nazwa: {self.name}, frakcja: {self.fraction})"

    @abstractmethod
    def typeOfShip(self):
        pass

    def draw(self, image):
        self.surface.blit(image, (self.x, self.y))
        pygame.display.flip()

    def move(self, rockX=-1, rockY=-1):
        directions = [1, 2, 3, 4]  # Góra, prawo, dół, lewo
        randomDirection = directions[random.randint(0, 3)]
        match randomDirection:
            case 1:
                if rockX != -1:
                    if (self.y-SIZE) == rockY:
                        self.y += SIZE
                elif self.y <= (0*SIZE):
                    self.y += SIZE
                else:
                    self.y -= SIZE

                return self.y
            case 2:
                if rockX != -1:
                    if (self.x+SIZE) == rockX:
                        self.x -= SIZE
                elif self.x >= (19*SIZE):
                    self.x -= SIZE
                else:
                    self.x += SIZE

                return self.x
            case 3:
                if rockX != -1:
                    if (self.y+SIZE) == rockY:
                        self.y -= SIZE
                elif self.y >= (14*SIZE):
                    self.y -= SIZE
                else:
                    self.y += SIZE

                return self.y
            case 4:
                if rockX != -1:
                    if (self.x-SIZE) == rockX:
                        self.x += SIZE
                elif self.x <= (0*SIZE):
                    self.x += SIZE
                else:
                    self.x -= SIZE

                return self.x
            case _:
                print("Error! Wynik jest niemożliwy!")
                return 0

    def sayHello(self):
        print(
            f"Hi, my name is {self.name} and my class is {self.typeOfShip()}. My color is {self.color} and my fraction is {self.fraction}!")
