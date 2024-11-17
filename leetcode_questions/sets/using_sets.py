"""
Sets allow you to search for an item in O(1) time complexity;

No matter how large the set is, you still search it in constant number of operations

TLDR: you can quickly check if something exists in a set, very efficiently

Lets say I have a list of numbers, which can contain duplicates

I want to check if i have a number that is a duplicate

Strategy:
- Iterate through all numbers
- At every number, I check if the number exists in a set
- This set will represent numbers I have seen in the past
- If the number doesn't exist in the set
- I add it into the set, so next iteration can check if its the same as this
- Else, I early terminate and return False
"""

nums: list[int] = [1, 2, 3, 3]
past_numbers: set[int] = set()  # set([1, 2, 3])

has_duplicate: bool = False     # True
for num in nums:    # num = 3
    if num in past_numbers:     # True
        # you have a duplicate
        has_duplicate = True
        break
    else:
        past_numbers.add(num)

print(has_duplicate)    # True

