import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("wage_bros.csv")
    # dtype is an attribute of the pd.Series
    # df is an object of type pd.DataFrame
    # cat is an object of type Cat
    # attribute is analogous to the name of a cat
    # we are printing it
    # object -> a generic type
    print(df["name"].dtype)