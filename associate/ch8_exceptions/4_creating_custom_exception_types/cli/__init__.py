import sys

from .errors import ArgumentError        # 如果没有 . 就会出 ModuleNotFoundError: No module named 'errors'   ？？？为什么要加 . ???

print("running cli.__init__.py")     # 这行是自己加的，就是想证明，没动我们 import 一个 package 的时候，都会 run 这个 package 的 __init__.py 

def main():
    if (len(sys.argv) < 2):
        raise ArgumentError("too few arguments")
    print(f"Name is {sys.argv[1]}")


