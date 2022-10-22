

ages = {'kevin': 61, 'bob': 79 }

# You can all of the keys in the dictionary by using the keys() method
print(ages.keys())   # dict_keys(['kevin', 'bob']) 
# it's going to return us a dict key object that is a list of the keys

print( list(ages.keys()) )   # need to maually cast it into a list

print( ages.values() )       # a list of values


print( ages.items() )        # a list of tuples
print( list(ages.items()) )


