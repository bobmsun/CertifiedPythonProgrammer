
class Vehicle:
    """
    Vehicle is a type that describes a machine that helpes us travel. (This is a docstring)
    """

    def __init__(self, distance_traveled=0, unit='miles'): 
        # print("vehicle constructor")
        self.distance_traveled = distance_traveled
        self.unit = unit
    
    
    def description(self):
        return f"A {self.__class__.__name__} that has traveled {self.distance_traveled} {self.unit}"
        # 当 一个 Bicycle object call 这个 function 时，虽然 这个function 是从 Vehicle inherit 来的，但是 self 依然会是 Bicycle

    
