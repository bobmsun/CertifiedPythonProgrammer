
# 如果没有 name mangling 会怎么办？

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.update(iterable)
    
    def update(self, iterable):
        print("original update")
        for item in iterable:
            self.item_list.append(item)
    

class MappingSubclass(Mapping):
    def update(self, keys, values):          # 注意：这里的 subclass 中 override 了 update，但却没有 override __init__
        print("update in subclass")
        for item in zip(keys, values):
            self.item_list.append(item)


# python -i mapping2.py 

# >>> mapping = MappingSubclass([], [])
# TypeError: __init__() takes 2 positional arguments but 3 were given

# >>> mapping = MappingSubclass([])
# TypeError: update() missing 1 required positional argument: 'values'

