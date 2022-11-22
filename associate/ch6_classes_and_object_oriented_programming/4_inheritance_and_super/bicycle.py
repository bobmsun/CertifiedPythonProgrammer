
from vehicle import Vehicle

class Bicycle(Vehicle):  # 括号中 specify the type we are gonna inherit from
    # pass
    # 此时 we created a class that works exactly like Vehicle, but it just has the name Bicycle
    # 这时候 run:
    # python -i bicycle.py
    # bike = Bicycle()
    # 会出 error：
    # Traceback (most recent call last):
    #    File "<stdin>", line 1, in <module>
    # TypeError: __init__() missing 2 required positional arguments: 'engine' and 'tires'
    # 因为 we inherit all the functionality that are present on Vehicle

    def __init__(self, tires=None):
        if not tires:
            tires = [self.default_tire, self.default_tire]
        self.tires = tires
    
# python -i bicycle.py
# bike = Bicycle()
# bike.tires               # ['tires', 'tires']
# bike.engine              # AttributeError: 'Bicycle' object has no attribute 'engine'      因为我们上面 customize 了 __init__ ，所以就没有了 engine attached to the object
# bike.description()       # description() function 有，也可以被 call，但是会 throw  AttributeError: 'Bicycle' object has no attribute 'engine'





