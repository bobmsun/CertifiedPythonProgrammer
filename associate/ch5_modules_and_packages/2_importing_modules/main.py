
# If the module name is gonna conflict with variable name, then we can change the module name while we are importing it 
# by doing import XXX as YYY
import helpers as h

name = "Keith Thompson"
print(f"Lowercase Letters: {h.extract_lower(name)}")      # Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']

print(f"Uppercase Letters: {h.extract_upper(name)}")      # Uppercase Letters: ['K', 'T']

