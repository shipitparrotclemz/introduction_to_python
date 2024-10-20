"""
Create a skill tree dictionary

Part 2: Add skill into skill tree

Warrior has a Power Strike skill

{
    "Power Strike": {
        "max_level": 20,
        "damage_multiplier": 5.0
    }
}
"""
from typing import Any

skill_tree: dict[str, Any] = {
    "warrior": {
        "skills": {
            "Sword Mastery": {
                "max_level": 20,
                "damage_multiplier": 0.0
            }
        }
    },
    "magician": {
        "skills": {}
    },
    "archer": {
        "skills": {}
    },
    "thief": {
        "skills": {}
    },
}

"""
Editing a nested dictionary has two steps to it
 
Step 1: Navigate to the right location you want to edit
- my_nested_dict = my_dict[key]

Step 2: Editing it
- my_dict[key] = value
"""
warrior_dict: dict[str, Any] = skill_tree["warrior"]
warrior_skill_dict: dict[str, Any] = warrior_dict["skills"]
warrior_skill_dict["Power Strike"] = {
    "max_level": 20,
    "damage_multiplier": 5.0
}


magician_dict: dict[str, Any] = skill_tree["magician"]
magician_skill_dict: dict[str, Any] = warrior_dict["skills"]
magician_skill_dict["Magic Claw"] = {
    "max_level": 20,
    "damage_multiplier": 3.0
}

print(skill_tree)

