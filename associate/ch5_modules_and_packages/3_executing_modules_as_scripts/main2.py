from helpers2 import *
import extras2


# __name__ is a variable that you didn't know you have. This is there always in every module and it lets us know what the name of this module is 
# in this context. And there is a specifc thing that this will get changed to if you're running it.
print(f"__name__ in main2.py: {__name__}")

print(f"Lowercase Letters: {extract_lower(extras2.name)}")
print(f"Uppercase Letters: {extract_upper(extras2.name)}")

# 打印：
# HELLO FROM HELPERS
# __name__ in helpers2.py: helpers2
# __name__ in extras2.py: extras2
# __name__ in main2.py: __main__   （这里是 __main__ 是因为 we are actively running the main and this is the thing we can leverage to add different mode to different modules）
#                                 (可以利用这一点加 condition：do this only when we are running this script)
# Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
# Uppercase Letters: ['K', 'T']



# 自己加（网上查）：
# __name__ is a built-in variable which evaluates to the name of the current module. 
# Thus it can be used to check whether the current script is being run on its own or being imported somewhere else by combining it with if statement, as shown below.

# print ("File1 __name__ = %s" %__name__) 
  
# if __name__ == "__main__": 
#     print ("File1 is being run directly")
# else: 
#     print ("File1 is being imported")
