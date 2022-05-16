import pygame
from .ship import Ship


class AircraftCarrier(Ship):  # Lotniskowiec
    def __init__(self, surface, name, fraction, x=0, y=0, endurance=5, strength=5, color="lightblue"):
        super().__init__(surface, name, fraction, endurance, strength, color, x, y)
        self.shipImage = pygame.image.load("./images/lotniskowiec.png")

    def typeOfShip(self):
        return "Lotniskowiec"

    def draw(self):
        super().draw(self.shipImage)
