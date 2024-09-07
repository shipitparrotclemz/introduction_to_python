"""
Create a list from 1 to 100

then, shuffle with random.shuffle
"""

import random

my_list: list[int] = [num for num in range(1, 101)]
random.shuffle(my_list)
print(my_list)