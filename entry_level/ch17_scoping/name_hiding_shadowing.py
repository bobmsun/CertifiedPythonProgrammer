
# Functions creates their own scops

y = 5

def set_x(y):
    print("Inner y:", y)
    x = y        # We know x is not accessible outside the function anyway
    y = x        # Then we're gonna modifiy y to see what happen

set_x(10)

print("Outer y:", y)

# Inner y: 10
# Outer y: 5

# Because parameters went out over the variables of the same name that are at a higher context. This called name hiding.
# By setting the parameter y, we are hiding the fact that there is variable that exists at a higher context here. This is sometimes called shadowing.


# When you looking at a function, the scopy of everything inside of it is going to be:
# if it's defined as a parameter, it's going to be whatever it's passed in as a argument, or 
# if it's created inside the function, then it's going to be local only to the function



# 自己加

# 回忆之前 creating_and_using_generator 那节 的 自我 research
a_num = 33
def change_value(a_num):
    a_num = 35
change_value(33)
print( a_num )     # 33


a = 0
def change_value2():
    print("Inner a (change_value2):", a)     # 这行会报错 UnboundLocalError: local variable 'a' referenced before assignment
    a = 999
change_value2()
print(a)   # 到不了这行，之前就报错了

