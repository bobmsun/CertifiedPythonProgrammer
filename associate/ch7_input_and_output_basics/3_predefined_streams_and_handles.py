

# There are some predefined streams and handles that we have access to.
# You might not even think of it as files, but they are, and they are exceptionally useful
# They are standard out, standard in, standard err
# They are all accessible to us through the sys module in python

import sys
from tkinter import READABLE
# sys module 有很多东西可以用，we use sys.exit planty of times

# sys.stdin - READABLE, take something from the user
# sys.stdout & sys.stderr    - writable, write to / print something
# stdin, stdout, stderr 都是 one-way stream，要么读，要么写，they don't do the opposite

print(sys.stdout.write("Testing\n"))
# Testing
# 8
# it wil also print out the length of the stream


print( sys.stderr.write("ERROR\n") )
# ERROR
# 6

lines = sys.stdin.readlines()
print(lines)
# Hello
# bob
# !
# ['Hello\n', 'bob\n', '!\n']

# 需要按 control + D 去结束 stdin







