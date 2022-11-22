
class Vehicle:
    """
    Vehicle is a type that describes a machine that helpes us travel. (This is a docstring)
    """

    def __init__(self, distance_traveled=0, unit='miles', **kwargs):    # **kwargs : this allows us to be a little more safe because now 
                                                                        # you can effectively pass infinite number of keyword arguments 
                                                                        # to the initialization function for Vehicle, Car, Boat 
                                                                        # and you can just ignore the ones that doesn't use
        # print("vehicle constructor")
        self.distance_traveled = distance_traveled
        self.unit = unit
    
    
    def description(self):
        return f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}"
        # 当 一个 Bicycle object call 这个 function 时，虽然 这个function 是从 Vehicle inherit 来的，但是 self 依然会是 Bicycle


