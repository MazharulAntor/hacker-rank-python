import textwrap


def wrap(string, max_width):
    wrapped_string = textwrap.wrap(string, max_width)
    new_string = ""
    for line in wrapped_string:
        if new_string == "":
            new_string = line
        else:
            new_string = new_string + '\n' + line
    return new_string


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
