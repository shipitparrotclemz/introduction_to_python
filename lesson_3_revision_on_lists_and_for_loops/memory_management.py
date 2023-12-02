"""
How does python manage memory
"""
# my_string: str = "cheese"
# print(type(my_string))

"""
Concept:
- If we use the type magic wand on a variable
and we print out class 'str'

keyword is class
<class 'str'>

the variable is an object

for now, think of objects as conceptual boxes

Concept:
- In our machines, a box or object in memory (heap)
is given an address

an address can look something like this
- starts with 0x
- followed by some number

0x123

address is analogous to a HDB unit's address blk 226 #10-232
"""

"""
If we define a "cheese" string
we create the object in memory
but we don't store the address to it
"""

# my_string: str = "cheese"

"""
Concept:
Memory is not neceesarily assigned in sequence
- I.E, next address is not always the next number
0x123
0x124
"""

"""
Q: What is the difference in time taken
if we add an item to a list with .append

vs

recreating a list with that new item
"""

# my_list: list[str] = []
# my_list.append("cheese")

"""
Q: What if we .append("cheese_cake")?
A: We will create another box (variable) to store the "cheese_cake" object
we will then create another box to store the address of where "cheese_cake" object is
we put the second box into the list box
"""

"""
Pointer
- box that contain an addreess
"""

my_list: list[int] = [1, 2, 3]      # 0x123
my_another_list: list[int] = my_list    # 0X123

"""
Hypothesis
since my_list and my_another_list contains 0x123
pointing to the list in memory

if we append 4 to my_another_list and print 
- both my_another_list and my_list

both will print [1,2,3,4]
because both are pointing to the same list
"""
my_list.append(4)
print(my_list)  # [1,2,3,4]
print(my_another_list)  # [1,2,3,4]