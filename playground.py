
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
