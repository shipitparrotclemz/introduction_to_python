"""
dict["level_key": str,
    list[
        dict[monster_info_key, monster_info]
    ]
]
"""

from typing import Any

ludibrium_pq_monsters: dict[str, list[dict[str, Any]]] = {
    "level_one": [
        {
            "ratz": {
                "level": 35,
                "hp": 1050,
                "weakness": ["fire", "ice"],
                "quantity": 50,
            }
        },
        {
            "black ratz": {
                "level": 35,
                "hp": 1050,
                "weakness": ["fire", "ice"],
                "quantity": 20,
            }
        },
    ]
}

level_one: list[dict[str, Any]] = ludibrium_pq_monsters["level_one"]
ratz_dictionary: dict[str, Any] = level_one[0]
inner_ratz_dictionary: dict[str, Any] = ratz_dictionary["ratz"]
"""
Challenge 1: Increment quantity of ratz by 50
ratz quantity should now be 100
"""
