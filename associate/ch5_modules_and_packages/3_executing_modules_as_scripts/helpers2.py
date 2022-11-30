
def extract_upper(phrase):
    return list(filter(str.isupper, phrase)) 


def extract_lower(phrase):
    return list(filter(str.islower, phrase))


print("HELLO FROM HELPERS")

print(f"__name__ in helpers2.py: {__name__}")
