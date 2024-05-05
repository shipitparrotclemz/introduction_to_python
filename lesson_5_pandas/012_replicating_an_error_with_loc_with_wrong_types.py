import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("009_salary.csv")
    # let's print out the types of each column
    print(df.info())
    # we can see the name is inferred as "object", a generic mixed type
    # I.E, it means pandas dunno what the heck this type is
    # we can see the age is correctly inferred as "int64"
    # this means an integer that can store -2**63 to 2**63
    # that is -9.223372e+18 to 9.223372e+18
    # now, we will purposely set "salary" column to "string"
    # then, we create a boolean mask to filter "salary" by int64
    # this will fail expectedly; We can't compare str with int
    df["salary"] = df["salary"].astype("string")

    # error here
    boolean_mask: pd.Series = df["salary"] > 30
