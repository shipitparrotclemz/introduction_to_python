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

# E.G print from 1 to 10 with a while loop
start: int = 1
end: int = 10
while start <= end: # 11 <= 10 -> False
    print(start)    # print(10)
    start += 1      # start = 11