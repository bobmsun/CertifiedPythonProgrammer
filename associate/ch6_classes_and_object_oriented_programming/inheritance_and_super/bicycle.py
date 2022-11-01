
from vehicle import Vehicle

class Bicycle(Vehicle):
    # pass
    # 这时候 run:
    # python -i bicycle.py
    # bike = Bicycle()
    # 会出 error：
    # Traceback (most recent call last):
    #    File "<stdin>", line 1, in <module>
    # TypeError: __init__() missing 2 required positional arguments: 'engine' and 'tires'

    def __init__(self, tires=None):
        if not tires:
            tires = [self.default_tire, self.default_tire]
        self.tires = tires
    
# python -i bicycle.py
# bike = Bicycle()
# bike.engine           error
# bike.description()    error



