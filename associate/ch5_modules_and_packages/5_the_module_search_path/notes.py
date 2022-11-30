# 这节课的 point
# So we've successfully created our own modules,
# figured out how imports work so that we can use our modules,
# but we haven't quite covered where imports import from and if we
# can modify those things. 


import helpers     # 我们这里可以 import helpers 是因为我们有一个 helpers.py 在我们的 current directory 中

# PYTHONPATH
# The other way that you can do it is if a PYTHONPATH
# environment variable -- so if some Python path --
# if this environment variable is set before running Python,
# you can add some more directories to the list of directories that you need to be
# able to access. 


import sys

print(sys.path)


['/Users/shihaosun/Developer/CertifiedPythonProgrammer/associate/ch5_modules_and_packages/5_the_module_search_path',   # current directory, here is where helpers come from
 '/Users/shihaosun/anaconda3/lib/python37.zip', 
 '/Users/shihaosun/anaconda3/lib/python3.7',                     # Python standard library 从这里来
 '/Users/shihaosun/anaconda3/lib/python3.7/lib-dynload', 
 '/Users/shihaosun/anaconda3/lib/python3.7/site-packages',                # this is where thrid-party packages go. 
                                                                          # If we install a third-party package into this version of Python, 
                                                                          # it's gonna go into site-packages
                                                                          # If we do an import, it's gonna search through these directories in this order.
                                                                          # If we find, then it's gonna end up loading that.
 '/Users/shihaosun/anaconda3/lib/python3.7/site-packages/aeosa']


# touch ~/example_mod.py 
# PYTHONPATH='/home/cloud_user' python3.7            # 这里我们用一个 绝对路径
# import helpers
# import example_mod        # 这里不会报错
# import sys
# sys.path          # 这是就会发现，'/home/cloud_user' 被加到了 sys.path 中，所以这是我们可以成功 import example_mod 的原因


# touch ~/sys.py           # sys.py 在 python standard library 中已经有了，这里我们是在 create 一个与 standard library 中重名的 library
# PYTHONPATH='/home/cloud_user' python3.7
# import helpers
# import sys
# sys.path                  # 这里会发现，依然可以 print 出跟原来一样的 path，不会报错，可以找到 sys.path
# 原因在于：
# although it searches through these directories in order,
# it only searches through these directories in order if it doesn't find a module
# that is built-in that has that name. So,
# if sys wasn't a standard library module,
# then it would find the sys.py that we created at home,
# but it's going to first search the standard library. So,
# this prevents us from accidentally creating a module that overrides a standard
# library module and prevents us from accessing that code.
# So when you're doing imports, it'll always look at standard library first.
# Then it's going to check out the directories that are in sys.path,
# so sys.path will always be something that the Python
# interpreter has access to. There's not a way for us to screw that up.


