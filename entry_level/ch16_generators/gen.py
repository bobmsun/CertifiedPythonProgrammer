def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step 

# we can load this function into the interpreter by using the -i flat and then the name of the file

