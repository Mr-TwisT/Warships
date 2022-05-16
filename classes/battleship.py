import pygame
from .ship import Ship


class Battleship(Ship):  # Pancernik
    def __init__(self, surface, name, fraction, x=0, y=0, endurance=6, strength=4, color="brown"):
        super().__init__(surface, name, fraction, endurance, strength, color, x, y)
        self.shipImage = pygame.image.load("./images/pancernik.png")

    def typeOfShip(self):
        return "Pancernik"

    def draw(self):
        super().draw(self.shipImage)
