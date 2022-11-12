name = input("What is your first name? ")

# 1) Call `print` with a different string using a single conditional expression
# if len(name) >= 6:
#     print(
#         "Your name is as long or longer than the average first name in the United States"
#     )
# else:
#     print("Your name is shorter than the average first name in the United States")

print(
    "Your name is as long or longer than the average first name in the United States"
) if len(name) >= 6 else print(
    "Your name is shorter than the average first name in the United States"
)


# 2) Set `message` using a single conditional expression
# if name[0].lower() in ["a", "j", "m", "e", "l"]:
#     message = "The first letter in your name is among the five most common"
# else:
#     message = "The first letter of your name is not among the five most common"

message = ("The first letter in your name is among the five most connon" if name[0].lower() in ["a", "j", "m", "e", "l"] else "The first letter of your name is not among the five monst common")

print(message)

# 3) Change the string passed to the `print` function using a conditional expression
# for letter in name:
#     if letter.lower() in ["a", "e", "i", "o", "u"]:
#         print(f"{letter} is a vowel")
#     else:
#         print(f"{letter} is a consonant")


for letter in name:
    print(f"{letter} {'is a vowel' if letter.lower() in ['a', 'e', 'i', 'o', 'u'] else 'is a consonant'}")          # 这里 list 中的元音字母必须要用单引号，不能用双引号，否则会出 syntax error

