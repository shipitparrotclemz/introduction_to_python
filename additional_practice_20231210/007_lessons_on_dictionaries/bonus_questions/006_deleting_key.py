from typing import Any

character_info: dict[str, dict[str, Any]] = {
    "mr_yandao": {
        "job": "thief",
        "str": 999,
        "int": 999,
        "dex": 4,
        "luk": 4,
        "inventory": []
    },
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
        "job": "scammer",
        "str": 999,
        "int": 60,
        "dex": 32,
        "luk": 4,
        "inventory": []
    }
}
item_popped: dict[str, Any] = character_info.pop("xiaoclemz", {})
print(item_popped)
print(character_info)