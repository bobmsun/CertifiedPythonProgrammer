print( 'single quoted string' )      # This is what is called 'string literals'

print( "double quoted string" )

print( '''
this is a triple quoted 
multi-line stirng
''' )
# '\nthis is a triple quoted\nmulti-line string\n'

# "This is a double quoted string'
# SyntaxError: EOL while scanning string literal


print( "pass" + "word" )     # password       can combine string using +

# "pass" - "word"
# TypeError: unsupported operand type(s) for -: 'str' and 'str'

print( "Ha" * 4 )       # HaHaHaHa


# String is an object
# Object is used to encapsulte 2 things: state & behavior (functionality that tied to this type, methods)

"my_string".find('t')      # return 4
"my_string".find('in')     # return 6
"TeStInG".lower()          # return testing      
"PassWord123".lower()      # password123        (if it doesn't have lower case, this function will do nothing, will not throw error)

# 自我补充（find）
"hiiiii".find('i')       # return 1
"hiiiii".find('a')       # return -1
print("abc13".capitalize())     # Abc13

# 自我补充（rfind）
# https://www.w3schools.com/python/ref_string_rfind.asp
# The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)        # 12

# 自我补充： .index() & .rindex()  vs.   .find() & .rfind()
# index() & rindex() 如果要找的东西不存在的话，会 throw error
# .find() & .rfind() 如果要找的东西不存在的话，会 return -1
# >>> a = 'abcde'
# >>> a.index('f')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: substring not found
# >>> a.rindex('f')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: substring not found
# >>> a.find('f')
# -1
# >>> a.rfind('f')
# -1

# list 与 string 都有：  .index() & .rindex()     in / not in operator
# list 没有  .find() & .rfind()  
print('case' in 'fdsbhicase gga')         # True
print('case' not in 'dfsagdaga fdsa')     # True
print('abc' in 'fdsgagdssa')              # False

print( ['a', 23, False, [1, 2, 3]].index(23))     # 1
print( ['a', 23, False, [1, 2, 3]].index(293) )   # ValueError: 293 is not in list

print(False in ['a', 23, False, [1, 2, 3]])       # True
print([1, 2, 3] in ['a', 23, False, [1, 2, 3]])   # True     注意：这里是 True，由此引申出以下补充


# 自我补充：in   vs.   ==
print( [1, 2, 3] == [1, 2, 3] )     # True
print( [1, 2, 3] is [1, 2, 3] )     # False
# 摘自：https://www.w3schools.com/python/ref_keyword_is.asp
# The is keyword is used to test if two variables refer to the same object.
# The test returns True if the two objects are the same object.
# The test returns False if they are not the same object, even if the two objects are 100% equal.
# Use the == operator to test if two variables are equal.
# 自我补充：
print([1, 2, 3] == [1, 2, 3])          # True
print((1, 2, 3) == (1, 2, 3))          # True
print({'a': 1, 'b': 2} == {'b': 1, 'a': 2})      # False
print({'a': 1, 'b': 2} == {'b': 2, 'a': 1})      # True
set_a = set([1, 2, 3])
set_b = set([1, 2, 3])
set_c = set([3, 2, 1])
print(set_a == set_b)                  # True
print(set_a == set_c)                  # True



# 自我补充
text = 'HelloWorld'
print(text[5])   # w


# Escape Sequence
print("Tab\tDelimited")     # Tab     Delimited

print("New\nLine")
# New
# Line


# 就想 print \n
print("New\\nLine")


print("'Single' in Double")       # 'Single' in Double
print('"Double" in Single')       # "Double" in Single
print("\"Double\" in Double")     # "Double" in Double

