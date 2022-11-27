
# Define `random_words` and  `random_word` but we're only importing one directly
from words.generator import random_word

# *Only* provides `random_words` when the package is imported directly
from words import *    # 意思是：random_words should be imported throught importing words 

print(f"Random word generated: {random_word()}")
print(f"Random list of words:  {random_words(5)}")

