"""
dict[str, dict[str, str]]

dict[customer_name, dict[detail_name, detail_value]]

"""

from typing import Any

names_to_drinks_map: dict[str, dict[str, Any]] = {
    "weixuan": {
        "name": "matcha latte",
        "instructions": "6 scoops of matcha instead",
        "quantity": 2,
    }
}
print(names_to_drinks_map)
