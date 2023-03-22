
# 这节课的名字：custom constructors, class methods, and decorators

# 之前讲的是绝大多数情况下 object-oriented programming 中我们做的事：
# We define what the type can do and the information we expect to hold. And we create instances in our code and we use it.
# But sometimes, we want to hold information on the class itself, because classes are also objects. 
# Because it is an object, we can define data on a class

class Vehicle:
    """
    Vehicle is a type that describes a machine that helpes us travel.
    """

    # Because it is an object, we can define data on a class by just defining variables up here. Below are class variables.
    class_variable = "Keith"        # this will be accessible by Vehicle.class_variable
    default_tire = 'tire'

    def __init__(self, engine, tires):
        self.engine = engine
        self.tires = tires
    

    # We can also create functions or methods that are available on the class itself. These are called class methods.
    # You will use these (指 class methods) when you don't need the individual instance information, but you need the overarching
    # information that is held by something like class_variable 

    # So a good example of one reason you might want to do this. It's not something you would do super commonly,
    # and it's something that you might've been used to doing in other languages, maybe if you were working with them,
    # is setting up different constructor methods. So in Python, we only have 1 way to create an instance,
    # and that's by calling this __init__ method. And so we can't describe what that looks like
    # with different parameters, for instance. In other languages, such as Java,
    # you can have multiple constructors where you could have different constructor methods that have different things here.

    # In order to create class method, we need to annotate it with classmethod decorator. (The first implict argument will be the class itself)
    @classmethod
    def bicycle(cls, tires=None):      # cls is going to be implicitly passed in as self was. But rather than being an instance of Vehicle, it's gonna be the class Vehicle itself
        if not tires:    # this is checking if someone calls this function without passing in a tire
            tires = [cls.default_tire, cls.default_tire]
        return cls(None, tires)        # Want to return an instance of class
    # Above defines a class method. It will be accessible by Vehicle.bicycle and you can pass in tires or you won't. 
    # And what will be passed back to you is an instance of a Vehicle that has no engine and has tires. (If it doesn't have tires passed into it,
    # it will create a list that only have the two default tires in it)
    # So this is an alternative way if we wanted to do multiple constructors and have different ways to define an instance of a class. 
    # Then this is one way to do it by defining a class method.

    # There is an alternative to this, and that is if you wanted a function to be attached to your class
    # that didn't need even any class information -- so it didn't need this default_tire -- 
    # you would create what's called a static method, which is just a function that's attached to an object.
    # And to do that, you could do the same thing.
    # You could do @staticmethod, which converts a function to be a static method, and it doesn't receive an implicit first argument,
    # which means it's just a function.
    # It has no access to any state, it's just what comes in and what comes out.
    # So that's something else that I don't believe we need to know for the PCAP, but it's kind of the alternative one.
    # @staticmethod

    def description(self):
        print(f"A vehicle with an {self.engine} engine, and {self.tires} tires")

 
# python -i vehicle.py
# bike = Vehicle.bicycle()
# bike.engine              # Nothing prints out, because it's None
# bike.tires               # ['tire', 'tire']

# bike.default_tire        # 'tire'        # will still get 'tire', because default_tire is a static information that's available to every instance 
                           # 这里想展示的点在于：It is worth talking about these class-level variables are accessible on the instance, by default
# Vehicle.default_tire     # 'tire'

# 自己试了一下：(class variable 可以改)
# Vehicle.default_tire = 'haha'
# a = Vehicle.bicycle()
# a.tires                  # ['haha', 'haha']


# If you want the whole trifecta of things
# that you would do here,
# you have instant methods with self,
# you have class methods with the @ class method
# and the cls implicit argument,
# and then static method,
# which is just basically a function
# that's attached to the object.
# So those are the various things that we can do
# when we're defining methods inside of a class.

# 根据以上，自我总结：
# python 中有 3 中 method：
# instance method: first implicit method: self, call 的时候 instace_name.fucntion_name()
# class method: annotate with @classmethod, first implicit method: cls, call 的时候 class_name.function_name()
# static method: annotate with @staticmethod, no first implicit method, just a function attached to the object
