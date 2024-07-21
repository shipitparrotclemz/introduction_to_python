import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.read_csv("wage_bros.csv")
    """
    filter_only_gabe
    False (aaron)
    False (clement)
    False (elson)
    False (zheng yang)
    True (eugene)
    False (gabe)
    False (wei xuan)
    """
    filter_only_gabe: pd.Series = df["name"] == "gabe"
    """
    filter_only_gabe
    False (aaron)
    False (clement)
    False (elson)
    False (zheng yang)
    False (eugene)
    True (gabe)
    False (wei xuan)
    """
    filter_only_eugene: pd.Series = df["name"] == "eugene"
    """
    | here means an OR
    
    filter_only_gabe
    False or False = False(aaron)
    False or False = False (clement)
    False or False = False (elson)
    False or False = False (zheng yang)
    False or True = True (eugene)
    True or False = True (gabe)
    False or False = False (wei xuan)
    """
    filter_mask: pd.Series = filter_only_gabe | filter_only_eugene
    filtered_df: pd.DataFrame = df.loc[filter_mask, :]
    print(filtered_df)
