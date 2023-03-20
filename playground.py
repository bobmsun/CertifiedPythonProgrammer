
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


hello = 1
def change_hello(hello_new):
    print('inside function', hello)
    hello = 1
change_hello(hello)
print('jjkjjkj', hello)
