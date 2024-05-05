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
        
    def meow(self) -> None:
        print("meow")

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

## Concept 7: Filtering rows by equal condition; Filter only for rows whose name == "elson"

```commandline
python 007_filter_rows_by_equal_condition_with_loc.py 
equal_elson
0    False
1    False
2    False
3     True
4    False
Name: name, dtype: bool
filtered_df
    name              likes
3  elson  scam auntie money
```

## Concept 8: Filtering rows by condition; Filter only for rows whose name contains "elson"

```commandline
python 008_filter_rows_by_contain_condition_with_loc.py 
contains_elson
0    False
1    False
2    False
3     True
4     True
Name: name, dtype: bool
filtered_df
           name              likes
3         elson  scam auntie money
4  elson gorgor  scam auntie money
```

## Concept 9: Increase salary in a column by 10%

Step 1: Load DataFrame
- `df: pd.DataFrame = pd.read_csv("your_file.csv")`

Step 2: Select and make a copy of the salary column with
- `copy_of_salary_column: pd.Series = df.loc[:, ["salary"]]`

Step 3: Make yet another copy, but this with increased salary
- `copy_of_increased_salary_column: pd.Series = copy_of_salary_column * 1.1`
- This will have the salary column multiplied by 1.1

Step 4: Assign this second increased salary column to your data frame
- `df["salary"] = copy_of_increased_salary_column`

## Concept 10: Checking Types of a pd.DataFrame with `df.info()`

1. pd.DataFrame has columns (pd.Series), and pandas by default, will infer the type of the column when you load it

In the example below, we created a simple pd.DataFrame
- We can see pandas, by default, correctly detects the age column is of type int64
- The name is not correctly inferred as a string, but that's fine

```python
>>> import pandas as pd
>>> df = pd.DataFrame([{"name": "xuan", "age": 29}])
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    1 non-null      object
 1   age     1 non-null      int64 
dtypes: int64(1), object(1)
memory usage: 148.0+ bytes
```

### Q: What is int64?

Short Answer:

It represents a number from -2**63 to 2**63

Long Answer:

Concept 1: Computers represent data with bits; switches that can either be 0 or 1

0 -> open circuit
1 -> closed circuit

int64? -> integer represented by 64 bits
1 bit = 1 switch

Concept 2: Possible numbers represented with bits follow 2**number_of_bits

With 1 bit, we can represent 2 numbers (2**1)

0 -> 1st state
1 -> 2nd state

With 2 bits, we can represent 4 numbers (2**2)

00 -> 0
01 -> 1
10 -> 2
11 -> 3

With 3 bits, we can represent 8 numbers (2**3)

000 -> 0
001 -> 1
010 -> 2
011 -> 3
100 -> 4
101 -> 5
110 -> 6
111 -> 7

With 64 bits, we can represent 1.8 * 10**19 (2**64)

1st bit for sign -> positive or negative
Use the subsequent 63 bits for the actual number (without sign)

Hence, the range of int64 is from -2**63 to 2**63

## Concept 11: Changing the type of a column (pd.Series) in a table (pd.DataFrame)

1. Before creating the boolean mask for filtering with df.loc, please remember to ensure the column you are filtered by is of the right type

If it is not the right type, you can change the column type with the following

```
df["name"] = df["name"].astype("string")
```

```python
python 011_changing_type_of_column.py
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    5 non-null      object
 1   salary  5 non-null      int64 
dtypes: int64(1), object(1)
memory usage: 212.0+ bytes
None
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    5 non-null      string
 1   salary  5 non-null      int64 
dtypes: int64(1), string(1)
memory usage: 212.0 bytes
None
```

## Concept 12: Purposely creating an error during filtering with an incorrect column type

1. If you don't ensure you have the right type, you can get an Exception when filtering, or worse, silently fail and perform a bad filter

Here is an example:
- We purposely change the type of "age" column to a bad type; String, and try filtering by int
- We will get an exception

```
# purposely set salary to be the wrong type; str
df["salary"] = df["salary"].astype("str")
# now we create a bad boolean mask that filters for salary by an int
# this will fail of course; we can't compare str with int
df = df.loc[df["salary"] > 30]
TypeError: '>' not supported between instances of 'str' and 'int'```
```

## Concept 13: How to calculate mean across an age column
- `df["age"].mean()`

## Concept 14: How to calculate median across an age column
- `df["age"].median()`

## Concept 15: (Analogous to GROUP BY in SQL) How to group rows in pd.DataFrame by column
- `df.group_by`
- Lets say you have 10,000 grandmas, from different towns
- How do you group the 10,000 rows of grandmas, by their town column

## Concept 16: (Analogous to JOIN in SQL) How to find ahma that exists in Yew Tee Community Club but not in CCK Community Club
- `pd.merge`