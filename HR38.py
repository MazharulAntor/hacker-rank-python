total_stamps = int(input())

country = set()
for i in range(total_stamps):
    name = input()
    country.add(name)
print(len(country))
