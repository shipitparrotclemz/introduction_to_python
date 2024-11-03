"""
Getting an input from the user

Check if the user wants to
1) list all skills
2) add a skill
3) update a skill
4) delete a skill
"""

input_str: str = input(
    """Please enter
- 1 to list all skills
- 2 to add a skill
- 3 to update a skill
4 to delete a skill
"""
)

if input_str == "1":
    print("Listing all skill")
elif input_str == "2":
    print("Adding a skill")
elif input_str == "3":
    print("Updating a skill")
elif input_str == "4":
    print("Deleting a skill")
else:
    print("Invalid Input")
