def pattern(n, m, pos):
    if pos == "top":
        for i in range(n // 2):
            print((".|." * (i * 2 + 1)).center(m, "-"))
    else:
        for i in range(n // 2 - 1, -1, -1):
            print((".|." * (i * 2 + 1)).center(m, "-"))


if __name__ == '__main__':
    n, m = map(int, input().split())

    pattern(n, m, "top")
    print("WELCOME".center(m, "-"))
    pattern(n, m, "bottom")
