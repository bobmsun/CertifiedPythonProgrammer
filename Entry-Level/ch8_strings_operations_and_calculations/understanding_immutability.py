
# immutability: means something cannot be changed
# mutable: can be changed
my_str = 'testing'
my_str.capitalize()      # this is a new object. it takes up a different spot in memory. We cannot modify object inplace. 
# If we can modify in place, then will be a mutable object

print(my_str.capitalize())      # print: Testing
print(my_str)     # testing

# immutibility 有时能给我们带来一些性能上的优化，因为计算机不用去 check 内容是否被改变了，如果是 immutable 的，计算机就知道了 it will never be changed

# Let's test to see string is immutable by looking at the id
print(id(my_str))

# In Python, every single unique stirng that you can create. Once it's created, that's the only one of that exact string that will ever be created.
print(id('testing'))    # this will be the same id even though this is a literal made separately
other_str = 'testing'
print(id(other_str))   # Still the same id
print( id(my_str) == id(other_str) )

# Python knows we will only need to make one of those, because strings are immutable. So it will look at the same spot of memory.



