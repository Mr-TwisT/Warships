from .aircraftCarrier import AircraftCarrier
from .motorboat import Motorboat
from .passengerFerry import PassengerFerry
from .submarine import Submarine
from .hovercraft import Hovercraft


class FractionTwo:
    def __init__(self, surface, fractionName):
        self.name = fractionName

        self.aircraftCarrier1 = AircraftCarrier(
            surface, "Lotniskowiec1", self.name, 16, 2)
        self.aircraftCarrier2 = AircraftCarrier(
            surface, "Lotniskowiec2", self.name, 16, 3)
        self.aircraftCarrier3 = AircraftCarrier(
            surface, "Lotniskowiec3", self.name, 17, 3)
        self.motorboat1 = Motorboat(surface, "Motorówka1", self.name, 16, 1)
        self.motorboat2 = Motorboat(surface, "Motorówka2", self.name, 17, 2)
        self.motorboat3 = Motorboat(surface, "Motorówka3", self.name, 18, 3)

        self.passengerFerry = PassengerFerry(
            surface, "Prom pasażerski", self.name, 18, 1)
        self.submarine = Submarine(surface, "Okręt podwodny", self.name, 15, 4)
        self.hovercraft1 = Hovercraft(
            surface, "Poduszkowiec1", self.name, 17, 1)
        self.hovercraft2 = Hovercraft(
            surface, "Poduszkowiec2", self.name, 18, 2)

        self.allMyShips = [
            self.aircraftCarrier1,
            self.aircraftCarrier2,
            self.aircraftCarrier3,
            self.motorboat1,
            self.motorboat2,
            self.motorboat3,
            self.passengerFerry,
            self.submarine,
            self.hovercraft1,
            self.hovercraft2
        ]
        # All endurance = 35
        # All strength = 32
