"""
Challenge 6: Using the range() magic wand
print out 100 to 1_000_000
"""

# for num in range(100, 1000001):  # start: 100 end: 999999
#     print(num)

"""
Challenge 7: Using the range() magic wand
print out 1_000_000 to 0
"""
# for num in range(1000000, -1, -1):
#     print(num)

"""
Challenge 8: Using the range() magic wand
print out 0,5,10
"""
# for num in range(0, 100, 5):
#     print(num)

"""
Challenge 9: Using the range() magic wand
print out odd numbers from 0 to 100
1,3,5...99
"""
# for num in range(1, 100, 2):
#     print(num)
#
for num in range(1, 100):
    if num % 2:
        print(num)