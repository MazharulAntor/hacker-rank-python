def print_rangoli(size):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    pattern = ""
    counter = size
    pattern_list = []
    for i in range(size - 1, -1, -1):
        counter -= 1
        for j in range(i, counter - 1, -1):
            pattern += alphabet[j] + "-"
            pattern_list.append(pattern)
    if size == 1:
        val = pattern_list[0]
        pattern_list[0] = val[:len(val) - 1]

    pattern_list2 = pattern_list.copy()
    pattern_list3 = pattern_list.copy()

    for i in range(len(pattern_list3)):
        val = pattern_list3[i]
        pattern_list3[i] = val[:len(val) - 1]

    for i in range(len(pattern_list3)):
        val = pattern_list3[i]
        pattern_list3[i] = val[::-1]

    for i in range(len(pattern_list) - 1):
        pattern_list[i + 1] = pattern_list2[i + 1] + pattern_list3[i]

    for x in pattern_list:
        print(x.center((size - 1) * 4 + 1, "-"))

    pattern_list.reverse()
    for i in range(len(pattern_list) - 1):
        print(pattern_list[i + 1].center((size - 1) * 4 + 1, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
