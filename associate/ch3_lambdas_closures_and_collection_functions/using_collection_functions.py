
# 这节课在于展示 when Lambda will be useful, 通过 collection function 来展示：
# 有一些 collection functions 是之前讲过的: reversed, sorted 
# 也有一些是新的：map, filter, and reduce

# All these functions are kind of special, because they're what are known as "higher order function": a function
# that can take in another function as an argument or return a function as a return value
# 目前先不管 functions that return a function

# map
# f(x) = x + 1
# Domain: [1, 2, 3]
# Range: [2, 3, 4]
# We can give "map" function a function and a collection and we can map that function over that collection

domain = [1, 2, 3, 4, 5]
# f(x) = x * 2
# 当我们 pass 一个 function 给 map function 时，it's gonna be the function without calling it. So 这时我们就可以用 lambda
our_range = map(lambda num: num * 2, domain)
print(list(our_range))     # [2, 4, 6, 8]  # need to conver our_range into a list, otherwise it's a map object
print(our_range)         # <map object at 0x7fd2d72546a0>
# 对于 map function 来说，the result is always going to have the same length as the input

# map allows us to do something that 可能需要 a for loop （or you can use list comprehension)


# 自己加：map 不一定非要take lambda function，也可以 take 一般的非 lambda 函数
def square(num):
    return num * num
our_range_square = map(square, domain)     
print(list(our_range_square))       # [1, 4, 9, 16, 25]







# filter
# filter(first parament is a callable(a funtion), for second parameter it asks for a iterable)
evens = filter(lambda num: num % 2 == 0, domain)
# for filter function, the lambda needs to return a true/false value. If the value is true, then the particular item that we are currently working with 
# as we are iterating our list is going to be kept and put into the final list that gonna be returned back to us.
# if it does not meet the criteria, it will not make to the final result
print(list(evens))       #  [2, 4]
print(evens)       # it's gonna give you a filter object   <filter object at 0x7fd2d73c6ba8>





# reduce
# reduce 比 map and filter 有一点点 complicated, because it doesn't just take one argument
# reduce takes a iterable. it's gonna iterate over it and each time we are going to be modifying an accumulater so that
# at the end we get one final result
# So reduce 干的事是：we are reducing an iterable down into one thing
# For example, calculating the sum of numbers in a list

# I'm going to say it's not used commonly enough to where they moved it out of
# being a built-in function, and it actually is in a different module now.
from functools import reduce
the_sum = reduce(lambda acc, num: acc + num, domain, 0)
# here lambda takes 2 paramters, whatever returned by lambda function is gonna become the accumulator value for the next iteration
# The third argument is the initial accumulator value
# So reduce takes (a function, a iterable, a starting point of the cummulator) 
print(the_sum)       # 15
# 自己加的：
print( sum(domain) )      # 15

# reduce 比 map 和 filter 有一点 complecated 的 点在于: we have to consider the state of each iteration

# 自己加的：
a_string = reduce(lambda string, letter: string + letter, ['a', 'b', 'c', 'd'], '')
print(a_string)           # abcd







# sorted & reversed  (we have seen they work with list before)
# 这两个 function 可以 take 一个 parameter, parameter 名叫 key (这个命名很 bad) --- you can pass in a function that you can process each individual item 
# before it's compared
words = ['Boss', 'a', 'Alfrad', 'fig', 'Daemon', 'dig']
print("Sorting by default") 
print(sorted(words))   # ['Alfrad', 'Boss', 'Daemon', 'a', 'dig', 'fig']
# 用 sorted function 来 sort a list of string 不能把list sorted alphebatically, because capital values and lower case values have different ordinal values,
# they compared differently


print("Sorting with a lambda key")
print(sorted(words, key=lambda s: s.lower()))   # ['a', 'Alfrad', 'Boss', 'Daemon', 'dig', 'fig']
# It is saying: This is what the comparison value should be s.lower(), and it will factor that in (Let's make the comparisons on the lower case strings)
# It's not changing the values inside words, but changing the value you're comparing with
# This will return a NEW list that is actually sorted

# the "list" type has a sort function that will go and change the list itself (lists are mutable, so we can make modifications to them, 
# we can change the value of our variable by calling methods on the object)

print("Sorting with a method")
words.sort()
print(words)     # ['Alfrad', 'Boss', 'Daemon', 'a', 'dig', 'fig']

# list type 的 sort function 也有一个叫 key 的 parameter，you can pass in a function (it doesn't have to be lambda)
# Remember, 对于一个 function 来说，if you 不加括号（不 call）, it will always represent itself
# In Python, you are able to pass functions around as objects.

# 下面的例子 is：not working with lambda but still working with the "key" paramter
words.sort(key=str.lower, reverse=True)    # we will throw our string into the function
                                           # reverse=True will reverse the order， kind of combining sorted and reverse

# For string, the type will be str

# "my_sting".lower()     (calling lower on "my_string")  和
# str.lower("my_string") 
# work exactly the same way
print(str.lower("ABC"))         # abc

print(words)       # ['fig', 'dig', 'Daemon', 'Boss', 'Alfrad', 'a']


# sort vs sorted 的区别
# sorted([a list])   vs     [a list].sort()
# sorted is going to create a new list and return it
# sort is going to change the list that you're calling it on


