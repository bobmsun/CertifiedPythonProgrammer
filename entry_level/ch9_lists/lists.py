
# Collection of items
# First collection we take a look - list

my_list = [1, 2, 3, 4, 5]
print(my_list)

# The items within list do NOT all have to have the same type
other_list = ['a', 1, 1.0, False]
print(other_list)


# Indexing operation
print(my_list[0])    # 1
print(my_list[2])    # 3

# print(my_list[6])    IndexError: list index out of range

# Get length
print(len(my_list))   # 5


# Slicing: get a subsection of the list
# When we slice a string, we get a string back
# When we slice a list, we get a list back


print(my_list[0:2])   # [1, 2]
print(my_list[1:])    # [2, 3, 4, 5]
print(my_list[:3])    # [1, 2, 3]

# Stepping also works
print(my_list[0::1])   # [1, 2, 3, 4, 5]
print(my_list[0::2])   # [1, 3, 5]


# List is the first mutable type we've ever worked with
print(id(my_list))
my_list[0] = 'a'
print(my_list)     # modify the list in place    这里是 mutability 的体现
print(id(my_list))

print(my_list + [8, 9, 10])     # here is going to return a new list

print(id(my_list))
my_list += [8, 9, 10]
print(my_list)         # 这里就与 mutability 无关了  <-  这里讲错了，因为下面的地址依旧会是相同的
print(id(my_list))

# 也可以通过 slices 来 reassign 值
print(id(my_list))
my_list[1:3] = ['b', 'c']   
print(my_list)              # ['a', 'b', 'c', 4, 5, 8, 9, 10]
print(id(my_list))          # (same id) 

# They don't have to have the same size
my_list[3:5] = ['d', 'e', 'f']      # size 不 match 也没关系，the list just grow in size
print(my_list)              #  ['a', 'b', 'c', 'd', 'e', 'f', 8, 9, 10]
print(id(my_list))          # (same id) 


# 也可以通过 slice 来 remove element in the array
my_list = ['a', 'b', 'c', 'd', 5, 6, 7]
print(id(my_list))       # 这里换了新 id

my_list[4:] = []
print(my_list)
print(id(my_list))      # (same id)


# The more common way to remove element is by using the del statement
# del is a statement, it's different from a function
del my_list[0]       # remove the first element in the array,    del will NOT return the element it deletes
print(my_list[0])

del my_list          # 用 del 会有些 risky，如果 del 后面不加 index，就会 completely remove the list completely
print(my_list)       # NameError: name 'my_list' is not defined



