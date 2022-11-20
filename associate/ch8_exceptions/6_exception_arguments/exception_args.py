class ExampleError(Exception):
#     def __init__(self, *args):        ######
#         self.args = args
    pass

def bad_function():
    raise ExampleError("this is a message", 1, 2)      # we can pass in any number of arguments

try:
    bad_function()
except ExampleError as err:        
    message, x, y = err.args   # All the argument that have ever passed in are going to be stored as args, 因为 ##### is basically how it was defined
    print(message)            # this is a message
    print(x)                  # 1
    print(y)                  # 2
    print(err.args)           # ('this is a message', 1, 2)
    print( dir(err) )         

    message, x, y, *other = err.args   # 如果有多个 arguments 但只 care 前三个，可以这样写
    print(message)            # this is a message
    print(x + y)              # 3
    print(other)              # []

    message3, x3 = err.args       # 这一行会出 error   ValueError: too many values to unpack (expected 2)  所以如果有多个 arguments 但只 care 前三个，应该按上例那样写
    print(message3)
    print(x3)

# 自己加： *args vs **kwargs
# https://www.programiz.com/python-programming/args-and-kwargs

