
from boat import Boat
from car import Car

class AmphibiousVehicle(Car, Boat):
    def __init__(self, engine, tires=[], distance_traveled=0, unit='miles'):
        super().__init__(engine=engine, tires)