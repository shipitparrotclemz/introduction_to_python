"""
Now, you dont know if the list is even or odd length

create one list, let it be even or odd

assume you don't know it's length if it is even or odd

give a solution to get it's median

hint: you have to check if it's length is even or odd

then use if-else statement to decide if you should use odd or even solution

hint:
is_even: bool = len(my_list) % 2 == 0
"""

import random

# NEW CONCEPT: CREATING A RE-USABLE PIECE OF CODE
# WRITING YOUR OWN FUNCTION
"""
def <function_name>(param_name: <type_hint>, param_two_name: <type_hint>) -> <output_type_hint>:
    pass
    
def add(num_one: int, num_two: int) -> int:
    return num_one + num_two
    
We are going to create a function that automatically generates a random size list
"""
# my_list: list[int] = [num for num in range(1, 100)]


def generate_test_case() -> list[int]:
    length_of_list: int = random.randint(50, 100)
    list_to_generate: list[int] = [num for num in range(1, length_of_list + 1)]
    random.shuffle(list_to_generate)
    return list_to_generate


test_case_one_list: list[int] = generate_test_case()
print(test_case_one_list)
print(len(test_case_one_list))

# write a solution to get the median of this list above ^
# rmb to sort it first, before doing anything
# rmb to check the length if its even or pdd
# rmb to use if-else statements to decide which solution to use

test_case_one_list.sort()
length_of_list: int = len(test_case_one_list)
is_my_list_even: bool = length_of_list % 2 == 0

if is_my_list_even:
    right_index: int = len(test_case_one_list) // 2
    left_index: int = (right_index) - 1
    right_item: int = test_case_one_list[right_index]
    left_item: int = test_case_one_list[left_index]
    median_of_list: float = (right_item + left_item) / 2

else:
    index_of_list: int = len(test_case_one_list) // 2
    median_of_list: int = test_case_one_list[index_of_list]

print(median_of_list)
