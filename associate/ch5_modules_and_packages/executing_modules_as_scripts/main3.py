from helpers3 import *
import extras3


print(f"Lowercase Letters: {extract_lower(extras3.name)}")
print(f"Uppercase Letters: {extract_upper(extras3.name)}")


# Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
# Uppercase Letters: ['K', 'T']

# 这时就 不会 打印出这行了：print("HELLO FROM HELPERS"), which is exactly what we want
# But if we were to run helper3.py, we will see "HELLO FROM HELPERS" printed out.

# If you want to run a module, not a file, you can use the -m flag
# python -m helpers3     (注意：这里需要用 module name 而不是 file name，所以 没有 .py)
# 会 print out "HELLO FROM HELPERS"
# There might be things in the standard library that you might import that actually have a scriptable portion to them


# But just to recap what we covered here,
# we wanted to take a look at what happens when you import something.
# And what we learned was when something is imported,
# everything inside that file is going to be run through the interpreter and executed.
# And that means if you have an expression that prints out to the screen,
# it's going to do that,
# but it'll only do it the first time that that module is imported during
# the interpreter's life cycle. So,
# if you're running a script and multiple things import the exact same module,
# it doesn't matter. Only the first time it's run will that actually be executed.
# So that's one thing we learned. We learned about the double underscore name,
# double underscore variable,
# and the double underscore main value that you'll have when it
# is actually the file that is being run.

