
print(2 + 2)   # return integer    4

print(2.0 + 2.0)   # return floats    4.0

print(2 + 2.0)    # return floats    4.0   只要有 float，结果就是 float


# Scientific Notation
print(4.5e9)      # 4500000000.0        不是整数
print(4.5e9 == 4.5 * (10 ** 9))     # return True
print(4.5e-2)    # 0.045


print(4.5 * (10 ** 9))     # 4500000000.0    不是整数
print( type(4.5 * (10 ** 9)) )     # <class 'float'>
print( type(450000000) )      # <class 'int'>

# 自己加：Python 中的数据类型
print( type(4.5) )     # <class 'float'>
print( type(10) )      # <class 'int'>
