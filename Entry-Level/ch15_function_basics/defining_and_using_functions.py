

# function normally starts with lower case letter
# snake case

# functions whose name starts with underscore _, those indicate some sort of hidden functions (it's not something you are going to call directly most of the time)

from turtle import fd


def print_something(something):   # parameter - is going to be some variable that exists inside the body of the function
    pass

def print_name(name):
    print(f"Name is {name}")        # f string allows us to interprate things


print( print_name )        # will just tell you it's a function

# print_name()       # TypeError: print_name() missing 1 required positional argument: 'name'


print_name('Keith')
# Name is Keith


output = print_name("Keith")
print(output)         # None     because the function doesn't return anything


def add_two(num):
    return num + 2

result = add_two(4)
print(result)       # 6


def add(num1, num2):
    return num1 + num2

print( add(1, 5) )      # 6



