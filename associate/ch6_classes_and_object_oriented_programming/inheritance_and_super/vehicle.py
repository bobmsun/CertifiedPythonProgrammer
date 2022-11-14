

# Inheritance allows us to define a type and then we can define a more specific type that shares functionality that parent type. 
# So we base a type off an existing type so that we don't have to redo that work and define those things additionally.

class Vehicle:
    """
    Vehicle is a type that describes a machine that helpes us travel. (This is a docstring)
    """

    class_variable = "Keith"
    default_tire = 'tires'

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires

    # @classmethod
    # def bicycle(cls, tires=None):
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None, tires)
    
    
    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")
    
