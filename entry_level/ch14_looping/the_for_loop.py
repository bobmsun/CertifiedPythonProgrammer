
# for TEMP_VARIABLE in SEQUENCE: # could be list, tuple, string
#     pass


# Can iterate a list
colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    print(color)


# Can iterate a tuple
point = (1, 2, 3)
for value in point:
    print(value)
# 1
# 2
# 3


# Can iterate a dictionary
ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
for key in ages:
    print(key)
# When iterating a dictionary, by default, we get the keys
# kevin
# bob
# kayla

# Recall Dictionary 那章：
ages = {'kevin': 61, 'bob': 79 }
print( ages.items() )        # a list of tuples            dict_items([('kevin', 61), ('bob', 79)])
print( list(ages.items()) )    # [('kevin', 61), ('bob', 79)]



# If you want to iterate over both the key and the value, you can do this. It's going to unpack that.
# It's unpacked in the same way as we unpack key, value = (a tuple of two items)
for key, value in ages.items():
    print(key, value)
# kevin 59
# bob 40
# kayla 21


# Can also iterate a string
for letter in 'my_string':
    print(letter)
# m
# y
# _
# s
# t
# r
# i
# n
# g


