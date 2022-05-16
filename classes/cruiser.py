import pygame
from .ship import Ship


class Cruiser(Ship):  # Krążownik
    def __init__(self, surface, name, fraction, x=0, y=0, endurance=2, strength=3, color="green"):
        super().__init__(surface, name, fraction, endurance, strength, color, x, y)
        self.shipImage = pygame.image.load("./images/krazownik.png")

    def typeOfShip(self):
        return "Krążownik"

    def draw(self):
        super().draw(self.shipImage)
