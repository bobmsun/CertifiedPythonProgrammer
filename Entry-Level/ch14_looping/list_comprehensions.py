

# Want to take a list/sequence, go through each item, make some sort of modification to it, 
# and end up having a list containing all those modified item at the end 
# 这时就可以用 list comprehension, python 的一个 feature，并不是所有其他编程语言都有这样的 feature

colors = ['red', 'blue', 'orange', 'green', 'yellow']
uppercase_colors = []

for color in colors:
    uppercase_colors.append(color.upper())

print(uppercase_colors)
# ['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']



# list comprehension
colors = ['red', 'blue', 'orange', 'green', 'yellow']
uppercase_colors = [color.upper() for color in colors]    # put a for loop inside the list and write what we want to do
print( uppercase_colors )
# ['RED', 'BLUE', 'ORANGE', 'GREEN', 'YELLOW']



# Another benefit of using list comprehension is used for filtering
warm_colors = []
for color in colors:
    if color in ['red', 'orange', 'yellow']:
        warm_colors.append(color)
print( warm_colors )
# ['red', 'orange', 'yellow']


# Can achieve exactly the same thing by using list comprehension
warm_colors = [color for color in colors if color in ['red', 'orange', 'yellow']]     # more reads like a sentence
print( warm_colors )
# ['red', 'orange', 'yellow']




