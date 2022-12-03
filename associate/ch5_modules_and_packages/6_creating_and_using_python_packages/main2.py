
from helpers.strings import extract_lower  
from helpers import variables 
from helpers import *             # 这时，下面的 extract_upper comes from 这行
import helpers  

print(f"Lowercase Letters: {extract_lower(variables.name)}")      # Lowercase Letters: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n']
print(f"Uppercase Letters: {extract_upper(variables.name)}")      # Uppercase Letters: ['K', 'T']


print(f"From helpers: {helpers.strings.extract_lower(variables.name)})")      # From helpers: ['e', 'i', 't', 'h', 'h', 'o', 'm', 'p', 's', 'o', 'n'])

