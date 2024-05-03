n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command = input()
    if command.startswith("remove"):
        if int(command[7:]) in s:
            s.remove(int(command[7:]))
    if command.startswith("discard"):
        s.discard(int(command[8:]))
    if command.startswith("pop"):
        s.pop()
print(sum(s))
