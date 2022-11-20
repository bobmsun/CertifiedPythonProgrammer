
# when you are building up a package that has its own types and functions, then you can also package along your own exception type
# that you can raise in very specific situation.

import sys

from cli import main
from cli.errors import ArgumentError

try:
    main()
except ArgumentError as err:
    print(f"Error: {err}")
    sys.exit(1)


# python 4_creating_custom_exception_types.py     
# Error: too few arguments

# python 4_creating_custom_exception_types.py test
# Name is test



