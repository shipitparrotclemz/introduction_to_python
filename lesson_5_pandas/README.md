# Installing dependencies

At your root (introduction_to_python)

Create a virtual environment -> fancy box containing your installed 3rd party code

```commandline
poetry shell
```

Put your 3rd party code into your box

```commandline
poetry install --no-root
```

Install a dependency

```commandline
poetry add pandas
```

```commandline
pip install pandas
```

Check if a dependency exist -> Check if pandas is installed

```commandline
pip3 freeze | grep pandas
```

# Pandas

Pandas is one of the most important libraries for data transformation and analysis

Pandas introduces two Columnar table like data structures
- Q: Columnar? What does that mean?
- In these data structures, the data in a single column is stored side by side
- This makes it very fast, if you want to do data transformations involving 1 column
- Data transformations that involves one column: Mean of 1 column, Median of 1 column, Sum of 1 column

Example of a row-based table like data structures
-> Data in a row is stored side by side

name,age,color
xuan,29,black and white
     ^
aaron,32,black and white
      ^

Pandas is column based -> It looks something like this below
-> pd.DataFrame -> class that allows you to create your own efficient columnar table like data structure
- But if i want to simplify this explanation further
- pd.DataFrame -> table like data structure

Q: Since pandas has multiple columns in it's pd.DataFrame, what is the class that represents a column?
- pd.Series

name,xuan,aaron -> notice your column data is all stored side by side in disk (your long term memory)
age,29,32
    ^  ^
color,black and white, black and white

If i want to sum age, notice i only have to scan a few cells

## Use Cases
1. Read CSV files and Excel files

```python
import pandas as pd

# read csv
df: pd.DataFrame = pd.read_csv("path_to_your_file.csv")

# read excel
df: pd.DataFrame = pd.read_excel("path_to_your_excel.csv")
```

2. Do filtering

```python
import pandas as pd
from typing import Any 

my_list: list[dict[str, Any]] = [
    {
        "name": "xuan", "likes": "chocolate cake",
    },
    {
        "name": "aaron", "likes": "taiwan girls",
    },
    {
        "name": "clement", "likes": "short taiwan girls",
    },
    {
        "name": "elson", "likes": "scam auntie money",
    }
]

df: pd.DataFrame = pd.DataFrame(my_list)

# filter for only 1st row; 

name,likes
xuan,chocolate cake

filtered_df: pd.DataFrame = df.iloc[0, :] # -> filters for only xuan
```

## Prerequisite

1. Object Oriented Programming -> We use classes as blueprints to create an object, and objects as instances of that class
- If you want to create a Cat in code, we will create a Cat class

```python
class Cat:
    """
    Blueprint to create a Cat in code
    """
    def __init__(self, name: str, age: int, color: str) -> None:
        self.name: str = name
        self.age: int = age
        self.color: str = color

if __name__ == "__main__":
    """
    Create a Cat object
    """
    xuan: Cat = Cat(name="Xuan", age=29, color="black and white")
    aaron: Cat = Cat(name="Aaron", age=32, color="black and white")
    clemz: Cat = Cat(name="Clemz", age=29, color="black and white")
    elson: Cat = Cat(name="Elson", age=29, color="black and white")
```

Q: What does this Object Oriented Programming have to do with Pandas?

A: Pandas really gives you it's own classes
- `pandas.DataFrame` -> Table, multiple column
- Notice we used a new concept: The constructor
- The constructor is a fancy word for the function, used to create an object
- To call the constructor, its ClassName(input1, input2, input3)
- ClassName here is DataFrame

```python
import pandas as pd

if __name__ == "__main__":
    df: pd.DataFrame = pd.DataFrame([{
        "name": "Xuan", "age": 29, color: "black and white"
    }])
```

- `pandas.Series` -> column itself

## Concept 1: Reading a list[dict[str, str]] (in-memory) into a pandas.DataFrame
- Create a `list[dict[str, str]]`
- Pass it to the `pd.DataFrame` constructor

```python
python 001_creating_df_from_list_dict.py
      name               likes
0     xuan      chocolate cake
1    aaron        taiwan girls
2  clement  short taiwan girls
3    elson   scam auntie money

```

## Concept 2: Reading a CSV file
- Create a CSV file (`.csv`)
- Read the CSV file with `pd.read_csv(path_to_csv)`

```python
python 002_reading_csv_into_df.py
      name               likes
0     xuan      chocolate cake
1    aaron        taiwan girls
2  clement  short taiwan girls
3    elson   scam auntie money
```

## Concept 3: Reading a Excel file
- Create an Excel file (`.xlsx`)
- Read the excel file with `pd.read_excel(path_to_excel)`

```python
python 003_reading_excel_into_df.py
      name               likes
0     xuan     chocolate cakes
1    aaron        taiwan girls
2  clement  short taiwan girls
3    elson   scam auntie money
```

## Concept 4: Filter Row by Index
- Use Exercise 1; Create a `list[dict[str,str]]`
- Pass it to the `pd.DataFrame` constructor
- Call `df.iloc[0:2, :]` to filter for the first two rows, with all columns

```python
python 004_filter_rows_by_index_with_iloc.py 
    name           likes
0   xuan  chocolate cake
1  aaron    taiwan girls
```

## Concept 5: Filter Columns by Index
- Use Exercise 1; Create a `list[dict[str, str]]`, add another columnage
- Pass it to the `pd.DataFrame` constructor
- Call `df.iloc[:, 0:2]` to get all rows, but filter for first two columns

```python
python 005_filter_columns_by_index_with_iloc.py 
df
      name               likes  age
0     xuan      chocolate cake   29
1    aaron        taiwan girls   29
2  clement  short taiwan girls   29
3    elson   scam auntie money   29
filtered_df
      name               likes
0     xuan      chocolate cake
1    aaron        taiwan girls
2  clement  short taiwan girls
3    elson   scam auntie money
```

## Concept 6: Filter by both Rows and Columns by Index
- Use Exercise 1; Create a `list[dict[str, str]]`, add another columnage
- Pass it to the `pd.DataFrame` constructor
- Call `df.iloc[0:2, 0:2]` to get first two rows, filter for first two columns

```python
python 006_filter_rows_and_columns_by_index_with_iloc.py 
df
      name               likes  age
0     xuan      chocolate cake   29
1    aaron        taiwan girls   29
2  clement  short taiwan girls   29
3    elson   scam auntie money   29
filtered_df
    name           likes
0   xuan  chocolate cake
1  aaron    taiwan girls
```