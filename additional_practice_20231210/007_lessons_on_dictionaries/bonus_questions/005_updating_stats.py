"""
character_info[character_name: str, dict[info_key: str, value: Any]]
"""
from typing import Any

character_info: dict[str, dict[str, Any]] = {
    "weixuan9595": {
        "job": "warrior",
        "str": 999,
        "int": 999,
        "dex": 4,
        "luk": 4,
        "inventory": []
    },
    "aaronongtongong": {
        "job": "hunter",
        "str": 93,
        "int": 999,
        "dex": 50,
        "luk": 4,
        "inventory": []
    },
    "xiaoclemz": {
        "job": "pirate",
        "str": 999,
        "int": 60,
        "dex": 32,
        "luk": 4,
        "inventory": []
    }
}

aaron_dict: dict[str, Any] = character_info["aaronongtongong"]
aaron_dict["str"] += 5
character_info["weixuan9595"]["job"] = "Spearman"
character_info["weixuan9595"]["inventory"].append(
    {
        "item name": "zakum helm",
        "quantity": 1
    }
)
print(character_info)
