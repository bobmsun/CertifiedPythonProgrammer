
value = int(input("Enter an integer value: "))

if value % 3 == 0 and value % 5 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(value)

