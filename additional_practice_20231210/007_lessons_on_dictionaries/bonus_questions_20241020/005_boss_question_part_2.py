"""
Getting an input from the user

Check if the user wants to
1) list all skills
2) add a skill
3) update a skill
4) delete a skill

Implement it all
"""

from typing import Any

skill_tree: dict[str, Any] = {
    "warrior": {
        "skills": {"Sword Mastery": {"max_level": 20, "damage_multiplier": 0.0}}
    },
    "magician": {"skills": {}},
    "archer": {"skills": {}},
    "thief": {"skills": {}},
}


while True:
    input_str: str = input(
        """Please enter
- 1 to list all skills
- 2 to add a skill
- 3 to update a skill
- 4 to delete a skill
    """
    )
    if input_str == "1":
        print("Listing all skill")
        all_classes: list[str] = list(skill_tree.keys())
        print(f"Possible classes: {all_classes}")
        job_input: str = input("Please enter a class\n")
        skill_tree_dict: dict[str, Any] = skill_tree[job_input]["skills"]
        skills: list[str] = list(skill_tree_dict.keys())
        print(skills)
    elif input_str == "2":
        print("Adding a skill")
    elif input_str == "3":
        print("Updating a skill")
    elif input_str == "4":
        print("Deleting a skill")
    else:
        print("Invalid Input")
