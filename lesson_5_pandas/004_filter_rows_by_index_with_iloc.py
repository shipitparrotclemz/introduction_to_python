import pandas as pd
from typing import Any

my_list: list[dict[str, Any]] = [
    {
        "name": "xuan",
        "likes": "chocolate cake",
    },
    {
        "name": "aaron",
        "likes": "taiwan girls",
    },
    {
        "name": "clement",
        "likes": "short taiwan girls",
    },
    {
        "name": "elson",
        "likes": "scam auntie money",
    },
]

df: pd.DataFrame = pd.DataFrame(my_list)

# filter for only 1st and 2nd row, all columns
# notice iloc takes in the following syntax
# [range_of_row_index, range_of_col_index]
# 0:2 -> index 0 to index 1, exclusive of 2
# : -> all columns
filtered_df: pd.DataFrame = df.iloc[0:2, :]
print(filtered_df)
