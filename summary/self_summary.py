
# 自悟：string 是 immutable 的，所以只要是相同的 string 就不会 create 两份，就会是用一个 object
s1 = "aaa"
s2 = "aaa"
s3 = s1[1:2]
s4 = s1[:]

print(id(s1))
print(id(s2))      # same id as s1
print(id(s3))      # 这里 create 了新的 object 因为 s3 的值 也 s1 和 s2 不同
print(id(s4))      # same id as s1 and s2        这里没有 create 新的 obj，因为 string 是 immutable 的，只要值是相同的，就是一个 object
print(s1 == s2)    # true
print(s1 == s3)    # false
print(s1 == s4)    # true


# == 比的不是地址，而是 比的内容
l1 = []
l2 = []
l3 = ['a']

print(id(l1))
print(id(l2))     # different id with l1
print(l1 == l2)   # True
print(l1 == l3)   # False


# == 也可以用来比 dictionary
d1 = {'key1': 'value1', 'key2': 'value2'}
d2 = {'key1': 'value1', 'key2': 'value2'}

print(id(d1))
print(id(d2))     # different id as d1
print(d1 == d2)   # True


# in / not in 不光可以用于 list，还可以用于 string
print('ab' in 'feabfes')    # True
print('sed' in 'fsdagsag')   # False


# string 的 几个 function
# index()   vs   find()
# Both index() and find() are identical in that they return the index position of the first occurrence of the substring from the main string. 
# The main difference is that Python find() produces -1 as output if it is unable to find the substring, 
# whereas index() throws a ValueError exception.
# find()   vs   rfind()
# The Python function rfind() is similar to the find() function, with the sole difference being that rfind() 
# returns the highest index (from the right) for the provided substring, 
# whereas find() returns the index position of the element's first occurrence, i.e. the very first index.
print('abcdefg'.rfind('def'))   # 3


