from datetime import datetime


def time_delta(t1, t2):
    frmt = "%a %d %b %Y %H:%M:%S %z"
    x = datetime.strptime(t1, frmt)
    y = datetime.strptime(t2, frmt)

    return int(abs(x - y).total_seconds())


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)
