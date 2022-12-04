
# 即使我们刚刚学习了 name hiding (shadowing), it doesn't mean that we always want our variables to be local to a function
# Occasionally we want to be able to call a function and it changes some global state
# 这是我们可以用 "global" keyword that will allow us to do that, but it has some limitations


# 例 1
y = 5
# def set_x(y):
#     print("Inner y:", y)
#     x = y 
#     global y          # 这一行会报错    SyntaxError: name 'y' is parameter and global
#     y = x
# set_x(10)
# print("Outer y:", y)
# You cannot use the "global" keyword to work with the global value if you have a parameter of the same name
# So it's important to know, parameters always win
# There is not a situation where you have a parameter set that you are going to be interact with a variable of the same name at a higher level
# even if interacting with the "global" keyword.



# 例 2
def set_x2(z):
    x = z
    global y     # That means, I have the access to the y variable for the rest of the function that is going to be whatever the global context is
    global a     # and if it doesn't exist yet then we can create it. That's what's going on the "global a"
                 # We can create global varible from inside the function. This is probably the more useful case of using the "global" keyword
    y = x
    a = 7

print("y before set_x:", y)        # y before set_x: 5

set_x2(10)
print("y after set_x", y)          # y after set_x 10
print("a after set_x", a)          # a after set_x 7


# 对于例2 自己补充
# def create_var():
#     global aa 

# create_var()
# print(aa)      # NameError: name 'aa' is not defined


# def create_var2():
#     global aa 
#     aa = 'hello'

# create_var2()
# print(aa)      # 可以 print 出 hello


# 例 3.1
y2 = 11
def set_x3():
    x = y2  #####
    print("Inside set_x3 x:", x)
    print("Inside set_x3 y2:", y2)              
set_x3()
# Inside set_x3 x: 11
# Inside set_x3 y2: 11

# （自己加，作为对例 3.1 的补充）例 3.1.1
y2_2 = 15
def set_x3_2(y2_2):
    x = y2_2
    print("Inside set_x3_2 x:", x)
    print("Inside set_x3_2 y2:", y2)   
    print("Inside set_x3_2 y2_2:", y2_2)             
set_x3_2(20)
# Inside set_x3_2 x: 20
# Inside set_x3_2 y2: 11
# Inside set_x3_2 y2_2: 20



# 例 3.2
# 但是一旦加上这样一句，就会报错
y3 = 77
def set_x4():
    x = y3      # 报错在这一行：UnboundLocalError: local variable 'y3' referenced before assignment
    print("Inside set_x3 x:", x)
    print("Inside set_x3 y3:", y3)     
    y3 = 99         # 只要加上这句就会报错，但报错的地方在上面👆
set_x4()

# 启示：if we are just using y (例3.1)，是可以的；在外面定义的 y can be used in this more localized setting  
# （自悟：这点的前提是 parameter 中不能有重名的 y，否则会 name mangling，上一讲讲的，也就是例 3.1.1）
# 但如果像 例 3.2 中，如果我们加入了 assignment，it's not going to change something higher
# because we are assigning y 在下面，it's assuming that y is suppose to be local
# 这就是为什么会在上面报 Error 说，UnboundLocalError: local variable 'y3' referenced before assignment

# 所以 if you want to work with a global y, put the "global" keyword there （在 ##### 行的前一行加上 global y2, even though ##### would still work for us prior to the assignment)


# 视频结尾里说：
# "global" is something we can use, but I wouldn't encourage you to use it very often

