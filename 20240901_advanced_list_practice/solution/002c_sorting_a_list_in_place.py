# step 1: generate list of random numbers
import random

my_list: list[int] = [random.randint(1, 10) for i in range(10)]
print(my_list)
# step 2: sort
my_list.sort()
print(my_list)
