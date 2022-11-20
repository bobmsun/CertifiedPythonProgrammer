
# Occassionally, you want to write exception types that hold on the some additional information and you want to be able to
# access that when you handling the exception. So for that, we can use exception argument.

# Exception is just classes. So if you want it ot have some argument, we just have to customize init

class TransitionError(Exception):
    def __init__(self, previous, next_state, message):
        self.previous = previous
        self.next = next_state
        self.message = message

# crete file using touch
# touce transition_error.py
