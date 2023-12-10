"""
## Challenge 8: Continue Statement
- Implement a for loop to print odd numbers from 1 to 10, but skip printing 5
"""
for i in range(1, 11):
    if i == 5:
        continue
    elif i % 2 == 1:
        print(i)