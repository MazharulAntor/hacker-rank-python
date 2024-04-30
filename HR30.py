from itertools import permutations

string, size = input().split()
size = int(size)

p_list = list(permutations(string, size))
p_list.sort()

for x in p_list:
    for i in x:
        print(i, end="")
    print("")
