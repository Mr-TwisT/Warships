from .battleship import Battleship
from .cruiser import Cruiser
from .submarine import Submarine
from .passengerFerry import PassengerFerry


class FractionOne:
    def __init__(self, surface, fractionName):
        self.name = fractionName

        self.battleship1 = Battleship(surface, "Pancernik1", self.name, 2, 4)
        self.battleship2 = Battleship(surface, "Pancernik2", self.name, 3, 3)
        self.battleship3 = Battleship(surface, "Pancernik3", self.name, 4, 2)
        self.cruiser1 = Cruiser(surface, "Krążownik1", self.name, 1, 3)
        self.cruiser2 = Cruiser(surface, "Krążownik2", self.name, 2, 2)
        self.cruiser3 = Cruiser(surface, "Krążownik3", self.name, 3, 1)

        self.submarine1 = Submarine(
            surface, "Okręt podwodny1", self.name, 2, 3)
        self.submarine2 = Submarine(
            surface, "Okręt podwodny2", self.name, 3, 2)
        self.passengerFerry1 = PassengerFerry(
            surface, "Prom pasażerski1", self.name, 1, 2)
        self.passengerFerry2 = PassengerFerry(
            surface, "Prom pasażerski2", self.name, 2, 1)

        self.allMyShips = [
            self.battleship1,
            self.battleship2,
            self.battleship3,
            self.cruiser1,
            self.cruiser2,
            self.cruiser3,
            self.submarine1,
            self.submarine2,
            self.passengerFerry1,
            self.passengerFerry2
        ]
        # All endurance = 38
        # All strength = 31
