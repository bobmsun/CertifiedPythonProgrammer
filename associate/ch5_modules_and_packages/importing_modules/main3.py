

# import everything
from helpers import *

name = "Keith Thompson"
print(f"Lowercase Letters: {extract_lower(name)}")      # Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']

print(f"Uppercase Letters: {extract_upper(name)}")      # Uppercase Letters: ['K', 'T']


# 绝大多数情况，不会想 from XXX import * , 因为希望 import 的得 as specific as possible
