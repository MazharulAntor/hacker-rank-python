T = int(input())
values = []
for i in range(T):
    a, b = input().split()
    values.append((a, b))

for i in range(len(values)):
    try:
        print(int(values[i][0]) // int(values[i][1]))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
