"""
Challenge 11:

Print out 0,2,4,6,8,10,12,14,...100

Concept: If you need a step, even if your start is 0
you still need to specify it

otherwise
you will do range(100,2)
and python mistake 100 for start instead of end
and 2 as end instead of step
"""
for i in range(0,101,2):
    print(i)