import random

my_list: list[int] = []

for i in range(10):
    my_list.append(random.randint(1, 10))

print(my_list)