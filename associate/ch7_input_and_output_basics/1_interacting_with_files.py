
# This chapter is about how we can interact with files or file-like object

# To create a file object, the main way to do that is by using the "open" function

# open("some_file.txt", "r")
# mode
# r - read
# w - write       When you open something for writing (w), actullly it will replace all the content of the file. 
#                 It will truncate the file and it's gonna start writing from the zero-th position of the file
# r+ - read and write      want to read it but also have the option to write to it
# w+                      truncate the file but also have the ability to read and write to it
# x - creation 
# a - appending (just add to the end of the content, will not delete what's currently there, just want to add new things to it)
# r+ by default is r+t, meaning you're gonna get text (string) back
# r+b   alternatively, you have +b, this is for working with binary data

my_file = open('xmen.txt', 'w+')
# truncate the file if it already exists and we also want to be able to read from it
my_file.write('Beast\n')      # need to add newline character, otherwise 下一次 write 的时候 it will just continue
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops',
    'Bishop',
    'Nightcrawler'
])
# writelines allows us to give a list instead of a value

# cat xmen.txt      看看file 里写进去了什么
# Beast
# Phoenix
# CyclopsBishopNightcrawler      # 尽管这里我们 call 了 writelines，你可能会想 each of these will in separate lines，但事实不是这样

# whenever we work with a file, we need to close it when we are done. Just call .close() function
my_file.close()



my_file = open('xmen.txt', 'r')       # open the file in reading mode
print(my_file.read())             # read is going to give us one big string. It just gives us the entire content of the file.
# 上面的 r 是 text mode by default, 所以 read 会给我们 text
# 如果是 r+b，那么 read 会给我们 byte object
my_file.close()
# Beast
# Phoenix
# CyclopsBishopNightcrawler




my_file = open('xmen.txt', 'w+')

my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n'
])

print(my_file.read())
my_file.close()
# It will print nothing
# Becasue there is a curse, as we are going through this file, the curse maintains what current position is
# When we call read(), it's gonna read from the current curse to the end of the file, which currently isn't anything




my_file = open('xmen.txt', 'w+')

my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n'
])

my_file.seek(0)    # seek to the offset or the position you want to go to
print(my_file.read())   # then it's going to read from the zero-th position, which is the very beginning of the file
my_file.close()




# the curse position is very important 
my_file = open('xmen.txt', 'w+')

my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n'
])

my_file.seek(0)
my_file.write("Morph")     # here I am very specific. I'm going to write something that's exactly 5 characters long.
print(my_file.read())
my_file.close()

# will print:
# 
# Phoenix
# Cyclops
# Bishop
# Nightcrawler

# 因为 we wrote over "Beast" and stop the cursor right before this newline character, 然后 print 的时候它从 \n 开始 print
# So when we move our cursor, then anythime we write, we just write on top of it.





my_file = open('xmen.txt', 'w+')

my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n'
])

my_file.seek(0)
my_file.write("Morph")
my_file.seek(0)
print(my_file.read())
my_file.close()
# Morph
# Phoenix
# Cyclops
# Bishop
# Nightcrawler

# 这也就证明了，we move our curser and every time we write, we just write on top of it






# with statement （用了 with statement 就不用在最后 close了）
with open('xmen.txt', 'w+') as my_file:
    my_file.write('Beast\n')
    my_file.write('Phoenix\n')
    my_file.writelines([
        'Cyclops\n',
        'Bishop\n',
        'Nightcrawler\n'
    ])
    my_file.seek(0)
    my_file.write("Morph")
    my_file.seek(0)
    print(my_file.read())


# 这样也行：
my_file = open('xmen.txt', 'r')
with my_file:
    print(my_file.read())
    my_file.seek(0)
    for line in my_file.readlines():
        print(line)
    # each of the line has a newline character at the end of it
    # and print() will add another new line character
    
    my_file.seek(0)      # 如果没有这行，下面会 return 一个 []
    lines = my_file.readlines()
    print(lines)         # ['Morph\n', 'Phoenix\n', 'Cyclops\n', 'Bishop\n', 'Nightcrawler\n']
    
# my_file_object.read()  vs   my_file_object.readlines()
# read() 就是从 current cursor 的位置开始读，然后return 下面的所有 content as one big string
# readlines() 是 return 一个 list (也是从 current cursor 的位置开始读)，list 中 每一个 string 是一行


