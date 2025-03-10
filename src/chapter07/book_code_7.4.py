import re


def main():
    sample_text = '''See the U.S.A. today. It's right here, not a world 
        away. Average temp. is 66.5.'''
    pattern = r'[A-Z].*?[.!?](?= [A-Z]|$)'
    matches = re.findall(pattern, sample_text, flags=re.DOTALL | re.MULTILINE)
    for match in matches:
        print('->', match)


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
