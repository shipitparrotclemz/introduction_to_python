"""
## Challenge 2: Nested If-Else Statement
- Define an integer object age and assign its value to 18
- Implement a nested if-else statement to check if age is greater than 18 or equal to 18
- If greater, print "You are an adult"
- Else if equal, print "You are a teenager"
- Else, print "You are a child"
"""

age: int = 18
if age > 18:
    print("You are an adult")
elif age == 18:
    print("You are a teenager")
else:
    print("You are a child")
