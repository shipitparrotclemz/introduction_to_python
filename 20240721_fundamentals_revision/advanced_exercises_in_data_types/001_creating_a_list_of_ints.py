# Create a list of the following numbers
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Prerequisites:
# range(1, 11) -> 11 is exclusive


## Optional: Strategy 1: Use list-compressions
# being comfortable with list-comprehensions
# [num for num in range(1, 11)]


## For loop, and append
my_list: list[int] = []
for num in range(1, 11):
    my_list.append(num)

my_second_list: list[int] = [num for num in range(1, 11)]

print(my_list)
print(my_second_list)
