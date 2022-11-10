

ages = {'kevin': 61, 'bob': 79 }

# You can get all of the keys in the dictionary by using the keys() method
print(ages.keys())   # dict_keys(['kevin', 'bob']) 
# it's going to return us a dict key object that is a list of the keys

print( list(ages.keys()) )   # need to maually cast it into a list      ['kevin', 'bob']

print( ages.values() )       # a list of values            dict_values([61, 79])


print( ages.items() )        # a list of tuples            dict_items([('kevin', 61), ('bob', 79)])
print( list(ages.items()) )    # [('kevin', 61), ('bob', 79)]


