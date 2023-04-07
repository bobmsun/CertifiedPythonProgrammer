
# Another type of sequence in Python. But less used.

# Tuple is an immutable sequence type so it has a fixed length
point = (2.0, 3.0)

print(point[0])     # 2.0

# 自我补充: tuple is immutable
print(id(point))
point2 = (2.0, 3.0)
print(id(point2))       # (same is as above, 因为 tuple 是 immutable 的)


# we can never modify a tuple
# point[0] = 1      # TypeError: 'tuple' object does not support item assignment
# Because tuple is an immutable type

# We still have operations that we would have with strings that would return a new tuple
point_3d = point + (4.0,)           # To state (4.0) is a tuple, we have to add a comma; otherwise it will 认为它是一个 math operation
print(point_3d)      # (2.0, 3.0, 4.0)


# You unpack it into separate variables
x, y, z = point_3d
print(x)         # 2.0
print(y)         # 3.0
print(z)         # 4.0
# You can do this with lists, but it's less common.
list1 = ['hello', 'hi', 'hey']
a, b, c = list1
print(a)         # hello
print(b)         # hi
print(c)         # hey


# If you have something what you will potentially put into a list and you know it's never going to change size and it always going to be a specific size,
# then tuples is a really good way of doing that, because then you know it's safe from being modified.


# format string
# 以下这种语法是 Python 2 的
print("My name is: %s %s" % ("keith", "Thompson"))   # it will unpack the tuple and 放到 string 当中
# If you look at some Python2 source code, you will very commonly see this


# 自己加：tuple 也可以 slice，like a list
# a = (1, 2, 3, 4)
# print( a[1:3] )      # (2, 3)
