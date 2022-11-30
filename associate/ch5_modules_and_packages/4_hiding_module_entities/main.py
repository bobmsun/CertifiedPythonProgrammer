
# 这节课是关于：If there is any way we can prevent our entity in a module from being shown (hiding module entity)
# Basically everything inside a module is accessible outside a module if you know its name


from helpers import *
import extras
# from helpers import extract_lower
# If someone do "from module import XXX", so there is really no way you can prevent them from accessing it，除非一些非常诡异的做法


print(f"Lowercase Letters: {extract_lower(extras.name)}")     # NameError: name 'extract_lower' is not defined 
# 但这并不代表 extract_lower 就不 available to us anymore，只是 通过 from helpers import * 不 available 了
# 如果 改成 from helpers import extract_lower 就 work 了
print(f"Uppercase Letters: {extract_upper(extras.name)}")


# There only two ways to hide entities from module （其实都只是针对 from Module import * 而言的）
# 法一：setting __all__
# 法二：naming things slightly differently


