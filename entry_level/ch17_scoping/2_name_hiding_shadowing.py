
# Functions creates their own scops

y = 5     ####

def set_x(y):
    print("Inner y:", y)
    x = y        # We know x is not accessible outside the function anyway
    y = x        # Then we're gonna modifiy y to see what happen (这里其实是想看看能不能 modify 函数外面 #### 行定义的 y)
    print("Inner y 2nd time:", y)
    y = 8
    print("Inner y 3rd time:", y)

set_x(10)

print("Outer y:", y)

# Inner y: 10
# Inner y 2nd time: 10
# Inner y 3rd time: 8
# Outer y: 5

# Because parameters went out over the variables of the same name that are at a higher context. This called name hiding.
# By setting the parameter y, we are hiding the fact that there is variable that exists at a higher context here. This is sometimes called shadowing.


# When you looking at a function, the scope of everything inside of it is going to be:
# if it's defined as a parameter, it's going to be whatever it's passed in as a argument, or 
# if it's created inside the function, then it's going to be local only to the function



# 自己加：

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


# 自己加：
# list 是 mutable 的（之前自己试的都是 int，是 mutable type）
a_list = [1, 2, 3]
def append_number(list_input):
    list_input[0] = 100
    list_input.insert(1, 99)
    list_input.append(20)

append_number(a_list)
print(a_list)          # [100, 99, 2, 3, 20]


a_list_4 = [1, 2, 3]
def change_list_4(a_list_4):
    a_list_4[0] = 100
    a_list_4.insert(1, 99)
    a_list_4.append(20)
    print(a_list_4)        # [100, 99, 2, 3, 20]
    return a_list_4
result_4 = change_list_4(a_list_4)
print(result_4)            # [100, 99, 2, 3, 20]
print(a_list_4)            # [100, 99, 2, 3, 20]


a_list_5 = [1, 2, 3]
def change_list_4(a_list_5):
    a_list_5[0] = 100
    a_list_5.insert(1, 99)
    a_list_5.append(20)
    print(a_list_5)         # [100, 99, 2, 3, 20]
    return a_list_5
result_5 = change_list_4([1, 2, 3])
print(result_5)             # [100, 99, 2, 3, 20]    
print(a_list_5)             # [1, 2, 3]


a_list_1 = [1, 2, 3]
def change_list_1():
    print(a_list_1)       # [1, 2, 3]
    a_list_1.append(4)
    a_list_1.pop(0)
    print(a_list_1)       # [2, 3, 4]
change_list_1()
print(a_list_1)           # [2, 3, 4]


# 以下启示：不能有 assignment，一旦有了，就认为是函数内定义的 local variable了（这点跟 immutable 一样）
a_list_2 = [1, 2, 3]
def change_list():
    print(a_list_2)       # UnboundLocalError: local variable 'a_list_2' referenced before assignment
    a_list_2.append(4)
    a_list_2.pop(0)
    print(a_list_2)
    a_list_2 = [3]
change_list()
print(a_list_2)            # run 不到这行


# 这个例子跟 a_list_4 一样了
a_list_3 = [1, 2, 3]
def change_list_3(a_list_3):
    print(a_list_3)        # [1, 2, 3]
    a_list_3.append(4)
    a_list_3.pop(0)
    print(a_list_3)        # [2, 3, 4]
change_list_3(a_list_3)
print(a_list_3)            # [2, 3, 4]


# tuple 是 imutable 的
a_tuple = (1, 2)
def change_tuple(a_tuple):
    a_tuple = (1, 2, 3) 

change_tuple(a_tuple)
print(a_tuple)         # (1, 2)

