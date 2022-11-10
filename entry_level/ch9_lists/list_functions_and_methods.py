
# This section we will take a look at some of the functions and methods that list has access to

my_list = [1, 2, 3]

# If we want to add things to the list, we can do the += operation, or we can modify the list inplace by using the append() method
print(id(my_list))
my_list.append(4)    # it's gonna put it to the very end of the list
print(my_list)        # [1, 2, 3, 4]
print(id(my_list))     # (same id)

# If we want to add something somewhere else within the list, we have to use the "insert" function
my_list.insert(0, 'a')
print(my_list)             # ['a', 1, 2, 3, 4]

# If we want to know the actual position of an item, we can use the "index" function
my_list = [1, 2, 3]
print(my_list.index(2))       # 1
# 如果对 index() function pass in 一个 list 中 不包含的 element，会报错
# print(my_list.index(15))      ValueError: 15 is not in list
# Because above can raise an error, so there are other operations that can help us determine if we will run into the above situation
# That is the "in" and "not in" operation

my_list = [1, 2, 3]
print(4 in my_list)          # False
print(4 not in my_list)      # True
print(2 in my_list)          # True
# "in" works for most sequence types here
# check 是否 in 之后，就可以知道是否可以调用 index() function 了


# Sorting
my_list = [1, 3, 4, 8, 2]
print(id(my_list))
print(sorted(my_list))      # it's gonna reture a NEW list
my_list2 = sorted(my_list)
print(id(my_list2))         # 不同于上面的 id

# reverse a list
print(reversed(my_list))      # it will return a reverse iterator object, so we have to convert it to a list
# The reversed function doesn't return a list, but typecasting works for the list type also, and when we have a list iterator we can turn it back into a list using the list function:
print( list(reversed(my_list)) )     # [2, 8, 4, 3, 1]


# 结合上面所学，sort in descending order
print( list(reversed(sorted(my_list))) )


# To use "sorted" and "reversed", these are functions that require the internal items to be comparable. 
# Otherwise it gonna eventually run into an Error


