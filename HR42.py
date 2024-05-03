eng_sub = int(input())
eng_rolls = set(map(int, input().split()))
fr_sub = int(input())
fr_rolls = set(map(int, input().split()))

roll_students = eng_rolls - fr_rolls
print(len(roll_students))
