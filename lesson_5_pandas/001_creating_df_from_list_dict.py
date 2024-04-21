import pandas as pd

my_list: list[dict[str, str]] = [
    # name,likes
    # xuan,chocolate cake
    # aaron,taiwan girls
    # clement, short taiwan girls
    # elson,scam auntie money
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