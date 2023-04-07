
# When working inside a programming language, variables and objects that we are working with are only accessible within certain scopes

if 1 < 2:
    x = 5

while x < 6:
    print(x)
    x += 1

print(x)
# It's gonna print out:
# 5
# 6
# That's because conditionals and loops do not define their own scops


# This is a little different when it comes to functions

def set_a():
    a = 5

set_a()

#while a < 6:    # NameError: name 'a' is not defined
#    print(a)
#    a += 1

# Functions and classes they define their own scope - that means a variable that creates inside a function remains inside the function
# 对于以上，we are not able to access a where a is only set inside the set_a() function



# 自己加的, 作为之前 “conditionals and loops do not define their own scops” 的补充
num = 1
if 1 < 2:
    print("num inside if:", num)   # num inside if: 1
    num = 22
print(num)         # 22


# 自己加：对比以下
hello_0 = 1
def change_hello_0(hello_0):
    print('hafdafdsaf', hello_0)
change_hello_0(2)    # 2     注意：print 得不是 1
# 自悟：function 里面的 hello_0 是属于 function 里面的，因为function 有自己的 own scope
# parameter 的名字为 hello_0，就 hide 了 function外 同名的变量（见下一节 name hiding）


hello = 1
def change_hello(hello):
    hello = 2
    return hello 
change_hello(hello)
print(hello)       # 1


hello_1 = 3
def change_hello_1():
    print(hello_1)     # 这里可以被 reference 到
change_hello_1()       # 会 print 3


hello_2 = 33
def change_hello_2():
    hello_2 = 44
    print(hello_2)     # 44
    hello_2 += 1
    print(hello_2)     # 45
change_hello_2()       # 会 print 44, 45
print(hello_2)         # 33
# 自悟：一旦有了 assignment 就默认 是函数里 create 的了，scope 就仅限函数里


hello_3 = 1
def change_hello_3():
    print('inside function', hello_3)    # UnboundLocalError: local variable 'hello_3' referenced before assignment
    hello_3 = 2
    return hello_3
change_hello_3()
print(hello_3)      # Error，不会到这一行
# 因为函数里有了对 hello_3 的 assignment，所以 python 就认为 hello_3 是函数里 create 的 variable，
# 就不会去 reference 外边的同名变量


# 自己加: 这样居然也行（因为 hello_4 define 在了 function call 之前)
def change_hello_4():
    print('inside function change hello4:', hello_4)
    return hello_4
hello_4 = 10
result = change_hello_4()       # inside function change hello4: 10
print(result)                   # 10


# 如果 define 在 function call 之后就会出 error 了
def change_hello_5():
    print('inside function change hello5', hello_5)    # NameError: name 'hello_5' is not defined
    return hello_5
result_2 = change_hello_5()     # run 到这里会出 error
hello_5 = 25                    # 不会 run 到这里，上面就出 error 了
print(result_2)  


print(hello_6)        # NameError: name 'hello_6' is not defined
hello_6 = 88

