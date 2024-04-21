import pandas as pd

if __name__ == "__main__":
    # you need openpyxl as an additional dependency
    # on top of pandas to do this
    df: pd.DataFrame = pd.read_excel("003_my_excel.xlsx")
    print(df)