import pygame
from .ship import Ship


class Motorboat(Ship):  # Motorówka
    def __init__(self, surface, name, fraction, x=0, y=0, endurance=3, strength=2, color="white"):
        super().__init__(surface, name, fraction, endurance, strength, color, x, y)
        self.shipImage = pygame.image.load("./images/motorowka.png")

    def typeOfShip(self):
        return "Motorówka"

    def draw(self):
        super().draw(self.shipImage)
