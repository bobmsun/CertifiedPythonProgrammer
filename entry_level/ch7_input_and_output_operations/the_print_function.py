
# Below will prompt the user 3 times
name = input("What is your name? ")
color = input("What is your favoriate color? ")
age = int(input("How old are you today? "))

# Above we take some user input
# Then we want to present it back
print(name)
print("is " + str(age) + " years old")       # 这里如果不把 age 转化成 str 会报错，TypeError: can only concatenate str (not "int") to str, 这点和 java 不一样，java 会把数字变成 string 然后 concatenate
print("and loves the color " + color + ".")

# print fucntion will automatically add the newline charater
# the end parameter of the print function by default is a newline charater
print(name, end=" ")
print("is " + str(age) + " years old", end=" ")
print("and loves the color " + color + ".", end=" ")

# the sep parameter for print function
print(name, 'is', age, 'years old and loves the color', color + '.', sep=' ')      # single space is the default value of sep
print(name, 'is', age, 'years old and loves the color', color + '.') 
print(name, 'is', age, 'years old and loves the color', color + '.', sep=', ')  

print()
# Python 中的 print function
'''
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments:
file: a file-like object (stream); defaults to the current sys.stdout.
sep: string inserted between values, default a space.
end: string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.

*values: object 可以 take 无限多个 parameter
'''

# Main takeaway
# The print() function can take as many argument as you want, before you start specifying the things that customerize how print works
# print(xxx, xxx, xxx, xxx, ..., sep=' ', end='\n')
# can dictate what goes between each of these value using sep
# and what is at the end of the print using end

