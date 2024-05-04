n = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command, length = input().split()
    values = set(map(int, input().split()))
    if command.startswith("intersection_update"):
        A &= values
    elif command.startswith("update"):
        A |= values
    elif command.startswith("symmetric_difference_update"):
        A ^= values
    elif command.startswith("difference_update"):
        A -= values
print(sum(A))
