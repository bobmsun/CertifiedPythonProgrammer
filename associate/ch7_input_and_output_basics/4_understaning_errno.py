
# errno is a very simple package that we have access to through the Python standard library

# touch fake.py      create a file
# cat fake.py        把内容打印出来

import os
import errno

# open('fake.txt', 'r')       # FileNotFoundError: [Errno 2] No such file or directory: 'fake.txt'

# pyhton
# >>> FileNotFoundError.__bases__
# (<class 'OSError'>,)
# >>> PermissionError.__bases__
# (<class 'OSError'>,)
# 这两个 Error 的 parent class 都是 OSError

try:
    f = open('fake.txt', 'r')
except OSError as err:
    if err.errno == errno.ENOENT:
        print("File not found")
    elif err.errno == errno.EACCES:
        print("Bad permissions")
        print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}")   # 会打印：[Errno 13 (EACCES)] Permission denied

# Permission denied 是 the official string name for this type of error，需要用 os package 来给它 print 出来
# errno is a very very simple package that we have access to through the standard library


# 以下 from python doc
# errno.ENOENT
# No such file or directory. This error is mapped to the exception FileNotFoundError.
# errno.EACCES
# Permission denied. This error is mapped to the exception PermissionError.



# python understanding_errno.py
# 会打印：File not found

# touch fake.txt
# python understanding_errno.py
# 这是就什么都不会打印了，因为没有 error 了

# chmod 700 fake.txt && sudo chown root:root fake.txt      这里在 set this to be only readable by the owner and then also change it to be owned by root
# python understanding_errno.py
# 会打印：Bad permissions
# 
#  