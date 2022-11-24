
import sys

try:
    print(sys.argv)    # 如果 run 的是：python 2_handling_exceptions_with_try_except_else_and_finally.py test，
                       # 会打印出 ['2_handling_exceptions_with_try_except_else_and_finally.py', 'test']
    print(f"Received argument {sys.argv[1]}")      # sys.argv is a list, it's gonna give us the arguments our script receives
    # 打印 index 为 1 的 （第二个） argument
    # python my_program.py test
    # 这里的 test 就是 index 为 1 的 argument
    # test is the second argument, the first argument is actually the name of the file
except:          # 这样的 except will just catch everything, 能 catch 所有 error
    # catch all types of exception
    print(f"Error: no arguments, please provide at least one")
    # sys.exit(1)
    
# 可以有多个 except block to catch specific exception
try: 
    print(f"First argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f"Random argument {args[0]}")
except IndexError as err:
    print(f"Error: no arguments, please provide at least one ({err})")
    # 可以通过用 as 把 error message print 出来
    # sys.exit(1)       #####
except NameError:
    print(f"Error: random module not loaded")
else:   # the else block will get executed if we are able to make it all the way through the try block without an error
    # else is going to run if there was no exception caught
    print("else is running")
finally:  # the finally block will run regardless  但前提是，之前不能有像 ##### 这样的 sys.exit() 因为 sys.exit() will cause the termination of the script
    print("Finally is running")



try: 
    print(f"First argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f"Random argument {args[0]}")
except (IndexError, KeyError) as err:   # 如果想 catch 不止一种 exception，就 put a tuple here
    # 没有 except block 可以 catch 不止一个 Exception
    # It can catch an IndexError, an KeyError, or a class that inherits from either of these two classes.
    # Remember when we ask a class if it is a type of instance, 如果我们 ask if it is a type of parent class, it's going to say yes.
    # That's because subclasses are just more specific variation of a parent class
    print(f"Error: no arguments, please provide at least one ({err})")
except NameError:
    print(f"Error: random module not loaded")
else:   # else is going to run if there was no exception caught
    print("else is running")
finally:  
    print("Finally is running")

# If you happen to have some sort of exception type that inherited from KeyError and NameError, just like the elif statement in conditional,
# you are going to just hit one of these except blocks. That's also worth noting.
