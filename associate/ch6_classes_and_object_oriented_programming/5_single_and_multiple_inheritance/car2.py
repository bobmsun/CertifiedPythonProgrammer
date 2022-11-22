
# If a class makes sense to be multiple classes, then we can use multiple inheritence

from vehicle2 import Vehicle

class Car(Vehicle):  

    default_tire = 'tire'

    def __init__(self, engine, tires=None, distance_traveled=0, unit='miles'):
        # print("car constructor")
        super().__init__(distance_traveled=distance_traveled, unit=unit)         # 相比 car.py 改动是这里用了 keywork argument
        if not tires:
            tires = [self.default_tire, self.default_tire, self.default_tire, self.default_tire]
        self.tires = tires
        self.engine = engine
    
    def drive(self, distance):
        self.distance_traveled += distance


