

# open a file: touch closures.py


# 下面 define a function that returns a function
def greeter(prefix):
    def greet(name):
        print(f"{prefix} {name}")
    return greet

# Python treats functions as first-class citizens, so they are objects that can be passed around.
# They aren't implicitly invoked whenever you reference the name.
# And what this allows us to do is to kind of ad-hoc create functions
# that do things. So, we'll create a hello function,
# which is a greeter that starts with hello -- so, this is the prefix --

hello = greeter("Hello,")
goodbye = greeter("Goodbye,")

hello("Kevin")            # Hello, Kevin
goodbye("Kyle")           # Goodbye, Kyle



# 以下例子想说明：在函数里面定义的 variable 也可以被 closure 保留下来

def greeter2(prefix):
    other_name = prefix + "lala"                 # Normally, when you create a variable inside a function, it just gets cleaned up at the very end of the function. 
                                                 # But in this case, it's going to be held on to because of the way closure works.
    def greet2(name):
        print(f"{prefix} {name} {other_name}")
    return greet2

hello2 = greeter2("Hello,")
goodbye2 = greeter2("Goodbye,")

hello2("Kevin")            # Hello, Kevin Hello,lala
goodbye2("Kyle")           # Goodbye, Kyle Goodbye,lala


