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
    },
    {
        "name": "elson gorgor", "likes": "scam auntie money",
    }
]

df: pd.DataFrame = pd.DataFrame(my_list)

"""
1D column of booleans, of the same length as number of rows
Gives back
False
False
False
True
False
"""
equal_elson: pd.Series = df["name"] == "elson"
print("equal_elson")
print(equal_elson)

# filter for only rows whose name is equal "elson" + all columns
# notice loc takes in the following syntax
# [boolean_series, list_of_columns names]
filtered_df: pd.DataFrame = df.loc[equal_elson, ["name", "likes"]]
print("filtered_df")
print(filtered_df)