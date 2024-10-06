"""
Create a skill tree for jobs

{
    "warrior": {
        "skills": {
            "power strike": {
                "max_level": 20,
                "damage_multiplier": 500,
                "hits": 1
            }
        }
    },
    "archer": {
        "skills": {
            "double shot": {
                "max_level": 20.
                "damage_multiplier": 500,
                "hits": 2
            }
        }
    }
}
"""
from typing import Any

skill_tree: dict[str, dict[str, dict[str, dict[str, Any]]]] = {
    "warrior": {
        "skills": {
            "power strike": {
                "max_level": 20,
                "damage_multiplier": 500,
                "hits": 1
            }
        }
    },
    "archer": {
        "skills": {
            "double shot": {
                "max_level": 20,
                "damage_multiplier": 500,
                "hits": 2
            }
        }
    }
}
