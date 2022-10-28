from helpers2 import *
import extras2


# __name__ is a variable that you didn't know you have. This is there always in every module and it lets us know what the name of this module is 
# in this context. And there is a specifc thing that this will get changed to if you're running it.
print(f"__name__ in main2.py: {__name__}")

print(f"Lowercase Letters: {extract_lower(extras2.name)}")
print(f"Uppercase Letters: {extract_upper(extras2.name)}")

# 打印：
# HELLO FROM HELPERS
# __name__ in helper2.py: helpers2
# __name__ in extra2.py: extras2
# __name__ in main2.py: __main__   （这里是 __main__ 是因为 we are actively running the main and this is the thing we can leverage to add different mode to different modules）
#                                 (可以利用这一点加 condition：do this only when we are running this script)
# Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
# Uppercase Letters: ['K', 'T']

