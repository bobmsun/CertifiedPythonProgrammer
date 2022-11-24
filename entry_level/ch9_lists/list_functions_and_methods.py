
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

# 自己加：如果有多个满足条件元素，返回第一个的 index
my_list = [1, 2, 3, 2, 2]
print(my_list.index(2))      # 1





# 判断是否在 list 中
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
print(my_list)      # [1, 3, 4, 8, 2]     my_list 本身并没有改变，sorted() 函数并不是 sort in place，而是生成了新的 list

print(id(my_list))
my_list.sort()
print(my_list)      # [1, 2, 3, 4, 8]
print(id(my_list))      # 和上面的 id 相同

# 想 sort list 有两种方法：
# 用 built-in function: sorted()
# call list 的 sort() function
# 区别在于 sort() 是 in-place sort 的，没有新的 list 生成；而 sorted() 不是 in place 的，生成了新的 list





my_list = [1, 3, 4, 8, 2]
# reverse a list
print(reversed(my_list))      # it will return a reverse iterator object, so we have to convert it to a list
# The reversed function doesn't return a list, but typecasting works for the list type also, and when we have a list iterator we can turn it back into a list using the list function:
print( list(reversed(my_list)) )     # [2, 8, 4, 3, 1]

print(my_list)     # [1, 3, 4, 8, 2]           # reversed 不是 inplaced 的，就像 sorted 也不是 inplaced 的

# 结合上面所学，sort in descending order
print( list(reversed(sorted(my_list))) )       # [8, 4, 3, 2, 1]


# To use "sorted" and "reversed", these are functions that require the internal items to be comparable. 
# Otherwise it gonna eventually run into an Error


# 自己加：remove element from a list
# 法一：用 remove function
names = ['Alice', 'Bob', 'Lance', 'Mike']
names.remove('Bob')
print(names)             # ['Alice', 'Lance', 'Mike']       # 自悟：remove 函数是 inplace 的

# 如果有多个元素，remove 函数只会 remove first occurance 
numbers = [1, 2, 3, 3, 2]
numbers.remove(2)
print(numbers)           # [1, 3, 3, 2]

# 法二：通过 slicing 来 remove
names = ['Alice', 'Bob', 'Lance', 'Mike']
names[1:2] = []
print(names)             # ['Alice', 'Lance', 'Mike']






# 自己根据之后模拟考试，加的 join 函数：
names = ['Alice', 'Bob', 'Hillary', 'Elizabeth']
print( ' '.join(names) )     # Alice Bob Hillary Elizabeth

numbers = [1, 2, 3, 3, 2]
print( ' '.join(numbers) )    # TypeError: sequence item 0: expected str instance, int found
