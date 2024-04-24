def split_and_join(line):
    x = line.split(" ")
    newString = "-".join(x)
    return newString


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
