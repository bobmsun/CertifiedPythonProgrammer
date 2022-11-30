
# modules in Python are just files

# It's gonna return a list that are all upper case letters
# Phrase can be a string. String is an iterable (iterable 就是 something you can do a for loop over)
def extract_upper(phrase):
    return list(filter(str.isupper, phrase))    # whenever the character is upper case, then we are gonna return that 
# So the function will take a string and return a list of only upper characters inside of that


def extract_lower(phrase):
    return list(filter(str.islower, phrase))

# 以上这个 file 就是 一个 module 了，create a module 就是这样 simple，就是 create a python file and put python in it

# Modules can define more than functions. As we get further along, we can define classes to create our own types so that we can model data

# Anything we can give a name is something that can then be pulled in by something accessing this module. 
# Functions have name. Other things that have name are variables.



# 自己补充（网上查的）
# In Python, Modules are simply files with the “. py” extension containing Python code that can be imported inside another Python Program. 
# In simple terms, we can consider a module to be the same as a code library or a file that contains a set of functions that 
# you want to include in your application.
