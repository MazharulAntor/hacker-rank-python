def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string)):
        position = string.find(sub_string, i, len(string))
        if position != -1:
            i = position + 1
            counter += 1
            print(position)

    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
