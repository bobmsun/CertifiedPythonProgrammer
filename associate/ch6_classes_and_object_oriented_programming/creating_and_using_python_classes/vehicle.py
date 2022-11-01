
# Modeling Vehicles (design a blueprint for a type of concept)

class Vehicle:
    """
    Vehicle is a type that describes a machine that helpes us travel.
    """

    # This function is how we customize the creation of an object
    # From inside of the function, self is going to represent the instance that we are working with
    # def __init__(self):
    #     """
    #     Customizes the initializetion of the object
    #     """
    #     pass

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires 


    # This is going to be an instance method, which means you call it on an instance, not on the class itself -> 所以就要在 parameter list 中加 self
    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")



# python -i vehicle.py
# civic = Vehicle('3-cyclinder', ['front-deriver', 'front-passenger', 'rear-driver', 'rear-passenger'])
# civic
# type(civic)
# civic.engine
# civic.tires
# civic.description()
# civic.serial_number = '1234'     # it has engine and tires, you can also attach more things
# civic.serial_number

# 如何理解加的这个 serial_number
# So it provides us with a namespace to attach any number of variables that we want.
# And when a variable is attached to an object there.
# It's normally referred to as an attribute of the object.
# So this is how you can add more attributes to an individual instance that isn't described by the class,
# which is NOT necessarily all that useful.

# dir(civic)
# del civic.serial_number
# civic.serial_number





