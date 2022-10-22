
from codecs import BOM_BE


if 'b' < 'a':
    print('This is true')
elif 'c' < 'd':
    print('Second condition is true')
else:
    print("no condition was true")



name = input("What is your name? ")

if len(name) >= 6:
    print("Your name is long")
elif len(name) == 5:
    print("Your name is 5 characters")
elif len(name) >= 4:
    print("Your name is 4 or more characters")     # This line is gonna run when the len is exactly 4
else:
    print("Your name is short.")



