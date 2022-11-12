
# Lambdas are what are known as anonmyous functions or functions that don't have a name.
# And it's really what we utilize when we have a situation where we want to
# have a repeatable bit of code,
# but it's not really warranted to create a function for it, and we want to do it quick and easily in line.

# mkdir XXXXX
# rm -rf XXXX

# 相比较于普通 function，lambda function 的 function body only gets one expression

# We use "lambda" keyword to create a lambda expression, which is a single expression anonymous function

def square(num):
    return num * num

# lambda (parameter): expression     
lambda num: num * num     # (lambda 有 implict return）    The result of the expression in lambda is always going to be returned

# 以上两个 是 equivalent 的

# In fact, lambda can actually be named to variables, we can assigned it to a variable 
square_lambda = lambda num: num * num

# assert is just to verify the thing is true
assert square(4) == square_lambda(4)            # If this is not true, the assert will give us an Error (AssertError)


# Lambda can be handy when you factor in different functions and
# methods that can take in functions as arguments.
# And that's what we're going to cover in the next lesson as we go over working through collections.

