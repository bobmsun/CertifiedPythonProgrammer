
phrase = "This is a simple phrase"
words = phrase.split()

print( words )     # ['This', 'is', 'a', 'simple', 'phrase']

print( phrase.split("i"))     # ['Th', 's ', 's a s', 'mple phrase']


# let's say I just want the last segment of the url
url = "https://example.com/users/jimmy"
user = url.split('/')[-1]   # [-1] get the last portion
print( user )

print( url.split('/') )       # ['https:', '', 'example.com', 'users', 'jimmy']

  
print( ", ".join(words) )      # This, is, a, simple, phrase

lines = ['First line', 'Second line', 'Third line']
output = '\n'.join(lines)
print(output)
# First line
# Second line
# Third line



# Sring formating

template = "Hello, my name is {}, and I really enjoy {}, Have a nice day!"
print( template.format('Keith', 'Python') )

print( template.format('Keith', 'Python', True) )    # Hello, my name is Keith, and I really enjoy Python, Have a nice day!
# it's going to disregard the 多余的value instead of throwing an error

# print( template.format('Keith') )     # Error


print( "Hello, my name is {0}, and I really enjoy {1}. Have a nice day! - {0}".format('Keith', 'Python') )
# Hello, my name is Keith, and I really enjoy Python. Have a nice day! - Keith

# 自我补充：另一种 format string 的 方式是 f string
# .format()  还可以 format 显示几位小数
