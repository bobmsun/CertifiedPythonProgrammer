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

# 自我补充
"hiiiii".find('i')       # return 1
"hiiiii".find('a')       # return -1

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


print("'Single' in Double")
print('"Double" in Single')
print("\"Double\" in Double")

