
__all__ = ['extract_upper']   # set this to be a list of strings that are the names that we want to be available when someone goes and 
                              # imports * from our module

def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))


if __name__ == "__main__":
    print("HELLO FROM HELPERS")
