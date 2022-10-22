

ages = { 'kevin': 59, 'alex': 29, 'bob': 40 }
print(ages)             # {'kevin': 59, 'alex': 29, 'bob': 40}
# As of Python 3.7, the key will guarantee to stay in order (自悟：define 的时候什么 order，print 出来就是什么order)

# ordered version of the dictionary: ordered_dict   -> ordered dictionary

# keys need to be immutable type (they don't have to be string, but must be a immutable type)
# keys have to be unique

# read values
print(ages['kevin'])      # 59
# print(ages['billy'])    # KeyError: 'billy'

# dictonaries themselves are mutable type, so you can add things to it
ages['kayla'] = 21
print(ages)         # {'kevin': 59, 'alex': 29, 'bob': 40, 'kayla': 21}


# We can also reassign values
ages['kevin'] = 60    
print(ages)         # {'kevin': 60, 'alex': 29, 'bob': 40, 'kayla': 21}

# If fthe key that you are setting does not exist in the dictionary, it will add it and set the value.
# If it does exists, then it's just going to reset the value.

# remove
del ages['kevin']
print(ages)          # {'alex': 29, 'bob': 40, 'kayla': 21}

# del ages -> will remove the variable entirely

# With dictionary, we still have the "in" and "not in" operations that we have with lists
print('kevin' in ages)   # False
print('alex' in ages)    # True
# For list it ("in" / "not in") will look by value. For dictionary, it's going to look by key



# Different ways you can create dictionary (not super common)
weights = dict(kevin=160, bob=240, kayla=135)       # it will just turn kevin into string
print(weights)             # {'kevin': 160, 'bob': 240, 'kayla': 135}


# Another way we can create dictionary is by using tuple (you can pass in a list of tuples where the first item is the key and second item is value)
colors = dict([('kevin', 'blue'), ('bob', 'green'), ('kayla', 'red')])   
# This dict() function knows that if it gets a list of tuples, it will break apart each of these tuples into keys and values, 
# and add them to the dictionary you created.
print(colors)             # {'kevin': 'blue', 'bob': 'green', 'kayla': 'red'}



