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
# 3. input() -> stops the program and wait for a str input from user. save the result into a variable
# 4. \n -> new line character
while True:
    input_from_user: str = input("Please enter your job:\n")
    print(f"Received input: {input_from_user}")
