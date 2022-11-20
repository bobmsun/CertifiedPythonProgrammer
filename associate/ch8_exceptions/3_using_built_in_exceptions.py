

# 我们已经知道了 how to handle exceptions, but occassionally in our code, we want to raise exception

# First, let's take a look at what exceptions look like
err = Exception('something went wrong')    # just pass in the message as parameter when you're creating the exception
print( str(err) )            # something went wrong

print( dir(err) )

# Need to know what kind of exception we have at disposal within the system.
print( Exception.__subclasses__() )
# [<class 'TypeError'>, <class 'StopAsyncIteration'>, <class 'StopIteration'>, <class 'ImportError'>, <class 'OSError'>, 
# <class 'EOFError'>, <class 'RuntimeError'>, <class 'NameError'>, <class 'AttributeError'>, <class 'SyntaxError'>, 
# <class 'LookupError'>, <class 'ValueError'>, <class 'AssertionError'>, <class 'ArithmeticError'>, <class 'SystemError'>, 
# <class 'ReferenceError'>, <class 'MemoryError'>, <class 'BufferError'>, <class 'Warning'>, <class 'locale.Error'>, 
# <class 'warnings._OptionError'>]

# 可能会发现 IndexError is not here

print( IndexError.__bases__ )          # (<class 'LookupError'>,)
# IndexError is a LookupError, LookupError 是 parent class

# There is a big hierarchy of Exception

# Now let's go about raising an exception

import sys

if len(sys.argv) < 2:
    raise Exception('not enough arguments')

name = sys.argv[1]
print(f"Name is {name}")



