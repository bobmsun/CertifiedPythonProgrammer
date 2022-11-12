
def _extract_upper(phrase):              # everything that starts with a _ will be marked as a pseduo hidden entity, a private entity
                                         # 这一点 apply to everything you can define and import, 例如 variable，class 也是这样
    return list(filter(str.isupper, phrase))

def extract_lower(phrase):
    return list(filter(str.islower, phrase))


if __name__ == "__main__":
    print("HELLO FROM HELPERS")
