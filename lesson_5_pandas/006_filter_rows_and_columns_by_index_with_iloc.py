import pandas as pd
from typing import Any

my_list: list[dict[str, Any]] = [
    {"name": "xuan", "likes": "chocolate cake", "age": 29},
    {"name": "aaron", "likes": "taiwan girls", "age": 29},
    {"name": "clement", "likes": "short taiwan girls", "age": 29},
    {"name": "elson", "likes": "scam auntie money", "age": 29},
]

df: pd.DataFrame = pd.DataFrame(my_list)
print("df")
print(df)

# filter for only 1st and 2nd col, 1st and 2nd rows
# notice iloc takes in the following syntax
# [range_of_row_index, range_of_col_index]
# 0:2 -> index 0 to index 1, exclusive of 2
# notice we only get the 1st and 2nd column and rows; name and likes
# no age column; thats the 3rd column
filtered_df: pd.DataFrame = df.iloc[0:2, 0:2]
print("filtered_df")
print(filtered_df)
