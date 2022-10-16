
print(2 + 2)     # 4

print(2.0 + 2.0)   # 4.0

print(2.0 + 2)    # 4.0     只有有一个是 float，结果就 return float

print(3 * 9)     # 27

print(5 / 3)    # 1.6666666666667

print(6 / 3)    # 2.0    Even if something that is evenly divisible, it's always going to return float

# Python 3 中 / 就是 数学上的 division，但之前 Python 2 可不是这样的


# Floor division
print(5 // 3)      # 1
print(6 // 3)      # 2
print(-5 // 3)     # -2   NOT -1    Java 中 -5 / 3 = -1
# 自悟：这点和 Java 不一样，Java 是向零取整，而 Python 是向下取整

# Remainder
print(5 % 3)     # 2
print(-5 % 2)    # 1    Java 中 -5 % 2 = -1
print(-5 // 2)   # -3   Java 中 -5 / 2 = -2
# 自悟：这里与 Java 也不同


# Power
print(2 ** 3)    # 8
