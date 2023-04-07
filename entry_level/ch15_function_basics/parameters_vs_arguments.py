
# There is difference between parameter and argument

def contact_card(name, age, car_model):   # These are parameters. These are the variables we define when we define the function itself
    return f"{name} is {age} and drives a {car_model}"


# Argument exists at the time calling the function

# Positional argument
print( contact_card("Keith", 29, "Honda Civic") )

# keyword argument
# 这样就可以 mess up parameter 的 position
print( contact_card(age=29, car_model="Honda Civic", name="Keith") )

# can miss positional argument with keyword argument
# 一旦用了 keyword argument，后面就都要用 keyword argument
print( contact_card("Keith", car_model="Honda Civic", age=29) )


# contact_card(age=29, "Keith", car_model="Civic")   SyntaxError: positional argument follows keyword argument
# 3 ways:
# Can use all positional argument
# Can use all keyword argument
# Can put positonal argument first and then keywork argument


# keyword argument -> functions with default argument
def can_drive(age, driving_age=16):
    return age >= driving_age


print( can_drive(29) )      # True   don't need to explicitly specify driving_age, since it has default value


print( can_drive(16, driving_age=18) )     # False    If you have a very long list of argument that has default and you only want to modify the value of one of them, you can do this

print( can_drive(16, 18) )          # False

# 自己加
print( can_drive(driving_age=22) )       # TypeError: can_drive() missing 1 required positional argument: 'age'

# def can_drive(age, driving_age=16, vehicle_type):
#     pass
# Syntax Error: non-defult argument follows default argument
# 如果有一个 parameter 是 default argument，剩下的(之后的)所有 argument 都得是 default argument

