"""
Challenge 10:

10,000 to 0
"""
# range_object: range = range(10, -1, -1)
# for i in range_object:
#     print(i)
#
# for i in range_object:
#     print(i)

"""
Concept: range
- start
- end
- step (what step to move)

Q: Can i reuse a range object with start = 0 end = 10 step = 1
for iterating 10,9,8...0

A: No

iterating 10,9,8...0
start 10
end -1
step -1

range can be reused
"""

for i in reversed(range(10000, -1, -1)):
    print(i)