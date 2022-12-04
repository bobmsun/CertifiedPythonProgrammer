
# Generators are functions the behave like a iterator

def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step 

# 之前讲过，we can convert "range" into a list. We can also convert generator into a list
# The "list" function that we have been using for tpye-casting is pretty dynamic
# It will work for our customer generator also.
generator = gen_range(10)
print( list(generator) )   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 这样做也不是什么时候都 work，sometimes you'll have a infinite generator. 这时就会有问题，when we are trying to convert it into list

def gen_fib():
    a, b = 0, 1
    while True:    # while True, because the fibonnaci sequence never ends
        a, b = b, a + b
        yield a     # a is the current number, b is the next number always
# 1
# 1
# 2
# 3
# 5
# ...

fib = gen_fib()
list(fib)      # this line will just go forever
# That's the potential issue when we are trying to turn generator into a list


# 以下，just want to show how fast it can be to use generator 得到 fib(50) 
# Remember, 之前用 recursion 的时候 根本无法 计算出 fib(50)
print([next(fib) for _ in range(50)][-1])              # 12586269025


