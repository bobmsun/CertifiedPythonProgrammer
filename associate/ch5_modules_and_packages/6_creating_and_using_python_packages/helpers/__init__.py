# Modules are where the code really lives that we share, but we don't share modules by themselves.
# Packages allow us to bundle up our modules into something we can distribute to others so that they can utilize them

# __init__.py    this is how we distinguish something as being a package
# A package is really a directory that includes an __init__.py inside of it and then, from there, we can create modules within there the same way we did before.


# __init__.py 大多数情况下，it doesn't contain anything, but allow us to specify that it is a package.
# 但是我们也可以 do things inside of here
# This is where we put the initialization code for our package.
# So when we access any module inside of this package, the code inside of this __init__.py file is going to be run first.

__all__ = ['extract_upper']

from .strings import *        # .strings means use the strings module that is part of the current package that I'm in; 
                              # This prevents us from using any sort of global thing by accident.
# This will import the 2 functions that we have in strings. And we are explicitly making one of them available if somebody was to do "from helpers import *"

# Python3.3 之后，如果你的 __init__.py is empty，那么 create package 时可以 没有 这个 file

