
print(2 + 2)     # 4

print(2.0 + 2.0)   # 4.0

print(2.0 + 2)    # 4.0     只要有一个是 float，结果就 return float

print(3 * 9)     # 27

print(5 / 3)    # 1.6666666666667

print(6 / 3)    # 2.0    Even if something that is evenly divisible, it's always going to return float

# Python 3 中 / 就是 数学上的 division，但之前 Python 2 可不是这样的


# Floor division
print(5 // 3)      # 1
print(6 // 3)      # 2
print(-5 // 3)     # -2   NOT -1    Java 中 -5 / 3 = -1
# 自悟：这点和 Java 不一样，Java 是向零取整，而 Python 是向下取整

print(3.3775 // 2)      # 1.0
print(4 // 3)           # 1
print(4 // 3.0)         # 1.0
print(4 // 2.0)         # 2.0
# 自悟：如果是整数相除，// floor division 除出来的结果一定是整数 （这点不同于 / division，即使运算子都是整数 且 能被整除，/ division 除出来的也是 float ）；
#      如果运算子中有 float， // floor division 除出来的结果是 float




# 关于 flour division 自己加：
print(15.0 // 7)     # 2.0    不是 整数 2
# 自悟：所以 // 是 floor division，不是 integer division, 并不是说，// 除出来的结果肯定是整数，如果运算子中有 float，结果也会是 float


# Remainder
print(5 % 3)     # 2
print(-5 % 2)    # 1    Java 中 -5 % 2 = -1
print(-5 // 2)   # -3   Java 中 -5 / 2 = -2
# 自悟：这里与 Java 也不同


# Power
print(2 ** 3)    # 8


