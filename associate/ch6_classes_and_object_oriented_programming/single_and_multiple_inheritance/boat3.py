
from vehicle2 import Vehicle

class Boat(Vehicle):  

    # If we have more arguments, e.g. we are trying to pass 5 arguments that only takes three, we can use **kwargs
    # which is a way to collect all additional keyword arguments that are passed in into a variable
    # If there aren't any, then this will just be an empty dictionary
    def __init__(self, boat_type='sail', distance_traveled=0, unit='miles', **kwargs): # so now you can pass infinitely number of keyword arguments
        # print("boat constructor")
        super().__init__(distance_traveled=distance_traveled, unit=unit)
        self.boat_type = boat_type
    
    def voyage(self, distance):
        self.distance_traveled += distance
    
    def description(self):
        initial = super().description()
        return f"{initial} using a {self.boat_type}"

