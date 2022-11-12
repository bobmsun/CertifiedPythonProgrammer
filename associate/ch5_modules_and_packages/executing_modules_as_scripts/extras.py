
# Modules are just files. Modules are just py files.
# 所以 the difference between a module and a script is legitimately nothing except for 
# you could make one executable and give it a shebang if you want it to.
# But for all intents and purposes, they're just py files.
# So, even though main.py is our script here and helpers.py is the module that
# we've defined some things in, we could run both of these the same way.

print("Importing 'helpers' in 'extras'")
import helpers 

name = "Keith Thompson"
