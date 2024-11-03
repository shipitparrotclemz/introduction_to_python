"""
## Challenge 6: Removing Elements from a List
- Define a list object my_list containing integers 10, 20, 30, 40, 50
- Remove 30 from my_list
- Print my_list

WARNING: pop() method on list is expensive, and requires a full iteration of the list in the worst case
- After popping an element e.g at index 2 (3rd item), it needs to move 4th and 5th item forward
- The worst case happens when pop() receives index 0
- It needs to move all N-1 items in the list forward
- The python interpreter / implementation of pop() needs to iterate from front to back to move all items forward

We usually don't use it in technical interviews
"""

my_list: list[int] = [10, 20, 30, 40, 50]
my_list.pop(2)
print(my_list)
