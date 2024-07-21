import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("009_salary.csv")
    # let's print out the types of each column
    print(df.info())
