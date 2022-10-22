

# Occasionally, we want functions to behave like iterators
# benifit of "range" - we can just get the next item and not have to calcuate all the items in the big list that we are working with

# generator is very similar to range. We are gonna reimplement the range function using generator ourselves

def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num       # when we hit this "yield", it will work like a "return" essentially. Once it's returned, it's gonna stop right mid executions, 
                        # so it's not gonna continue on with the loop. It's gonna pause right here util we ask it for the next item.
                        # Then it will pick where we left off and continue on and yield again
                        # This is how we can build a function that can behave like a iterator. Becuase we just need the function to be able to pause
                        # temporarily and yield us the next item the next we ask for one.
        num += step 
        

generator = gen_range(5)

print( next(generator) )    # 1
print( next(generator) )    # 2
print( next(generator) )    # 3
print( next(generator) )    # 4
print( next(generator) )    # 5

# print( next(generator) )    # Error: StopIteration


# In practice, the way we are gonna use this would be something like this:
for num in gen_range(10, step=2):
    print(num)
# 1
# 3
# 5
# 7
# 9
# The way taht "for" works is that it's gonna continue to call "next" until it would have run into a StopIteration error
# and then it's gonna consider it to be completed

# So we won't mannally call the "next" function very often, we will just use it in the context of a "for" loop or what we will 
# find out in the next lesson (just turn our generator directly into a list)


# 自我 research
a_num = 33
def change_value(a_num):
    a_num = 35
change_value(33)
print( a_num )     # 33


# 自我 research - "yield" keyword in python
# from "GreeksforGreeks"
# The yield statement suspends a function’s execution and sends a value back to the caller, 
# but retains enough state to enable the function to resume where it left off. 
# When the function resumes, it continues execution immediately after the last yield run. 
# his allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.

