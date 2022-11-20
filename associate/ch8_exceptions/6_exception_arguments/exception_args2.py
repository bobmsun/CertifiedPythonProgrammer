class ExampleError(Exception):
    def __init__(self, *args):
        self.args = args
    pass

def bad_function():
    raise ExampleError("this is a message", 1, 2, "boom")

try:
    bad_function()
except ExampleError as err:
    message, x, y, *other = err.args
    print(message)            # this is a message
    print(x + y)              # 3
    print(other)              # ['boom']


# Exceptions are just classes
