import pygame
from .ship import Ship


class Destroyer(Ship):  # Niszczyciel
    def __init__(self, surface, name, fraction, x=0, y=0, endurance=5, strength=6, color="red"):
        super().__init__(surface, name, fraction, endurance, strength, color, x, y)
        self.shipImage = pygame.image.load("./images/niszczyciel.png")

    def typeOfShip(self):
        return "Niszczyciel"

    def draw(self):
        super().draw(self.shipImage)
