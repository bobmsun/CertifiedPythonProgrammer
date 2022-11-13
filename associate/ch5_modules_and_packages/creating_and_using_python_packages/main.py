from helpers.strings import extract_lower, extract_upper      # With a package, you can chain off to access the actual modules inside
from helpers import variables          # import the entire module
import helpers              # we can also import the entire package

print(f"Lowercase Letters: {extract_lower(variables.name)}")      # Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
print(f"Uppercase Letters: {extract_upper(variables.name)}")      # Uppercase Letters: ['K', 'T']

print(f"From helpers: {helpers.strings.extract_lower(variables.name)})")

