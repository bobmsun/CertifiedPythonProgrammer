
print(1 < 2)   # True

print(2 > 1)   # True

print(2 < 1)   # False

print(2.0 >= 3)  # False

print(2.0 >= 2)  # True

# 自我补充
print(2.0 == 2)      # True
print(2.0 == 2.0)     # True


# Can also compare string
# It is comparing alphebatically 
print('a' > 'b')     # False
print('b' > 'a')      # True
print('bb' >= 'ba')   # True
print('a' <= 'c')     # True

print( ord('a') )   # 97
print( ord('A') )   # 65

print( 'a' > 'A' )   # True

# print('a' <= 1)     Error, since cannot compare string to int, not comparable

# = for assignment operation
# == for check equal / equivalent
# == does support every type
print(1 == 1)        # True
print(1.0 == 1)      # True
print(2 == 1.0)      # False
print('a' == 2)      # False, Java 中也可以这样，也会 return false
print('a' == 'a')    # True

print( 1 != 1 )      # False
print( 2 != 1.0 )    # True


# Identity operator
print( 1 is 1 )    # True
# for "is" to return true, it has to be exact the same object (it has to take the exact spot in memory)
# 1 is 1 returns True becasue interger is immutable. There is always one instance of 1.
# Everytime we type interger 1, it's going to look at same spot memory, because you cannot modify an integer.
# So there is no reason to allocate a different spot on your computer to store it once you initialize it, 
# because there is no risk it's going to be changing.

print( 1 is 1.0 )   # False, because there is two distinct object

print( 1.0 is 1.0 )  # True

print( 'a' is 'a')  # True

print('a' is not 'a')   # False

# It's always goona be the same number. 不同人可能有不同number，但是对于同一个人来说，it's always goona be the same number
print(id('a'))    
print(id('a'))  
print(id('a'))  

# 'a' is 'a' returns True
# is essentially
# id('a') == id('a')

# Use "is" when you want to know if you are working with the exact two objects in the memory


# 以下两组 也是 always going to be same
print(id(1.0))
print(id(1.0))
print(id(1.0))

print(id(2.0))
print(id(2.0))
print(id(2.0))

# 以上涉及到的 type 都是 immutable type
# 但是也会有 mutable type，例如 list
print( [] is [] )      # False, because you can modify an empty, so Python will put this in different memory





