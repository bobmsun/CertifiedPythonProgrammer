
from vehicle2 import Vehicle

class Bicycle(Vehicle):  

    default_tire = 'tire'              # Moved this tire thing from Vehicle to Bicycle

    def __init__(self, tires=None, distance_traveled=0, unit='miles'):
        # I'm overriding __init__, but I still need to invoke what happens in my parent class's version of __init__
        # supper gives us the ability to call the pre-existing implementation so that, 当我们 defining our own 的时候，we are not
        # completely wiping out the pre-existing one
        # We still want the work defined in Vehicle to happend, we just add a little bit extra work below
        super().__init__(distance_traveled, unit)
        # supper() means call the parent class's implementation of whatever the next method is

        if not tires:
            tires = [self.default_tire, self.default_tire]
        self.tires = tires
    
    # 这时：
    # python -i bicycle2.py 
    # bike = Bicycle()
    # bike.tires                  # ['tire', 'tire']
    # bike.description()          # A Bicycle that has traveled 0 miles
    
    # Now let's customize description() a little bit just to practice using super
    def description(self):
        initial = super().description()          # This is the initial message
        return f"{initial} on {len(self.tires)} tires."


if __name__ == "__main__":
    bike = Bicycle()
    print(bike.description())              # A Bicycle that has traveled 0 miles on 2 tires.




