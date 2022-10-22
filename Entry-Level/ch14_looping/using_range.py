

# we can use the range function to create a range

my_range = range(10)    # start, end, step

print( list(my_range) )
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# If we have the range list out as a list, it's gonna fit into the memory one time. 
# But the way that range works is that, each individual item inside the sequence is calculated when it's needed
# So range takes a very small amount of space. They are very lightweighted.
# And it allows us to work with very big sequences without needing to specify something gigantic

print( list(range(1, 14, 2)) )    # exactly the same way when we work with slicing - start, end (exclusive), step
# [1, 3, 5, 7, 9, 11, 13]

count = 1
while count <= 4:
    print("looping")
    count += 1
# looping
# looping
# looping
# looping



for _ in range(4):      # we don't need this temp variable.   _   this is saying I don't need this variable
    print("looping")
# looping
# looping
# looping
# looping


# Using range is a easy way to create a list that don't take a large amount of space and might have many many items in them.

