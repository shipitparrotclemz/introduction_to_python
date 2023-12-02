"""
Challenge 8:

New Concept:
- Advancing a range (lazy iterator)

range (lazy list)
- start = 0
- end = 4
- curr = 0

Concept:
use a for loop to advance the iterator

create a range object range(0,4)
use for loop to get items in a range
"""

my_range_object: range = range(1,4)

for num in my_range_object:
    print(num)

"""
0
1
2
3
"""