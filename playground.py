
def create_var():
    global a 
    a = 89

create_var()

print(a)


a_tuple = (1, 2)
def change_tuple(a_tuple):
    a_tuple = (1, 2, 3)

change_tuple(a_tuple)
print(a_tuple)

s1 = "aaa"
s2 = "aaa"
s3 = s1[:]

print(id(s1))
print(id(s2))
print(id(s3))
print(s1 == s2)
print(s1 == s3)

l1 = ['a']
l2 = []

print(id(l1))
print(id(l2))
print(l1 == l2)


a_list_1 = [1, 2, 3]
def change_list_1():
    print(a_list_1)       # [1, 2, 3]
    a_list_1.append(4)
    a_list_1.pop(0)
    print(a_list_1)       # [2, 3, 4]
change_list_1()
print(a_list_1)           # [2, 3, 4]

a_list_2 = [1, 2, 3]
def change_list():
    print(a_list_2)       # UnboundLocalError: local variable 'a_list' referenced before assignment
    a_list_2.append(4)
    a_list_2.pop(0)
    print(a_list_2)
    a_list_2 = [3]
change_list()
print(a_list_2)            # run 不到这行

a_list_3 = [1, 2, 3]
def change_list(a_list_3):
    print(a_list_3)        # [1, 2, 3]
    a_list_3.append(4)
    a_list_3.pop(0)
    print(a_list_3)        # [2, 3, 4]
change_list(a_list_3)
print(a_list_3)            # [2, 3, 4]

add