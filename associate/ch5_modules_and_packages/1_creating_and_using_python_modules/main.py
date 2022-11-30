import helpers   #  这里 import 的 path is relative to the script we are running

name = "Keith Thompson"
print(f"Lowercase Letters: {helpers.extract_lower(name)}")      # Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']

print(f"Uppercase Letters: {helpers.extract_upper(name)}")      # Uppercase Letters: ['K', 'T']


# Modules in Python are just files