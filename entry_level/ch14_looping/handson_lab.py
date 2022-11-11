

upper_number = int(input("How many values should we process: "))

for number in range(1, upper_number + 1):    # 因为 range 函数的上界不是 inclusive 的
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

