"""
## Challenge 3: If-Elif-Else Statement
- Define an integer object marks and assign its value to 85
- Implement an if-elif-else statement to determine the grade based on marks
- If marks is greater than or equal to 90, print "Grade A"
- Else if marks is greater than or equal to 80, print "Grade B"
- Else if marks is greater than or equal to 70, print "Grade C"
- Else, print "Grade D"
"""
marks: int = 85
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")
