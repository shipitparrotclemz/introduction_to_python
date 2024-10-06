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
import time
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

# New concepts:
# 1. while <bool>
# 2. time.sleep(1) -> allows you to wait for 1 second before running
while True:
    time.sleep(1)  # wait for 1 second befor running
    print("Please enter your input")