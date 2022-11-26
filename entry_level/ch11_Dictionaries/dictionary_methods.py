

ages = {'kevin': 61, 'bob': 79 }

# You can get all of the keys in the dictionary by using the keys() method
print(ages.keys())   # dict_keys(['kevin', 'bob']) 
# it's going to return us a dict key object that is a list of the keys

print( list(ages.keys()) )   # need to maually cast it into a list      ['kevin', 'bob']

print( ages.values() )       # a list of values            dict_values([61, 79])


print( ages.items() )        # a list of tuples            dict_items([('kevin', 61), ('bob', 79)])
print( list(ages.items()) )    # [('kevin', 61), ('bob', 79)]


# 自己加：items() 函数多数是在 iterate 一个 dictionary 时用的；iterate 一个 dictionary 中的所有 key-value pair
for key, value in ages.items():
        print("{} is {}".format(key, value))


# 自己加：直接用 for loop go over 一个 dict，go over 的是 key
for i in ages:
    print(i)
# kevin
# bob




# 自己加（根据模拟考试加的）：[] 和 get 函数；如果key不存在，get 函数会返回 None，但是[] 会出 error

print(ages["kevin"])            # 61
print(ages.get("kevin"))        # 61

print(ages.get("hello"))        # None
print(ages["hello"])            # KeyError: 'hello'
