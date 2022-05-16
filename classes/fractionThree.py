from .destroyer import Destroyer
from .tanker import Tanker
from .submarine import Submarine
from .hovercraft import Hovercraft


class FractionThree:
    def __init__(self, surface, fractionName):
        self.name = fractionName

        self.destroyer1 = Destroyer(surface, "Niszczyciel1", self.name, 8, 12)
        self.destroyer2 = Destroyer(surface, "Niszczyciel2", self.name, 9, 11)
        self.destroyer3 = Destroyer(surface, "Niszczyciel3", self.name, 10, 12)
        self.tanker1 = Tanker(surface, "Tankowiec1", self.name, 8, 13)
        self.tanker2 = Tanker(surface, "Tankowiec2", self.name, 9, 13)
        self.tanker3 = Tanker(surface, "Tankowiec3", self.name, 10, 13)

        self.submarine1 = Submarine(
            surface, "Okręt podwodny1", self.name, 9, 12)
        self.submarine2 = Submarine(
            surface, "Okręt podwodny2", self.name, 9, 10)
        self.hovercraft1 = Hovercraft(
            surface, "Poduszkowiec1", self.name, 7, 13)
        self.hovercraft2 = Hovercraft(
            surface, "Poduszkowiec2", self.name, 11, 13)

        self.allMyShips = [
            self.destroyer1,
            self.destroyer2,
            self.destroyer3,
            self.tanker1,
            self.tanker2,
            self.tanker3,
            self.submarine1,
            self.submarine2,
            self.hovercraft1,
            self.hovercraft2
        ]
        # All endurance = 33
        # All strength = 35
