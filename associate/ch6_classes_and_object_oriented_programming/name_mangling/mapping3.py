
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
    
    def print_something(self):
        print("Print something")
    
    __update = print_something           # ??????



# python -i mapping3.py 

# >>> mapping = MappingSubclass([])
# original update

# >>> Mapping.__update
# AttributeError: type object 'Mapping' has no attribute '__update'

# 用 dir() to see all the attributes and methods that are defined

# >>> dir(Mapping)
# ['_Mapping__update', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'update']

# 以上的 _Mapping__update 就是 name mangling at its core:
# If you follow some very specific rule about how you name an identifier, spcifically it has 2 understores at the beginning (at least 2) and it 
# can only ever have at most one trailing understore, then Python interpretor will mangle that, so that it has a very specific version that is 
# held on the class (_Mapping__update) that is supper unlikely for something to override.


# >>> dir(MappingSubclass)
# ['_MappingSubclass__update', '_Mapping__update', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', 
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'print_something', 'update']

# 注意：MappingSubclass 中有：'_MappingSubclass__update', '_Mapping__update'
# 有 Mapping version of the update, 也有 MappingSubclass version of the update

# All you need to know with name mangling
# is that it will take these special variables
# that you create, or identifiers really
# that are __something,
# and then at most, 1 trailing underscore
# that you define in your classes.
# And when it's all said and done at the end,
# those will be accessible externally through a special name
# that has a prefixed underscore name of the class.

