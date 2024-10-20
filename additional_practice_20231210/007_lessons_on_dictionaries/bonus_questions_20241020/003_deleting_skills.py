from typing import Any

"""
Challenge 3:
- Delete Sword Mastery

Step 2: Navigate

Step 2: Delete
- pop("Sword Mastery")
"""

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