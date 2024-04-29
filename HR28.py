A = list(map(int, input().split()))
B = list(map(int, input().split()))

new_list = []
for x in A:
    for y in B:
        new_list.append((x, y))

for z in new_list:
    print(z, end=" ")
