# look at subsection of the string - slicing


# Indexing
test_str = 'testing'
print( test_str[0] )      # t

# test_str[18]    IndexError: string index out of range

# Negative indexing
print( test_str[len(test_str) - 1] )     # g
print( test_str[-1] )      # g
print( test_str[-4] )      # t

# test_str[-10]    IndexError: string index out of range


# Slicing: get the right segment of the string back
print( test_str[0:2] )       # te
# [starting index : the last index you want + 1 (the index that is just outside the item we want)]
# this will give us a new string

print( test_str[3 : 5] )    # ti

print( test_str[2: len(test_str)] )     # sting
print( test_str[2:] )       # sting   This is the shorthand of above   start from index 2 and give me the rest of everything

# 对于 slicing 来说，结束index可以超出 string 的边界，没关系，不会报错
print( test_str[2:99] )      # sting 
print( len(test_str[2:99]) )       # 5

# 自己加：
print(test_str[3:-1])     # tin
print(test_str[2:-2])     # sti


# In slicing, We can also add a step value
# Defaut is jump by 1 step (in this case you can just leave the step value off)
# 0 1 2 3 4 5 6
# t e s t i n g
print( test_str[1:5:2] )   # et
print( test_str[1:6:2] )   # etn

print( test_str[:6:2] )    # tsi          if you want to start from begining, you can not have the starting index
print( test_str[1::2] )    # etn

# You can also slice with negative step value
print( test_str[::-1] )    # gnitset
# Above is actually a clever way of reversing the string

# 自己加：
print( test_str[1:6:-2] )   # ""    will print empty string
print( test_str[6:1:-2] )   # gis
print( test_str[6:0:-1] )   # gnitse
print( test_str[8:0:-1] )   # gnitse
print( test_str[6:1:-1] )   # gnits
print( test_str[6:1] )      # ""   will print empty string, since default step value is 1

