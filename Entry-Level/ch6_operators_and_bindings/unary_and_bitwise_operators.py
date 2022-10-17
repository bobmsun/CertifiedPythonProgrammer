
# Unary operator

a = 0b010

print(a)     # 2

print( bin(a) )     # if you want to see the binary representation of the number
# will print 0b10    (will drop the leading zero)

# ~ operator means 2s complement
print(~a)    # -3
# the complement of a is always be   ~a  =  -1 * a - 1
print( bin(~a) )   # -0b11


# Bitwise Operator
# AND OR XOR NOT

a = 0b1001
b = 0b1100

# a | b = 0b1101
print( bin(a | b) )     # 0b1101

print( bin(a & b) )     # 0b1000

# XOR operator (exclusive OR operator)
# need only one of the columns to be 1 for the result column to be 1, otherwise will be 0
print( bin(a ^ b) )     # 0b0101  -> 0b101  (drop leading zero)

# OR: need one of them to be 1, otherwise 0
# AND: need two of them to be 1, otherwise 0
# XOR: need exactly one of them to be 1, otherwise 0


a = 0b110
print( bin(a >> 2) )     # 0b1
print( bin(a >> 4) )     # 0b0   if we to far, then it will be all zero

print( bin(a << 2) )     # 0b11000

print( a << 2 )   # 24
print(a)      # 6

a = -2
print( bin(a) )          # -0b10
print( bin(a >> 2) )     # -0b1
print( a >> 2 )    # -1
# 自悟：负数右移 >> 补1，正数右移 >> 补0；这里与 Java 一样；>> 不改变正负



