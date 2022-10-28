

# This allows us to import specific thing that we want from the module
from helpers import extract_lower, extract_upper

name = "Keith Thompson"
print(f"Lowercase Letters: {extract_lower(name)}")      # Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']

print(f"Uppercase Letters: {extract_upper(name)}")      # Uppercase Letters: ['K', 'T']


# print(f"Uppercase Letters: {helper.extract_upper(name)}")     # NameError: name 'helpers' is not defined


# Can also
# from helpers import extract_lower as e_low
# print(f"Lowercase Letters: {e_low(name)}") 

