import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("wage_bros.csv")
    # gives back another copy -> your df is not edited
    sorted_df: pd.DataFrame = df.sort_values(by=["name"], ascending=True)
    print("sorted_df")
    print(sorted_df)
    print("df -> to show you the original df is not edited")
    print(df)
