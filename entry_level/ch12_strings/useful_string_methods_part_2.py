
phrase = "This is a simple phrase"
words = phrase.split()         # by default, split by space

print( words )     # ['This', 'is', 'a', 'simple', 'phrase']

print( phrase.split("i"))     # ['Th', 's ', 's a s', 'mple phrase']


# let's say I just want the last segment of the url
url = "https://example.com/users/jimmy"
user = url.split('/')[-1]   # [-1] get the last portion
print( user )               # jimmy

print( url.split('/') )       # ['https:', '', 'example.com', 'users', 'jimmy']


print( ", ".join(words) )      # This, is, a, simple, phrase

lines = ['First line', 'Second line', 'Third line']
output = '\n'.join(lines)
print(output)
# First line
# Second line
# Third line



# String formating

template = "Hello, my name is {}, and I really enjoy {}, Have a nice day!"
print( template.format('Keith', 'Python') )

print( template.format('Keith', 'Python', True) )    # Hello, my name is Keith, and I really enjoy Python, Have a nice day!
# it's going to disregard the 多余的 value instead of throwing an error

# print( template.format('Keith') )     # Error


print( "Hello, my name is {0}, and I really enjoy {1}. Have a nice day! - {0}".format('Keith', 'Python') )
# Hello, my name is Keith, and I really enjoy Python. Have a nice day! - Keith

# 自我补充：另一种 format string 的 方式是 f string
# .format()  还可以 format 显示几位小数



# handson lab 补充：
a_test_str = '    a  b  c     '
a_test_str.strip()
print(a_test_str)        #     a  b  c       已在证明 strip 不改变原 string，而是生成新 string (当然不改变，因为string 是 immutable 的)

print(a_test_str.strip())      # a  b  c        # .strip() 的 default 参数是 space

a_test_str = '\n    a  b  c     \n'
print(a_test_str.strip('\n'))    #     a  b  c
