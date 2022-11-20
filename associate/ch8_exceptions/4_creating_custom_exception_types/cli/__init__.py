import sys

from .errors import ArgumentError        # 如果没有 . 就会出 ModuleNotFoundError: No module named 'errors'   ？？？为什么要加 . ???

def main():
    if (len(sys.argv) < 2):
        raise ArgumentError("too few arguments")
    print(f"Name is {sys.argv[1]}")


