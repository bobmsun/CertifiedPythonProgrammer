from boat2 import Boat
from car2 import Car


class AmphibiousVehicle(Car, Boat):
    
    def __init__(self, engine, tires=[], distance_traveled=0, unit='miles'):
        super().__init__(engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit)      # 相比 AmphibiousVehilce，改动是，这里用了 keyword argument
        self.boat_type = 'motor'
    
    def travel(self, land_distance=0, water_distance=0):
        super().voyage(water_distance)
        super().drive(land_distance)


# python -i amphibious_vehicle2.py
# >>> AmphibiousVehicle.__mro__
# (<class '__main__.AmphibiousVehicle'>, <class 'car2.Car'>, <class 'boat2.Boat'>, <class 'vehicle2.Vehicle'>, <class 'object'>)


