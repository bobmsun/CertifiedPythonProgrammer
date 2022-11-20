
# When something is private to a class, it's only accessible to the instance itself.
# Python doesn't really have this kind of concept, because anything can be explicitly access if you know the name of 
# the attribute you are trying to get.
# You can chain off the object using a period and you can access that attribute.
# But Python does have the feature of name mangling that allows us to protect something that are private to our class
# so that they are never overriden by the exactly same name if we have a subclass.

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)
    
    def update(self, iterable):
        print("original update")
        for item in iterable:
            self.item_list.append(item)
    
    __update = update         # Create a class-level variable that starts with 2 understore. 
                              # This is a private copy of the original update method.


class MappingSubclass(Mapping):
    def update(self, keys, values):
        print("update in subclass")
        for item in zip(keys, values):
            self.item_list.append(item)


# python -i mapping.py 
# >>> mapping = MappingSubclass([])
# original update

# >>> mapping.update([])
# TypeError: update() missing 1 required positional argument: 'values'

# >>> mapping.update([], [])
# update in subclass

# >>> mapping.__update([])
# AttributeError: 'MappingSubclass' object has no attribute '__update'


