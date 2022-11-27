
from random import sample

# Do not modifiy or remove this
# with open("/usr/share/dict/words", "r") as f:
    # WORD_LIST = [w.strip("\n") for w in f.readlines()]

WORD_LIST = ['Hello', 'Bob', 'You', 'Are', 'The', 'Best']

def random_word():
    return random_words(1)[0]

def random_words(length):
    return sample(WORD_LIST, length)      # Take the big list WORD_LIST, return a sub-list. That is just random ones selected from that list. That is this long (指 length)


