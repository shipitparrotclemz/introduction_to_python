"""
A maplestory character has 4 types of stats
- str: int
- int: int
- dex: int
- luk: int

job
- magician / warrior / pirate / thief / archer: str
"""

from typing import Any

"""
dict[
    character_name, dict[
        stat_name, list[
            dict[
                item_stat: item_value
            ]
        ]
    ]
]
"""
character_info: dict[str, dict[str, Any]] = {
    "weixuan": {
        "str": 100,
        "int": 100,
        "dex": 50,
        "luk": 10,
        "job": "thief",
        "inventory": [
            {
                "item name": "topaz ore",
                "quantity": 100
            },
            {
                "item name": "green mushroom cap",
                "quantity": 100
            }
        ]
    },
    "aaron": {
        "str": 90,
        "int": 100,
        "dex": 70,
        "luk": 40,
        "job": "magician",
        "inventory": [
            {
                "item_name": "jr balrog's hat",
                "quantity": 1
            },
            {
                "item_name": "elemental wand",
                "quantity": 1
            }
        ]
    },
    "clement": {
        "str": 999,
        "int": 90,
        "dex": 40,
        "luk": 70,
        "job": "archer",
        "inventory": []
    },
}

print(character_info)
