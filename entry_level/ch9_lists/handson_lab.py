# 1) Set the users variable to be an empty list

users = []

assert users == [], f"Expected `users` to be [] but got: {repr(users)}"

# repr() 函数
# The repr() function returns a printable representation of the given object.
# The repr() function takes a single parameter:
# obj - the object whose printable representation has to be returned
# The repr() function returns a printable representational string of the given object.


# Implement __repr__() for custom objects
# Internally, repr() function calls __repr__() of the given object.
# You can easily implement/override __repr__() so that repr() works differently.

class Person:
    name = 'Adam'

    def __repr__(self):
        return repr('Hello ' + self.name )

print(repr(Person()))         # 'Hello Adam'


# 2) Add 'kevin', 'bob', and 'alice' to the users list in that order without reassigning the variable.

# 注意：这里要求：without reassigning the variable!!

users.append('kevin')
users.append('bob')
users.append('alice')

assert users == ['kevin', 'bob', 'alice'], f"Expected `users` to be ['kevin', 'bob', 'alice'] but got: {repr(users)}"

# 3) Remove 'bob' from the users list without reassigning the variable.

del users[1]

assert users == ['kevin', 'alice'], f"Expected `users` to be ['kevin', 'alice'] but got: {repr(users)}"

# 4) Reverse the users list and assign the result to `rev_users`

rev_users = list(reversed(users))

assert rev_users == ['alice', 'kevin'], f"Expected `rev_users` to be ['alice', 'kevin'] but got: {repr(rev_users)}"

# 5) Add the user 'melody' to users where 'bob' used to be.

users.insert(1, 'melody')

assert users == ['kevin', 'melody', 'alice'], f"Expected `users` to be ['kevin', 'melody', 'alice'] but got: {repr(users)}"

# 6) Add the users 'andy', 'wanda', and 'jim' to the users list using a single command

users += ['andy', 'wanda', 'jim']

assert users == ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'], f"Expected `users` to be ['kevin', 'melody', 'alice', 'andy', 'wanda', 'jim'] but got: {repr(users)}"

# 7) Slice the users lists to return the 3rd and 4th items and assign the result to `center_users`

center_users = users[2:4]

assert center_users == ['alice', 'andy'], f"Expected `users` to be ['alice', 'andy'] but got: {repr(center_users)}"
