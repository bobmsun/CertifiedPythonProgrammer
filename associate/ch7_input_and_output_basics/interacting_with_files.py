
# interact with files or file-like object

# to create a file object, we can use the "open" function


# open("some_file.txt", "r")
# mode
# r - read
# w - write 
# r+ - read and write
# w+
# x - creation 
# a - appending (just add to the end)
# r+b

my_file = open('xmen.txt', 'w+')
# truncate the file if it already exists and we also want to be able to read from it
my_file.write('Beast\n')
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
# CyclopsBishopNightcrawler


# whenever we work with a file, we need to close it. Just call .close() function
my_file.close()

my_file = open('xmen.txt', 'r')
print(my_file.read())
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
# When we call read(), it's gonna read from the current curse to the end of the file




my_file = open('xmen.txt', 'w+')

my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n'
])

my_file.seek(0)    # seek to the offset or the position you want to go to
print(my_file.read())
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
my_file.write("morph")
print(my_file.read())
my_file.close()

# will print:
# 
# Phoenix
# Cyclops
# Bishop
# Nightcrawler

# 因为 we wrote over "Beast", 然后 print 的时候它从 \n 开始 print






my_file = open('xmen.txt', 'w+')

my_file.write('Beast\n')
my_file.write('Phoenix\n')
my_file.writelines([
    'Cyclops\n',
    'Bishop\n',
    'Nightcrawler\n'
])

my_file.seek(0)
my_file.write("morph")
my_file.seek(0)
print(my_file.read())
my_file.close()

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
    my_file.write("morph")
    my_file.seek(0)
    print(my_file.read())


# 这样也行：
my_file = open('xmen.txt', 'r')
with my_file:
    print(my_file.read())
    my_file.seek(0)
    for line in my_file.readlines():
        print(line)
    # readlines() is gonna put a new line character for each line
    # and print() will add another new line character
    
    my_file.seek(0)
    lines = my_file.readlines()
    print(lines)         # ['morph\n', 'Phoenix\n', 'Cyclops\n', 'Bishop\n', 'Nightcrawler\n']
    

  