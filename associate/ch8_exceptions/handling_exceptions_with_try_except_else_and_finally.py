
import sys

try:
    print(f"Received argument {sys.argv[1]}")
    # 打印 index 为 1 的 （第二个） argument
    # python my_program.py test
    # 这里的 test 就是 index 为 1 的 argument
except:          # 这样的 except will just catch everything, 能 catch 所有 error
    print(f"Error: no arguments, please provide at least one")
    # sys.exit(1)
    

try: 
    print(f"First argument {sys.argv[1]}")
    args = sys.argv
    random.shuffle(args)
    print(f"Random argument {args[0]}")
except IndexError as err:
    print(f"Error: no arguments, please provide at least one ({err})")
    # 可以通过用 as 把 error message print 出来
except NameError:
    print(f"Error: random module not loaded")
