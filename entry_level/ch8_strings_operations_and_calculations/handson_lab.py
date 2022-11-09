#!/usr/bin/env python3.7

# Indexing and Slicing Python Strings

# We want to be able to execute our script, so to begin create an empty script named string-info.py with a shebang and make it executable:
# $ echo '#!/usr/bin/env python3.7' > string-info.py
# $ chmod +x string-info.py

message = input("Enter a message: ")


print("First character:", message[0])
print("Last character:", message[-1])
print("Middle chararcter:", message[int(len(message) / 2)])      # If it's even number of characters, want to print the 后者
print("Even index characters:", message[0::2])
print("Odd index characters:", message[1::2])
print("Reverse message:", message[::-1])

