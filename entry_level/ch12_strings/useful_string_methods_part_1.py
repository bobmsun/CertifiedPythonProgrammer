
print( "This".lower )    # If you don't put any parathethses, it will just tell us this is a method on the string object. We didn't actually invoke it or call it.

print("This".lower())    # this        # it's gonna return a new string

print("this".upper())    # THIS        # it will capitalize every letter that can be capitalized. 
# If the letter doesn't have a capital version, it will stay the same.

my_str = "tEsTinG"
print( my_str.capitalize() )         # Testing        # It's gonna capitalize the first letter and lowercase everything else in the string
print( "McCord".capitalize() )       # Mccord


print( "This is a multiword String".title() )    # This Is A Multiword String  
# will capitalize the first letter of each word (everything separated by space, 
# it's gonna find the word and capitalize that)

print( "Kevin@example.com" == "kevin@example.com" )        # False
print( "Kevin@example.com".lower() == "kevin@example.com" )       # True


# isXXXX functions

# Check to see if a string follows certain type of pattern
print( my_str.isascii() )    # True     # If all the characters can be represented as a ASCII string (the much more restricted code point vs UTF-A) then return true


print( my_str.islower() )    # False
print( my_str.isupper() )    # False
print( my_str.istitle() )    # False      check if it is title-cased

print( my_str.title().istitle() )      # True

print( " ".isspace() )        # True 
print( "f".isspace() )        # False       if there is any kind of character, then return false


# isdecimal, isdigit, isnumeric
print( "1.0".isdecimal() )     # False    return Fase
print( "1".isdecimal() )       # True    check if it's a decimal notation, which basically means if it is a whole number, cannot contain '.'
print( "a".isdecimal())       # False

print("1".isdigit())         # True
print("11".isdigit())        # True

print( "1.0".isnumeric() )      # False
print( "10".isnumeric() )       # True

# Essentially, all these 3 functions work roughly the same way, which is, if the string you are working with is only numbers, 
# then they should return True



# isalpha - stands for is alphabetical, check if it's all alphabetical characters
print( "1a".isalpha() )       # False
print( "afasdfasdf".isalpha() )       # True


# isalnum - is alpha-numeric
print( "afasdfasdf123123".isalnum() )    # True


# isidentifier - check to see if the string could be used as a variable name or as a name of a function 
# or as a name of a class (anything we can use to represent a constant that we can pass around)
print( "1bead".isidentifier() )       # False 
print( "word".isidentifier() )        # True   return true because "word" would work to be an identifer
print( "if".isidentifier() )         # True    （自悟：居然 return true，看来不check keyword）

# From W3 school:
# The isidentifier() method returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier 
# cannot start with a number, or contain any spaces.


# isprintable
print( "This is printable".isprintable() )   # True
print( "This is printable\n".isprintable() )     # False
# it's gonna return False even though we could print it. It's not considered printable because it has a escape charater 
# (since escape charater cannot be printed out)




