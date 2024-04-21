import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("002_my_file.csv")
    print(df)