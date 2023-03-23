# zip 函数：
# zip(*iterables)
# iterables can be built-in iterables (like: list, string, dict), or user-defined iterables

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()
result                        # <zip object at 0x7ff61cba5c88>

# Converting iterator to list
result_list = list(result)
print(result_list)            # []

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)             # {(1, 'one'), (2, 'two'), (3, 'three')}
print(list(result))           # [(1, 'one'), (2, 'two'), (3, 'three')]

# 自己加，可以 take 多个 iterable
result = zip(number_list, str_list, (True, False, True, False, True))
print(list(result))           # [(1, 'one', True), (2, 'two', False), (3, 'three', True)]
# Suppose, two iterables are passed to zip(); one iterable containing three and other containing five elements. 
# Then, the returned iterator will contain three tuples. It's because the iterator stops when the shortest iterable is exhausted.

# 自悟：zip 函数就是把每一个 iterable 的 index 0 用一个tuple zip 到一起，每个iterable 的index 1 用一个tuple zip 到一起，每个iterable 的index 2 ....

# 自悟：zip 函数通常用于生成 dictionary 时使用

# Python zip() method takes iterable or containers and returns a single iterator object, having mapped values from all the containers. 
# It is used to map the similar index of multiple containers so that they can be used just using a single entity. 


