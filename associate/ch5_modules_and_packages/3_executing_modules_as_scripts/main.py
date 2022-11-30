
print("We're importing 'helpers' from 'main'")
from helpers import *         ####

print("We're importing 'extras' from 'main'")
import extras 


print(f"Lowercase Letters: {extract_lower(extras.name)}")       ##
print(f"Uppercase Letters: {extract_upper(extras.name)}")       ##

# We're importing 'helpers' from 'main'
# HELLO FROM HELPERS
# We're importing 'extras' from 'main'
# Importing 'helpers' in 'extras'
# Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
# Uppercase Letters: ['K', 'T']


# (这里注意，import helpers in extras 时并没有再次打印 HELLO FROM HELPERS，that's because in the first import [from helpers import *], the module is read in.
# Every subsequent time that it is read in, it doesn't need to be re-read, because it has ready been written to the application, the interprator already
# has that stuff in memory)
# 自己试了一下：如果只 import extras 不 import helpers (把 #### comment掉），那么 import helpers in extras 时就会 print 出 HELLO FROM HELPERS
# 但是 把 #### comment 掉后，## 两行也会有 error，找不到 extract_lower 和 extract_upper


# So if you have an expression within a module and you import that module, what will happen?
# Does it execute? Does it execute everytime?
# On first import, it's gonna execute everything that inside of the module.
