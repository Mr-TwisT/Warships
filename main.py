from abc import abstractclassmethod
import pygame

@abstractclassmethod
class Ship:
    def __init__(self):
        pass


class aircraftCarrier:  # Lotniskowiec
    def __init__(self):
        pass


class battleship:  # Pancernik
    def __init__(self):
        pass


class cruiser:  # Krążownik
    def __init__(self):
        pass


class destroyer:  # Niszczyciel
    def __init__(self):
        pass


class submarine:  # Okręt podwodny
    def __init__(self):
        pass


class motorboat:  # Motorówka
    def __init__(self):
        pass


class rockIsland:  # Wyspa skalna
    def __init__(self):
        pass


class Game:
    def __init__(self):
        pass

    def run(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.run()

# Każda frakcja będzie miała 3 rodzaje statków (w tym 2 wyjątkowe dla siebie - różne od pozostałych). W sumie na planszy niech będzie 15 statków.
# Jeśli pierwsza litera napotkanej frakcji będzie taka sama jaką ma dana frakcja to statki nie walczą
