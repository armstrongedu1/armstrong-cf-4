num_of_items = int(input())
num_of_days = int(input())

total_num_of_items = num_of_items

i = 0
while i < num_of_days:
    total_num_of_items *= 2
    i += 1

print(total_num_of_items)
