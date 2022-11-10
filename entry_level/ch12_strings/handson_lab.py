#!/usr/bin/env python3.7

message = input("Enter a message: ")

print("Lowercases:", message.lower())
print("Uppercase:", message.upper())
print("Capitalized:", message.capitalize())
print("Title Case:", message.title())

words = message.split()        # by default, it's gonna split on space
print("Words:", words)

sorted_words = sorted(words)

print("Alphabetic First Word:", sorted_words[0])
print("Alphabetic Last Word:", sorted_words[-1])
