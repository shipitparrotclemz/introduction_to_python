"""
character_info[character_name: str, dict[info_key: str, value: Any]]
"""

from typing import Any

character_info: dict[str, dict[str, Any]] = {
    "weixuan9595": {"str": 999, "int": 999, "dex": 4, "luk": 4},
    "aaronongtongong": {"str": 93, "int": 999, "dex": 50, "luk": 4},
    "xiaoclemz": {"str": 999, "int": 60, "dex": 32, "luk": 4},
}

aaron_info: dict[str, Any] = character_info["aaronongtongong"]
aaron_int: int = aaron_info["int"]
print(aaron_int)
