def gen_range(stop, start=1, step=1):
    num = start
    while num <= stop:
        yield num
        num += step 

# we can load this function into the interpreter by using the -i flag and then the name of the file

# python -i entry_level/ch16_generators/gen.py

# -i flag 必须得放在 file path 前面，发在后面（python entry_level/ch16_generators/gen.py -i）就会相当于没有 -i flag