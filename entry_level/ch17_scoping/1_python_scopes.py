
# When working inside a programming language, variables and objects that we are working with are only accessible within certain scopes

if 1 < 2:
    x = 5

while x < 6:
    print(x)
    x += 1

print(x)
# It's gonna print out:
# 5
# 6
# That's because conditionals and loops do not define their own scops


# This is a little different when it comes to functions

def set_a():
    a = 5

set_a()

while a < 6:    # NameError: name 'a' is not defined
    print(a)
    a += 1

# Functions and classes they define their own scope - that means a variable that creates inside a function remains inside the function
# 对于以上，we are not able to access a where a is only set inside the set_a() function



# 自己加的, 作为之前 “conditionals and loops do not define their own scops” 的补充
num = 1
if 1 < 2:
    print("num inside if:", num)   # num inside if: 1
    num = 22
print(num)         # 22


