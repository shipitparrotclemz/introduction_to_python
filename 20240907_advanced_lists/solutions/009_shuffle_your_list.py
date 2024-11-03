import random

my_list: list[int] = [num for num in range(1, 101)]
random.shuffle(my_list)
print(my_list)
