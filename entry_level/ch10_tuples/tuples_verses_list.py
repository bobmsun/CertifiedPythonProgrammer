
# When we should use tuple vs. when we should use list

# 就问自己一个问题：Will we ever not know how many items we are storing?
# If the answer is Yes, then you always need a list. 
# Tuple will not be good to use because tuple cannot be changing their sizes   vs.    List can be any length


# Tuples make more sense in two general situations:

# 1. When we're trying to return more than one piece of information from a function. In this case, you can use tuple so that you can use unpacking.
# 2. I want to model something that I know it has a specific field or a certain number of those fields so I can just put them in order in a tuple.
# This would be something like a point in 2D or 3D space having x, y, and potentially z. Those values should always be in a specific spot.

person = ('Kevin Bacon', 61, '555-555-5555')
person2 = ('Bob Ross', 76, '')

print(person[0])         # Kevin Bacon
print(person2[0])        # Bob Ross

# what happen if we combine list and tuple together
my_list = [1, 2, 3]
my_tuple = (my_list, 1)
print(my_tuple)          # ([1, 2, 3], 1)
other_list = [1, 2, my_tuple]
print(other_list)        # [1, 2, ([1, 2, 3], 1)]

# Even though we cannot change the tuple itself, we can change the thing that it is pointing at, in this cast, the list
my_list.append(1)
print(my_tuple)
print(other_list)      # that also picked up the change




