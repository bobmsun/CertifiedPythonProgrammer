
__all__ = ['extract_upper']   # set this to be a list of strings that are the names that we want to be available when someone goes and 
                              # imports * from our module

def extract_upper(phrase):
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))


if __name__ == "__main__":
    print("HELLO FROM HELPERS")


# __name__ is a built-in variable which evaluates to the name of the current module. 
# Thus it can be used to check whether the current script is being run on its own or 
# being imported somewhere else by combining it with if statement, as shown below.
# if __name__ == "__main__": 
#     print ("File1 is being run directly")
# else: 
#     print ("File1 is being imported")
