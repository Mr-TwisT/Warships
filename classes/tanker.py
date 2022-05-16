import pygame
from .ship import Ship


class Tanker(Ship):  # Tankowiec
    def __init__(self, surface, name, fraction, x=0, y=0, endurance=2, strength=1, color="grey"):
        super().__init__(surface, name, fraction, endurance, strength, color, x, y)
        self.shipImage = pygame.image.load("./images/tankowiec.png")

    def typeOfShip(self):
        return "Tankowiec"

    def draw(self):
        super().draw(self.shipImage)
