"""
Create a skill tree for jobs
"""

import time
from typing import Any

skill_tree: dict[str, dict[str, dict[str, dict[str, Any]]]] = {
    "warrior": {
        "skills": {
            "power strike": {"max_level": 20, "damage_multiplier": 500, "hits": 1},
            "sword mastery": {"max_level": 20, "damage_multiplier": 0, "hits": 0},
        }
    },
    "archer": {
        "skills": {
            "double shot": {"max_level": 20, "damage_multiplier": 500, "hits": 2}
        }
    },
}

# New concepts:
# 1. while <bool>
# 2. time.sleep(1) -> allows you to wait for 1 second before running
# 3. input() -> stops the program and wait for a str input from user. save the result into a variable
# 4. \n -> new line character
# 5. call .keys() on a dict, to get all keys only

"""
Create a script which can support the following operations:

Take in a Job
Take in a number
- 0 -> list all skills
- 1 -> add a skill
- 2 -> update a skill
- 3 -> delete a skill

1. List all skills for a given class, along with it's stats
    - max level
    - damage multiplier
    - hits
    
2. Add a skill
    - Add the skill name
    - Add the three stats (max_level, damage_multiplier, hits)
    
3. Update a skill
    - for the skill name
    - ask for the stat to update
    - after updating, ask user to type Y to continue, else N to go back to main menu
    
4. Delete a skill
    - ask for skill name
    - prompt user if he really wants to delete, Y to delete, N to not delete
    - ask for another skill to delete, Y to continue, N to delete
    - if N, go back to main menu
"""
while True:
    job: str = input("Please enter your job:\n").lower()
    print(f"Received Job: {job}")
    number_description: str = """
Please enter your operation:
0 to list all skills
1 to add a skill
2 to edit a skill
3 to delete a skill
"""
    operation: int = int(input(number_description))
    print(f"Received operation: {operation}")
    if operation == 0:
        # List all skills
        skills_dict: dict[str, Any] = skill_tree[job]["skills"]
        skills: list[str] = list(skills_dict.keys())
        for skill_index in range(len(skills)):  # 0 to len(skills) - 1
            print(f"Skill {skill_index}: {skills[skill_index]}")
    else:
        print("Unimplemented. Skipping.")
