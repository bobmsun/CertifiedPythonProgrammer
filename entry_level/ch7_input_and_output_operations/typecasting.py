print( float(1) )    # 1.0   

print( int(1.3) )    # 1
print( int(1.6) )    # 1   It does not round. It just juncate

print( str(1) )        # 1
print( str(1.0) )      # 1.0
print( str(False) )    # String 'False'

#int('1.2')     # ValueError: invalid literal for int() with base 10: '1.2'


# Everything in Python can be turned into a Boolean. Everything has a true/false representation

print( bool(1) )        # True
print( bool(2.4) )      # True
print( bool('Tada') )   # True

# In fact, almost everything is going to be True, with exception of some very specify things (basically things that equate to 0 or none)
print( bool(0) )       # False
print( bool(0.0) )     # False
print( bool('') )      # False
print( bool(None) )    # False
# Basically everything else will be evaluated True

# 自己加：
print( bool(0.0000000001) )     # True
print( bool(0.000000000)  )     # False


# It just returns the first one it runs into:
# So for AND:
# it will always return the first falsy value or the last trucy value 
print(1 and 0)         # 0
print(1 and 2)         # 2
print('This' and 'That')       # That
print('This' and 0 and 'That')      # 0, 都没有看到 ‘That’

print(0 and 'That')     # 0
print(0.0 and 1)     # 0.0


# It just returns the first one it runs into
# So for OR:
# it will always return the first trucy value or the last falsy value (go through all the falsy values and returns the last one)
print(1 or 0)       # 1
print(0 or 1)       # 1
print(0 or "")      # ""
print(0 or 1 or "This")      # 1     Returns 1 because it is the first truey value that it runs into


print(not "")     # True
# This is basically doing   print( not bool("") )






