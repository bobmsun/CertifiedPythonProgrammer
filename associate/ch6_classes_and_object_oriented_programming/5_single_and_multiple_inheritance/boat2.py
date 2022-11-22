
from vehicle2 import Vehicle

class Boat(Vehicle):  

    def __init__(self, boat_type='sail', distance_traveled=0, unit='miles'):
        # print("boat constructor")
        super().__init__(distance_traveled=distance_traveled, unit=unit)        # 相比 boat.py，改动是 这里用了 keywork argument
        self.boat_type = boat_type
    
    def voyage(self, distance):
        self.distance_traveled += distance
    
    def description(self):
        initial = super().description()
        return f"{initial} using a {self.boat_type}"


# python -i amphibious_vehicle2.py
# >>> water_car = AmphibiousVehicle('4 cylider')
# >>> water_car.description()
# 'A AmphibiousVehicle that has traveled 0 miles using a motor'
     
    # 如果把上面的 __init__ 函数改成如下（就是去掉了 boat_type 的 default 值）
    # def __init__(self, boat_type, distance_traveled=0, unit='miles'):
    #     # print("boat constructor")
    #     super().__init__(distance_traveled=distance_traveled, unit=unit)
    #     self.boat_type = boat_type

# 这时就会出下面的 error：
# python -i amphibious_vehicle2.py
# >>> water_car = AmphibiousVehicle('4 cylider')
# TypeError: __init__() missing 1 required positional argument: 'boat_type'

