from boat2 import Boat
from car2 import Car

# When you are creating class, you should use CamelCase instead of snake_case
class AmphibiousVehicle(Car, Boat):
    # pass
    # 这时 python -i amphibious_vehicle.py 
    # 会出 error：TypeError: __init__() missing 1 required positional argument: 'engine'
    # 这里有一个 Method (class) Resolution Order 的概念: the order we go about actual calling function
    # Method (class) Resolution Order: the order we go about actual calling function
    # If AmphibiousVehicle doesn't define it, it's gonna check car
    # If Car doesn't define it, it's gonna check Boat
    # If Boat doesn't define it, it's gonna check what they inherit from, in this case both Car and Boat are Vehicle
    # If Vehicle doesn't have it, it's gonna check what Vehicle inherit from. It's gonna be Object.

    # 自己有个 问题需要探究: 改成 class AmphibiousVehicle(Boat, Car) 之后，__init__ 的顺序 boat -> car -> vehilce, 这是为什么？？？

    def __init__(self, engine, tires=[], distance_traveled=0, unit='miles'):
        super().__init__(engine, tires, distance_traveled, unit)
        self.boat_type = 'motor'
    
    def travel(self, land_distance=0, water_distance=0):
        super().voyage(water_distance)
        super().drive(land_distance)


# python -i amphibious_vehicle.py
# water_car = AmphibiousVehicle('4 cyclinder')
# >>> water_car.description()
# 'A AmphibiousVehicle that has traveled miles miles using a motor'           # 这里打印的是 boat 的 description，这是由 method resolution order 造成的；这里的 miles miles 也是由 method resolution order 造成的 
# >>> water_car.tires
# ['tire', 'tire', 'tire', 'tire']

# check method resolution order:
# >>> AmphibiousVehicle.__mro__
# (<class '__main__.AmphibiousVehicle'>, <class 'car.Car'>, <class 'boat.Boat'>, <class 'vehicle.Vehicle'>, <class 'object'>)
# This doesn't just work for if it doesn't find it, it also works for if you call super(), what's the next thing that's gonna invoke.

# Then how do we fix it? 
# See 2
