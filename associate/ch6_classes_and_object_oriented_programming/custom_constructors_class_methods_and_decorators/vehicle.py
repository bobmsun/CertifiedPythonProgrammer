
# 这节课的名字：custom constructors, class methods, and decorators

class Vehicle:
    """
    Vehicle is a type that describes a machine that helpes us travel.
    """

    class_variable = "Keith"
    default_tire = 'tires'

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    @classmethod
    def bicycle(cls, tires=None):
        if not tires:
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)
    
    
    
    
    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")

 
# python -i vehicle.py
# bike = Vehicle.bicycle([1, 2])
# bike.engine
# bike.tires
# bike.default_tires
