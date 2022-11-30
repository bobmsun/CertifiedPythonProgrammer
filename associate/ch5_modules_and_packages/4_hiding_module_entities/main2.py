
from helpers2 import *
import extras2
# from helpers2 import _extract_upper      加了这行后就又可以 import 了


print(f"Lowercase Letters: {extract_lower(extras2.name)}") 
print(f"Uppercase Letters: {_extract_upper(extras2.name)}")     # 这是就会：NameError: name '_extract_upper' is not defined

