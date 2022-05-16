import pygame
from .ship import Ship


class Submarine(Ship):  # Okręt podwodny
    def __init__(self, surface, name, fraction, x=0, y=0, endurance=4, strength=4, color="black"):
        super().__init__(surface, name, fraction, endurance, strength, color, x, y)
        self.shipImage = pygame.image.load("./images/okret_podwodny.png")

    def typeOfShip(self):
        return "Okręt podwodny"

    def draw(self):
        super().draw(self.shipImage)
