import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("wage_bros.csv")
    # give me back rows of index 0, 1 and 2 (first 3 rows) -> 0:3
    # and all columns -> :
    filtered_df: pd.DataFrame = df.iloc[0:3, :]
    print(filtered_df)
