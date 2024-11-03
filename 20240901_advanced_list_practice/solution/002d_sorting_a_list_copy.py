import random

my_list: list[int] = [random.randint(1, 10) for i in range(10)]

print(my_list)

# create a sorted copy
my_sorted_list: list[int] = sorted(my_list)
print(my_sorted_list)

print(my_list)
