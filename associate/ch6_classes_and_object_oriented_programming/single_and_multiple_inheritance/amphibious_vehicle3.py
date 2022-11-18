from boat2 import Boat
from car2 import Car


class AmphibiousVehicle(Car, Boat):
    
    def __init__(self, engine, tires=[], distance_traveled=0, unit='miles'):
        super().__init__(engine=engine, tires=tires, distance_traveled=distance_traveled, unit=unit)
        self.boat_type = 'motor'
    
    def travel(self, land_distance=0, water_distance=0):
        super().voyage(water_distance)
        super().drive(land_distance)

        # super() is useful when we are customizing a method that is already created by one of our parent classes and we need to use the 
        # original implementation in our new customized implementation

        # Because we inherit from Car and Boat, so our AmphibiousVehicle instances have voyage and drive just by themselves
        self.voyage(water_distance)
        self.drive(land_distance)


