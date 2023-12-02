"""
Creating a range object
- start (int)   = 0
- end (int)     = 4
- curr (int)    = 4

think of a range object as a lazy list
it is lazy as it doesn't store all numbers from start to end - 1
- it only keeps track of the current number (curr)

Q: What is the difference between list vs range?

[0,1,2,3,4] vs range(0,5)   3 * 4 bytes = 12 bytes

A: List is very expensive in memory
- if the list contains 10 items, it uses ~4 bytes * 10  = 40 bytes

Concept:
1 byte = 8 zeros (can only be zero or one)
00000000
"""

my_range_object: range = range(0, 4)
print(my_range_object)

"""
Q: Can i make range store strings?
A: NO :')
"""