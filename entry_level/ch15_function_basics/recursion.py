

# Fibonnaci number: 1, 1, 2, 3, 5, 8, 13
# f(n) - the nth number in the Fibonnaci sequence: f(n) = f(n - 1) + f(n - 2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n - 2) + fib(n - 1)


item_to_calculate = int(input("What Fibinnaci item would you like to calculate it? "))
print(fib(item_to_calculate))

# fib(15)    结果返回得还比较快
# fib(30)    需要等一段时间才能返回结果，因为有 so many function call

# Certain language has the feature called tail-call optimization, where you call the function as the last call in the function,
# then it will manage to optimize that. But python is NOT one of those languages. So you will run into situations here where it's not 
# going to do anything to explicitly or implicitly improve the performance of recursion

# fib(50)   # 时间长得几乎无法完成，takes forever, 看不到结果，has to control+C to stop
# You will notice there is a big difference between fib(15) and fib(30), but there is a massive difference between fib(30) and fib(50)
# 自己用 Java 试了一下，fib(15) 和 fib(30) 可以 calculate，但是 fib(50) 就 calculate 不出来了，同样 take forever



