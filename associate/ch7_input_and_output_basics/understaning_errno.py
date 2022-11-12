
# errno is a very simple package that we have access to through the Python standard library

# touch fake.py      create a file
# cat fake.py        把内容打印出来

import os
import errno

try:
    f = open('fake.txt', 'r')
except OSError as err:
    if err.errno == errno.ENOENT:
        print("File not found")
    elif err.errno == errno.EACCES:
        # print("Bad permissions")
        print(f"[Errno {err.errno} ({errno.errorcode[err.errno]})] {os.strerror(err.errno)}")  # 会打印：[Errno 13 (EACCES)] Permission denied



# python understanding_errno.py
# 会打印：File not found

# touch fake.txt
# python understanding_errno.py
# 这是就什么都不会打印了，因为没有 error 了

# chmod 700 fake.txt && sudo chown root:root fake.txt
# python understanding_errno.py
# 会打印：Bad permissions
# 
#  