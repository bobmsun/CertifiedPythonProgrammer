
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue     # stop the execution of the loop for the current iteration and go to the next iteration
    print(f"We're counting odd numbers: {count}")     # f string: kind of like a shortcut of format
    count += 1

# We're counting odd numbers: 1
# We're counting odd numbers: 3
# We're counting odd numbers: 5
# We're counting odd numbers: 7
# We're counting odd numbers: 9


count = 1
while count < 10:
    if count % 2 == 0:
        break                # Stop the excution of the loop entirely
    print(f"We're counting odd numbers: {count}")
    count += 1

# We're counting odd numbers: 1


colors = ['blue', 'green', 'red', 'purple']
for color in colors:
    if color == 'blue':
        continue
    elif color == 'red':
        break 
    print(color)

# green




