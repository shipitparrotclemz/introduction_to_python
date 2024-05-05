"""
Given a CSV file

```
name,salary
xuan,10000
aaron,10000
clement,10000
elson,10000
eugene,10000
```

Let's say we want to increase salary by 10%
- Transform salary * 1.1
"""

# Concept 1: Import pandas
import pandas as pd

if __name__ == "__main__":
    # Concept 2: Reading a CSV file into memory
    # Store it as a columnar data structure; the pd.DataFrame
    df: pd.DataFrame = pd.read_csv("009_salary.csv")
    print("DF before transformation:")
    print(df)

    # (New) Concept 3: How to transform a single column in a data frame

    # Transform -> select "salary" column
    # Multiply each value by 1.1
    # Step 1: Make a copy of the salary series from the pd.DataFrame
    # loc here gives back a copy of the column
    salary_series_copy_one: pd.Series = df.loc[:, ["salary"]]

    # Then, we make yet another copy, this time with the transformed data
    # but you need to set this copy as your new column
    # Salary: 11,000
    increased_salary_copy_two: pd.Series = salary_series_copy_one * 1.1

    print("salary_series_copy_one")
    print(salary_series_copy_one)
    print("increased_salary_copy_two")
    print(increased_salary_copy_two)

    # set the old column to the new transformed column
    df["salary"] = increased_salary_copy_two
    print("DF after transformation:")
    print(df)





