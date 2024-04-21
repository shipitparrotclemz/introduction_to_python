import pandas as pd
from typing import Any

my_list: list[dict[str, Any]] = [
    {
        "name": "xuan", "likes": "chocolate cake",
    },
    {
        "name": "aaron", "likes": "taiwan girls",
    },
    {
        "name": "clement", "likes": "short taiwan girls",
    },
    {
        "name": "elson", "likes": "scam auntie money",
    }
]

df: pd.DataFrame = pd.DataFrame(my_list)
print(df)