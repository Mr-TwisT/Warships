import pygame
from .ship import Ship


class PassengerFerry(Ship):  # Prom pasażerski
    def __init__(self, surface, name, fraction, x=0, y=0, endurance=3, strength=1, color="orange"):
        super().__init__(surface, name, fraction, endurance, strength, color, x, y)
        self.shipImage = pygame.image.load("./images/prom_pasazerski.png")

    def typeOfShip(self):
        return "Prom pasażerski"

    def draw(self):
        super().draw(self.shipImage)
