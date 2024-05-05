import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("009_salary.csv")
    # let's print out the types of each column
    print(df.info())
    # we can see the name is inferred as "object", a generic mixed type
    # I.E, it means pandas dunno what the heck this type is
    # we can see the salary is correctly inferred as "int64"
    # this means an integer that can store -2**63 to 2**63
    # that is -9.223372e+18 to 9.223372e+18
    # now, we will purposely set "name" column to "string"
    df["name"] = df["name"].astype("string")
    print(df.info())