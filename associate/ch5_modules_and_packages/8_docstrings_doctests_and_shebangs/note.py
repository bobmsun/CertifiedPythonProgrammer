"""
Helpers is a package that provides easy to use helper functions and variables.

This is a docstring. It's NOT a doc comment. This is not a comment because the interpreter actually has to do something with it.

Docstrings are triple-quoted strings that we put at the top of modules, packages, inside of functions, or inside of class.
"""

# import helpers
# helpers.__doc__      会打印出
# 'Helpers is a package that provides easy to use helper functions and variables.'
# The triple-quoted string at the top of the __init__.py file inside our package. That is set to be the documentation of this package as a whole.
# And we can do the exactly same thing at the top of the module or at the top of a function.


def extract_upper(phrase):
    """
    extract_upper takes a string and return a list containingonly the uppercase characters from the string.
    >>> extract_upper("Hello There, BOB")
    ['H', 'T', 'B', 'O', '']
    """
    return list(filter(str.isupper, phrase))

# This is what is known as a doctest.
# It will ensure the next line is what the code returned if it's executed. And if it's not, it will give you an Error.
# So we can have automated test to make sure our documentation is up to date.
# You can run it by running: 
# python -m doctest note.py
# or
# python -m doctest note.py --verbose




# Shebang
# python main.py      有点麻烦
#!/usr/bin/env/ python
# use
# chmod +x main.py
# to make our file executable
