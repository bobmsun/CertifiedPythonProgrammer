
# Object: an entity that encapsulate some data and some functionality
# 目前为止见过最多的 object: string type (str)

my_str = "Test String"

print( dir(my_str) )   # if you want to know the attributes and what function you can call, you can use the built-in dir function
# 对于 dir function, you can basically pass in anything

print(my_str.__doc__)
# str(object='') -> str
# str(bytes_or_buffer[, encoding[, errors]]) -> str
# 
# Create a new string object from the given object. If encoding or
# errors is specified, then the object must expose a data buffer
# that will be decoded using the given encoding and error handler.
# Otherwise, returns the result of object.__str__() (if defined)
# or repr(object).
# encoding defaults to sys.getdefaultencoding().
# errors defaults to 'strict'.


print(my_str.isdigit())    # False


# Modules can also be object
import sys
print( type(sys) )     # <class 'module'>

print( type(str) )     # <class 'type'>

