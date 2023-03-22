
# Modeling Vehicles (design a blueprint for a type of concept)
# Defining a type
class Vehicle:
    """
    Vehicle is a type that describes a machine that helpes us travel. (This is the docstring)
    """

    # This function is how we customize the creation of an object
    # You will see "self" all the time in object-oriented code. That's because,
    # from inside of the function, self is going to represent the instance that we are working with
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
# civic = Vehicle('4-cyclinder', ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'])         # we don't pass in self, self is passed in implicitly
# civic                            # <__main__.Vehicle object at 0x7fe42b3bef28>
# type(civic)                      # <class '__main__.Vehicle'>
# civic.engine                     # '4-cyclinder'
# civic.tires                      # ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger']
# civic.description                # <bound method Vehicle.description of <__main__.Vehicle object at 0x7fe42b3bef28>>
# civic.description()              # 打印：A vehicle with an 4-cyclinder engine, and ['front-driver', 'front-passenger', 'rear-driver', 'rear-passenger'] tires
# civic.serial_number = '1234'     # it has engine and tires, you can also attach more things
# civic.serial_number

# 如何理解加的这个 serial_number
# So it provides us with a namespace to attach any number of variables that we want.
# And when a variable is attached to an object there.
# It's normally referred to as an attribute of the object.
# So this is how you can add more attributes to an individual instance that isn't described by the class,
# which is NOT necessarily all that useful.

# dir(civic)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'description', 'engine', 'serial_number', 'tires']

# del civic.serial_number
# civic.serial_number                # AttributeError: 'Vehicle' object has no attribute 'serial_number'

# del civic
# civic                              # NameError: name 'civic' is not defined

