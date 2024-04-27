def solve(s):
    new_list = s.split(" ")
    new_list2 = []
    for x in new_list:
        y = x.capitalize()
        new_list2.append(y)
    new_string = " ".join(new_list2)
    return new_string


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
