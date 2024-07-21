import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("wage_bros.csv")
    new_name_column_of_type_str: pd.Series = df["name"].astype("string")
    # new type
    print(new_name_column_of_type_str.dtype)
    # you have to assign this new column back to the dataframe
    df["name"] = new_name_column_of_type_str
    # check to be sure the dataframe takes the new column
    print(df["name"].dtype)
