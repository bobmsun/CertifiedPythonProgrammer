

# open a file: touch closures.py

def geeter(prefix):
    def greet(name):
        print(f"{prefix} {name}")
    return greet


