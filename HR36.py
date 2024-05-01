from collections import namedtuple

number = int(input())
columns = input().split()
avg = 0
Student = namedtuple("Student", f"{columns[0]}, {columns[1]} ,{columns[2]}, {columns[3]}")
for i in range(number):
    details = input().split()
    data = Student(details[0], details[1], details[2], details[3])
    avg += int(data.MARKS)
print(round((avg / number), 2))
