from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(n):
    d["A"].append(input())
for i in range(m):
    d["B"].append(input())

for i in range(len(d["B"])):
    if d["B"][i] in d["A"]:
        for j in range(len(d["A"])):
            if d["B"][i] == d["A"][j]:
                print(j + 1, end=" ")
    else:
        print("-1", end=" ")
    print("")
