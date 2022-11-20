
import sys

from cli import main
from cli.errors import ArgumentError

try:
    main()
except (ArgumentError, AssertionError) as err:
    print(f"Error: {err}")
    sys.exit(1)


# python 5_using_assertions.py
# Error: too few arguments
# python 5_using_assertions.py test
# Name is test

