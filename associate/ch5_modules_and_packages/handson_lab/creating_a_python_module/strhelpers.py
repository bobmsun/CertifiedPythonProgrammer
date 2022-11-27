
from random import shuffle as l_shufle   
# random 中的 shuffle 是 work on list，而我们这里是 work on string

def reverse(str_value):
    return str_value[::-1]

def str_shuffle(str_value):
    str_list = list(str_value)
    l_shufle(str_list)
    #return str(str_list)
    return "".join(str_list)
