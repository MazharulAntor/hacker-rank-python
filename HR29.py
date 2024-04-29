no_of_shoes = int(input())
shoe_sizes_list = list(map(int, input().split()))
no_of_customers = int(input())
desired_customer = []
amount = 0
for i in range(no_of_customers):
    size, price = map(int, input().split())
    desired_customer.append((size, price))

for i in range(len(desired_customer)):
    if desired_customer[i][0] in shoe_sizes_list:
        amount += desired_customer[i][1]
        shoe_sizes_list.remove(desired_customer[i][0])

print(amount)
