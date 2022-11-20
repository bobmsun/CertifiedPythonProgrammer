class ExampleError(Exception):
    def __init__(self, *args):
        self.args = args
    pass

def bad_function():
    raise ExampleError("this is a message", 1, 2)

try:
    bad_function()
except ExampleError as err:
    message, x, y = err.args
    print(message)            # this is a message
    print(x)                  # 1
    print(y)                  # 2
    print(err.args)           # ('this is a message', 1, 2)
    print( dir(err) )         

    message, x, y, *other = err.args
    print(message)            # this is a message
    print(x + y)              # 3
    print(other)              # []

    message, *other = err.args
    print(message)            # this is a message
    print(x + y)              # 3
    print(other)              # [1, 2]
