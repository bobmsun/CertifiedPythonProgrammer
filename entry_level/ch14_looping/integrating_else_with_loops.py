
# while-else: the code get executed anytime the loop finishes successfully

count = 1
while count <= 4:
    print(count)
    count += 1
else:
    print("While loop completed")
# 1
# 2
# 3
# 4
# While loop completed



for i in [1, 2, 3, 4, 5]:
    print(i)
else:
    print("For loop completed")
# 1
# 2
# 3
# 4
# 5
# For loop completed



# The real power of for-else loop comes in when we want to conditionally break out the loop we are in
# and this could be useful if we want to do something like search
colors = ['red', 'pink', 'blue', 'orange', 'green']
for color in colors:
    if color == 'orange':
        print('Orange is in the list')
        break     # if we hit this line, the else content is never going to be executed
else:
    print("Orange is not in the list")

# Orange is in the list

# You never want to use the else block unless you are explicitly using "break" inside the loop you are working with



for color in colors:
    if color == 'green':
        print('Green is in the list')
        break     # if we hit this line, the else content is never going to be executed
else:
    print("Green is not in the list")

# Green is in the list