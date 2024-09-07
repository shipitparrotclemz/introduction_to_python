"""
Create a random list of numbers

[1, ... 100] then shuffle

print it

then sort it with strategy 1: .sort() on list (in-place)

hint: don't use sorted(), that is way 2, it creates a copy, we don't want that
"""
import random

my_list: list[int] = [num for num in range(1,101)]
random.shuffle(my_list)
print(my_list)

my_list.sort()
print(my_list)