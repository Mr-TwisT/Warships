import pygame
from .ship import Ship


class Hovercraft(Ship):  # Poduszkowiec
    def __init__(self, surface, name, fraction, x=0, y=0, endurance=2, strength=3, color="purple"):
        super().__init__(surface, name, fraction, endurance, strength, color, x, y)
        self.shipImage = pygame.image.load("./images/poduszkowiec.png")

    def typeOfShip(self):
        return "Poduszkowiec"

    def draw(self):
        super().draw(self.shipImage)
