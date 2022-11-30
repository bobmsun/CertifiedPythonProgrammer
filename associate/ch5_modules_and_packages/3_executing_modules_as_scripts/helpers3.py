
def extract_upper(phrase):
    return list(filter(str.isupper, phrase)) 


def extract_lower(phrase):
    return list(filter(str.islower, phrase))


if __name__ == "__main__":    # 加这行之后的意思是：只有run helper3.py 这个 script 时 __name__ 的值 才是 __main__，才会 print 这行; 在 main.py import helpers3 的时候，这行就不会被打印出来
    print("HELLO FROM HELPERS")

