import sys

from .errors import ArgumentError        # 如果没有 . 就会出 ModuleNotFoundError: No module named 'errors'   ？？？为什么要加 . ???

def main():
    # if (len(sys.argv) < 2):
    #     raise ArgumentError("too few arguments")
    assert len(sys.argv) >= 2, "too few arguments"           # if it is evaluated to false, then it's gonna raise an AssertionError
    print(f"Name is {sys.argv[1]}")


# assert is a debug tool
# If you run code in production, you might use it using a flag that will optimize things.
# 例如，the capital O flag
# python -O 5_using_assertions.py 

# Running with -O is gonna optimize the final bytecode that is produced and executed. And it's gonna remove assert statement entirely.

# There is another version of it.  -OO flag   两个 capital O
# That will even remove doc strings

# So assert should only be used for development or debug purposes


# python -O 5_using_assertions.py     
# IndexError: list index out of range


